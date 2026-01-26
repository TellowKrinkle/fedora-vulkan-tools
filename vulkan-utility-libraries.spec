%global is_sdk 0
%global debug_package %{nil}

Name:           vulkan-utility-libraries-latest
Version:        1.4.341
Release:        %autorelease
Summary:        Vulkan utility libraries

%if %{is_sdk}
	%define tag vulkan-sdk-%{version}
	%define zip %{tag}
%else
	%define tag v%{version}
	%define zip %{version}
%endif

License:        Apache-2.0
URL:            https://github.com/KhronosGroup/Vulkan-Utility-Libraries
Source0:        %url/archive/%{tag}/Vulkan-Utility-Libraries-%{zip}.tar.gz

BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  cmake3
BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  vulkan-headers >= %{version}
Provides:       vulkan-utility-libraries = %{version}-%{release}
Provides:       vulkan-utility-libraries%{?_isa} = %{version}-%{release}

%description
%{summary}

%package        devel
Summary:        Development files for %{name}
Requires:       vulkan-headers >= %{version}
Obsoletes:      vulkan-validation-layers-devel < 1.3.268.0-2
Provides:       vulkan-validation-layers-devel = %{version}-%{release}
Provides:       vulkan-validation-layers-devel%{?_isa} = %{version}-%{release}
Provides:       vulkan-utility-libraries-devel = %{version}-%{release}
Provides:       vulkan-utility-libraries-devel%{?_isa} = %{version}-%{release}
Conflicts:      vulkan-utility-libraries-devel%{?_isa}

%description    devel
%{summary}

%prep
%autosetup -p1 -n Vulkan-Utility-Libraries-%{zip}

%build
%cmake3 -DCMAKE_BUILD_TYPE=Release \
        -DCMAKE_INSTALL_LIBDIR=%{_libdir} \
        -DBUILD_TESTS:BOOL=OFF \
        -DVUL_WERROR:BOOL=OFF \
        -DUPDATE_DEPS:BOOL=OFF
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE.md
%doc README.md
%{_includedir}/vulkan/
%{_libdir}/cmake/VulkanUtilityLibraries/*.cmake
%{_libdir}/libVulkanLayerSettings.a
%{_libdir}/libVulkanSafeStruct.a

%changelog
%autochangelog
