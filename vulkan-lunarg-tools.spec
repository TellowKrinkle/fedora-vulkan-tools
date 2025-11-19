%global is_sdk 0

Name:           vulkan-lunarg-tools
Version:        1.4.333
Release:        1%{?dist}
Summary:        LunarG Vulkan tools

%if %{is_sdk}
	%define tag vulkan-sdk-%{version}
	%define zip %{tag}
%else
	%define tag v%{version}
	%define zip %{version}
%endif

License:        Apache-2.0
URL:            https://github.com/LunarG/VulkanTools
Source0:        %{url}/archive/%{tag}/VulkanTools-%{zip}.tar.gz

BuildRequires:  g++
BuildRequires:  cmake
BuildRequires:  cmake(Qt6Core)
BuildRequires:  cmake(Qt6Gui)
BuildRequires:  cmake(Qt6Network)
BuildRequires:  cmake(Qt6Widgets)
BuildRequires:  cmake(valijson)
BuildRequires:  cmake(VulkanLoader)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  vulkan-headers >= %{version}
BuildRequires:  vulkan-utility-libraries-devel >= %{version}

%description
%{summary}

%package -n     vulkan-extra-layers
Summary:        Extra layers for Vulkan development

%description -n vulkan-extra-layers
Extra layers for Vulkan development

%package -n     vulkan-extra-tools
Summary:        Vulkan Configurator

%description -n vulkan-extra-tools
Vulkan Configurator

%prep
%autosetup -n VulkanTools-%{zip}

%build
%cmake -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install

%files -n vulkan-extra-layers
%{_libdir}/libVkLayer*
%{_datadir}/vulkan

%files -n vulkan-extra-tools
%{_bindir}/vkconfig-gui
%{_bindir}/vkconfig

%changelog
* Mon Aug 04 2025 TellowKrinkle <tellowkrinkle@gmail.com> - 1.4.321-1
- Update to 1.4.321
