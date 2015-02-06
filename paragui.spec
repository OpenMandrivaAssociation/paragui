%define Docs paraguidoc-html-1.1.8
%define	name	paragui
%define	version	1.1.8
%define release	22

%define lib_api 1.1
%define lib_major 8
%define lib_name %mklibname %{name} %{lib_api} %{lib_major}
%define develname %mklibname -d paragui

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Graphical User Interface based on SDL
License:	LGPLv2+
Group:		System/Libraries
Source0:	http://savannah.nongnu.org/download/paragui/%{name}-%{version}.tar.bz2
Source1:        http://savannah.nongnu.org/download/paraguidoc-html-1.1.8.tar.bz2
Patch0:		%{name}-1.1.8.install.patch
Patch1:		paragui-1.1.8-fix-underquoted-calls.patch
Patch2:		paragui-1.1.8-asneeded.patch
Patch3:		paragui-1.1.8-header.patch
Patch4:		020_stl_map.diff
Patch5:		paragui-1.1.8-remove-physfs.patch
URL:		http://www.paragui.org/
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	physfs-devel
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(SDL_image)
BuildRequires:	libgii-devel
BuildRequires:	pkgconfig(sigc++-2.0)
BuildRequires:	pkgconfig(expat)
BuildRequires:	multiarch-utils >= 1.0.3
BuildRequires:	automake1.8

%description
ParaGUI is a cross-platform high-level application framework and GUI
(graphical user interface) library. ParaGUI's cross-platform nature is
completely based on the Simple DirectMedia Layer (SDL).

%package -n	%{lib_name}
Summary:	Main library for paragui
Group:		System/Libraries
Provides:	%{name} = %{version}-%{release}
Obsoletes:	%{mklibname paragui 1.1} < %{version}-%{release}

%description -n	%{lib_name}
This package contains the library needed to run programs dynamically
linked with paragui.

%package -n	%{develname}
Summary:	Headers for developing programs that will use paragui
Group:		Development/C
Requires:	%{lib_name} = %{version}
Requires:	pkgconfig(expat)
Requires:	physfs-devel
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%{mklibname -d paragui 1.1 8} < %version-%release
Obsoletes:      %{mklibname -d paragui 1.1} < %{version}-%{release}

%description -n	%{develname}
This package contains the headers that programmers will need to develop
applications which will use paragui, a GUI on top of SDL.

%prep
%setup -q -n %{name}-%{version} -a1
%patch0 -p1
%patch1 -p1 -b .underquoted
%patch2 -p1 -b .asneeded
%patch3 -p0 -b .header
%patch4 -p1 -b .stl
%patch5 -p1 -b .physfs

%build
# TODO : --enable-python --enable-ruby
export AUTOMAKE="automake --foreign"
autoreconf -fi
%configure2_5x --enable-unicode --disable-static
%make

%install
%makeinstall_std
%multiarch_binaries %{buildroot}%{_bindir}/paragui-config

%files -n %{lib_name}
%defattr(-, root, root)
%doc AUTHORS COPYING
%{_libdir}/*.so.*

%files -n %{develname}
%defattr(-,root,root)
%doc README
%{multiarch_bindir}/paragui-config
%{_bindir}/paragui-config
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/%{name}.pc
%{_datadir}/aclocal/*.m4
%{_datadir}/%{name}


%changelog
* Fri Oct 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.8-19mdv2010.0
+ Revision: 452525
- rediff patch 2 for fuziness
- rebuild for new libphysfs

  + Thierry Vignaud <tvignaud@mandriva.com>
    - rebuild

* Sun Aug 17 2008 Funda Wang <fundawang@mandriva.org> 1.1.8-17mdv2009.0
+ Revision: 272983
- rebuild for new dfb

* Sat Jun 21 2008 Funda Wang <fundawang@mandriva.org> 1.1.8-16mdv2009.0
+ Revision: 227678
- Obsoletes old package name

* Sat Jun 21 2008 Funda Wang <fundawang@mandriva.org> 1.1.8-15mdv2009.0
+ Revision: 227662
- add ubuntu patch: use stl map all the time, drop physfs subdir
- refine gcc 4.3 patch
- add gentoo patches

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tvignaud@mandriva.com>
    - kill re-definition of %%buildroot on Pixel's request
    - fix autoconf-2.5x path

* Fri Jun 08 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 1.1.8-14mdv2008.0
+ Revision: 36977
- rebuild for expat

  + Herton Ronaldo Krzesinski <herton@mandriva.com.br>
    - Rebuild with libslang2.

* Sat May 26 2007 Funda Wang <fundawang@mandriva.org> 1.1.8-12mdv2008.0
+ Revision: 31416
- Rebuild for directfb 1.0


* Wed Mar 21 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.8-11mdv2007.1
+ Revision: 147155
- fix build dependencies

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - bunzip patches
    - rebuild
    - Import paragui

* Sat Aug 26 2006 Olivier Blin <blino@mandriva.com> 1.1.8-9mdv2007.0
- rebuild for physfs (#24545)

* Tue Aug 15 2006 Emmanuel Andry <eandry@mandriva.org> 1.1.8-8mdv2007.0
- rebuild for physfs
- disable parallel make to fix x86_64 compilation

* Sun Jul 16 2006 Anssi Hannula <anssi@mandriva.org> 1.1.8-7mdv2007.0
- fix buildrequires

* Tue Jun 20 2006 Charles A Edwards <eslrahc@mandriva.org> 1.1.8-6mdv2007.0
- rebuild for libpng
- add documentation in devel pkg

* Wed Jun 07 2006 Charles A Edwards <eslrahc@mandriva.org> 1.1.8-5mdv2007.0
- enable unicode support

* Tue Jan 31 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.1.8-4mdk
- fix buildrequires

* Tue Jan 31 2006 Per Øyvind Karlsen <pkarlsen@mandriva.com> 1.1.8-3mdk
- fix underquoted calls (P1)
- %%mkrel

* Thu Dec 29 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.8-2mdk
- fix x86_64 build
- spec cleanup

* Fri Nov 11 2005 Michael Scherer <misc@mandriva.org> 1.1.8-1mdk
- New release 1.1.8
- mkrel
- update major

* Thu Jul 01 2004 Michael Scherer <misc@mandrake.org> 1.0.4-2mdk 
- rebuild for new gcc
- clean BuildRequires
- remove Packager tag
- rpmbuildupdate aware

