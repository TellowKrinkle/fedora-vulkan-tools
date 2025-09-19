%global commit 402d0b3f024f8b1e2fbe297e16fc52023df164df
%global shortcommit %(c=%{commit}; echo ${c:0:7})

Name:           spirv-headers-latest
Version:        1.4.327
Release:        %autorelease
Summary:        Header files from the SPIR-V registry

License:        MIT
URL:            https://github.com/KhronosGroup/SPIRV-Headers/
Source0:        %{url}/archive/%{commit}/%{name}-%{shortcommit}.tar.gz

BuildArch:      noarch

BuildRequires:  cmake3
BuildRequires:  ninja-build
BuildRequires:  gcc
BuildRequires:  gcc-c++
Provides:       spirv-headers = 1.5.5
Conflicts:      spirv-headers

%description
%{summary}

This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.
* The XML registry file

%package        devel
Summary:        Development files for %{name}

%description    devel
%{summary}

This includes:

* Header files for various languages.
* JSON files describing the grammar for the SPIR-V core instruction
  set, and for the GLSL.std.450 extended instruction set.
* The XML registry fil

%prep
%autosetup -n SPIRV-Headers-%{commit}
chmod a-x include/spirv/1.2/spirv.py


%build
%cmake3 -DCMAKE_INSTALL_LIBDIR=%{_lib} -GNinja
%cmake_build

%install
%cmake_install

%files devel
%license LICENSE
%doc README.md
%{_includedir}/spirv/
%{_datadir}/cmake/SPIRV-Headers/*.cmake
%{_datadir}/pkgconfig/SPIRV-Headers.pc

%changelog
%autochangelog
