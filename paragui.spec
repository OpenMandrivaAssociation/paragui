%define Docs paraguidoc-html-1.1.8
%define	name	paragui
%define	version	1.1.8
%define	release	%mkrel 15

%define lib_api 1.1
%define lib_major 8
%define lib_name %mklibname %{name} %{lib_api} %{lib_major}
%define develname %mklibname -d paragui

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Graphical User Interface based on SDL
License:	LGPL
Group:		System/Libraries
Source0:	http://savannah.nongnu.org/download/paragui/%{name}-%{version}.tar.bz2
Source1:        http://savannah.nongnu.org/download/paraguidoc-html-1.1.8.tar.bz2
Patch0:		%{name}-1.1.8.install.patch
Patch1:		paragui-1.1.8-fix-underquoted-calls.patch
Patch2:		paragui-1.1.8-asneeded.patch
Patch3:		paragui-1.1.8-header.patch
Patch4:		020_stl_map.diff
Patch5:		paragui-1.1.8-remove-physfs.patch
URL:		http://www.bms-austria.com/projects/paragui/
BuildRequires:	freetype2-devel
BuildRequires:	physfs-devel
BuildRequires:	libSDL-devel
BuildRequires:	libSDL_image-devel
BuildRequires:	libgii-devel
BuildRequires:	libsigc++1.2-devel
BuildRequires:	libexpat-devel
BuildRequires:	multiarch-utils >= 1.0.3
BuildRequires:	automake1.8
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
ParaGUI is a cross-platform high-level application framework and GUI
(graphical user interface) library. ParaGUI's cross-platform nature is
completely based on the Simple DirectMedia Layer (SDL).

%package -n	%{lib_name}
Summary:	Main library for paragui
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with paragui.

%package -n	%{develname}
Summary:	Headers for developing programs that will use paragui
Group:		Development/C
Requires:	%{lib_name} = %{version}
Requires:	libexpat-devel
Requires:	physfs-devel
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d paragui 1.1 8} < %version-%release

%description -n	%{lib_name}-devel
This package contains the headers that programmers will need to develop
applications which will use paragui, a GUI on top of SDL.

%prep
%setup -q -n %{name}-%{version} -a1
%patch0 -p1
%patch1 -p1 -b .underquoted
%patch2 -p0
%patch3 -p0 -b .header
%patch4 -p1 -b .stl
%patch5 -p1 -b .physfs

%build
# TODO : --enable-python --enable-ruby
aclocal
autoconf 
automake --foreign
%configure2_5x --enable-unicode --disable-static
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%multiarch_binaries %{buildroot}%{_bindir}/paragui-config

%if %mdkversion < 200900
%post -n %{lib_name} -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %{lib_name} -p /sbin/ldconfig
%endif

%clean
rm -rf %{buildroot}

%files -n %{lib_name}
%defattr(-, root, root)
%doc AUTHORS COPYING
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc README
%multiarch %{multiarch_bindir}/paragui-config
%{_bindir}/paragui-config
%{_includedir}/*
%{_libdir}/*.?a
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal/*.m4
%{_datadir}/%{name}
