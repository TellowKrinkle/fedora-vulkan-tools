%undefine _cmake_shared_libs

Name:           gfxreconstruct
Version:        1.4.335.0
Release:        1%{?dist}
Summary:        Vulkan API Capture and Replay Tools

License:        MIT
URL:            https://github.com/LunarG/gfxreconstruct
Source0:        %{url}/archive/vulkan-sdk-%{version}/gfxreconstruct-vulkan-sdk-%{version}.tar.gz
Source1:        https://github.com/KhronosGroup/SPIRV-Reflect/archive/vulkan-sdk-%{version}/SPIRV-Reflect-vulkan-sdk-%{version}.tar.gz

BuildRequires:  g++
BuildRequires:  cmake
BuildRequires:  pkgconfig(liblz4)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(openxr)
BuildRequires:  pkgconfig(wayland-client)
BuildRequires:  pkgconfig(xcb)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  spirv-headers-latest-devel
BuildRequires:  vulkan-headers >= %{version}

%description
%{summary}

%package        tools
Summary:        Tools for manipulating and replaying gfxreconstruct captures

%description    tools
%{summary}

%prep
%autosetup -n gfxreconstruct-vulkan-sdk-%{version}
tar -C external/SPIRV-Reflect --strip-components=1 -xf %{SOURCE1}
mkdir -p external/Vulkan-Headers/include
mkdir -p external/SPIRV-Headers/include
mkdir -p external/OpenXR-SDK/include
ln -s /usr/include/vulkan   external/Vulkan-Headers/include/
ln -s /usr/include/vk_video external/Vulkan-Headers/include/
ln -s /usr/include/spirv    external/SPIRV-Headers/include/
ln -s /usr/include/openxr   external/OpenXR-SDK/include/
sed -i "s|add_subdirectory(\${PROJECT_SOURCE_DIR}/external/OpenXR-SDK)|find_package(OpenXR REQUIRED)|" CMakeLists.txt
sed -i "s/if defined(_WIN64) || defined(__x86_64__) || defined(__aarch64__)/if (XR_PTR_SIZE == 8)/g" framework/*/*.{h,cpp}

%build
%cmake -DCMAKE_BUILD_TYPE=Release -DBUILD_WERROR=OFF
%cmake_build

%install
%cmake_install

%files
%{_libdir}/libVkLayer*
%{_datadir}/vulkan
%{_datadir}/openxr

%files          tools
%{_bindir}/gfxrecon*

%changelog
* Wed Nov 26 2025 TellowKrinkle <tellowkrinkle@gmail.com> - 1.4.328.1-1
- Update to 1.4.328.1
