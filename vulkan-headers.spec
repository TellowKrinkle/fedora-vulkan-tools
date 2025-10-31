%global __python %{__python3}
Name:           vulkan-headers-latest
Version:        1.4.331
Release:        %autorelease
Summary:        Vulkan Header files and API registry

License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-Headers
Source0:        %url/archive/v%{version}/Vulkan-Headers-%{version}.tar.gz

BuildRequires:  cmake3
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildArch:      noarch
Provides:       vulkan-headers = %{version}-%{release}
Conflicts:      vulkan-headers

%description
Vulkan Header files and API registry

%prep
%autosetup -n Vulkan-Headers-%{version}


%build
%cmake3 -DCMAKE_INSTALL_LIBDIR=%{_libdir} -GNinja
%cmake_build

%install
%cmake_install


%files
%license LICENSE.md
%doc README.md
%{_includedir}/vulkan/
%{_includedir}/vk_video/
%dir %{_datadir}/vulkan/
%dir %{_datadir}/cmake/VulkanHeaders/
%{_datadir}/vulkan/registry/
%{_datadir}/cmake/VulkanHeaders/*.cmake


%changelog
%autochangelog
