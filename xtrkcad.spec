# spec file for package xtrkcad version 5.2.0GA Release
#
# Copyright (c) 2020 SUSE LINUX GmbH, Nuernberg, Germany.
# Copyright (c) 2020 Gilles laffite,France <gilles.laffite76@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via <gilles.laffite76@gmail.com>
#
%define name xtrkcad
%define version 5.2.0GA
Name: %{name}
Version: %{version}
Release: 1
License: GPL-2.0-or-later
Summary: XTrackCAD is a CAD program for designing model railroad layouts
Url:  http://www.xtrkcad.org
Group:  Productivity/Graphics/Other
Source: xtrkcad-source-%{version}.tar.bz2
BuildRequires: cmake >= 2.8
BuildRequires: cairo-devel
BuildRequires: doxygen
BuildRequires: fdupes
BuildRequires: gcc-c++
BuildRequires: gettext-runtime
BuildRequires: gettext-devel
BuildRequires: glib2-devel
BuildRequires: glibc-devel
BuildRequires: gtk2-devel
BuildRequires: libzip-devel
BuildRequires: pkgconfig
BuildRequires: zlib-devel
BuildRequires: update-desktop-files
BuildRequires: pandoc

BuildRoot:      %{_tmppath}/%{name}-%{version}-build

Recommends: %{name}-lang

%lang_package

%description
XTrackCAD is a CAD program for designing model railroad layouts. You can easily create layout of any scale or size. Libraries for many brands of track and turnouts are included.Adding new components is easy with the built-in editor

Authors:
--------
    Laffite Gilles <gilles.laffite76@gmail.com>

%prep
ln -s xtrkcad-source-%{version} xtrkcad-%{version}

%setup -qn %{name}-source-%{version}
 
%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_C_FLAGS="$RPM_OPT_FLAGS -lm -Wl,--allow-multiple-definition " \
    -DCMAKE_EXE_LINKER_FLAGS="$RPM_OPT_FLAGS -lm -Wl,--allow-multiple-definition" \
    -DBUILD_SHARED_LIBS:BOOL=OFF \
    -DXTRKCAD_USE_GETTEXT=ON \
    -DXTRKCAD_USE_GTK=ON \
    -DXTRKCAD_USE_GTK_CAIRO=ON \
    -Wno-dev
    
%cmake_build
 
%install
%cmake_install

# Fix mime, docs, desktop to the correct location
%__mkdir -p %{buildroot}%{_datadir}/doc/packages/%{name}
%__mv %{buildroot}%{_datadir}/%{name}/CHANGELOG.txt %{buildroot}%{_datadir}/doc/packages/%{name}/
%__mv %{buildroot}%{_datadir}/%{name}/Readme.txt %{buildroot}%{_datadir}/doc/packages/%{name}/

%__mkdir -p %{buildroot}%{_datadir}/pixmaps
%__mkdir -p %{buildroot}%{_datadir}/applications
%__mkdir -p %{buildroot}%{_datadir}/mime/packages

%__mv %{buildroot}%{_datadir}/%{name}/pixmaps/xtrkcad.png  %{buildroot}%{_datadir}/pixmaps/
%__mv %{buildroot}%{_datadir}/%{name}/applications/xtrkcad.xml %{buildroot}%{_datadir}/mime/packages/
%__mv %{buildroot}%{_datadir}/%{name}/applications/xtrkcad.desktop %{buildroot}%{_datadir}/applications/

%__install -dm 755 %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=XTrackCAD
Name[fr]=XTrackCAD
GenericName=CAD program for designing Model Railroad layouts
GenericName[de]=CAD-Programm zum Entwerfen von Modelleisenbahn-Layouts
GenericName[fi]=CAD-ohjelma rautatiemallien suunnittelun suunnitteluun
GenericName[fr]=Programme CAO modèlisme chemin de fer
GenericName[ja]=鉄道模型のレイアウトを設計するためのCADプログラム
GenericName[pt]=Programa CAD para projetar layouts de modelo de ferrovia
GenericName[ru]=Программа САПР для проектирования макетов Модельной железной дороги
Comment=Design model railroad layouts
Comment[de]=Design Modelleisenbahn Layouts
Comment[fi]=suunnittelumallin rautatiejärjestelyt
Comment[fr]=Concevoir des modèles de chemin de fer
Comment[ja]=鉄道模型のレイアウトを設計する
Comment[pt]=projetar layouts de modelo de ferrovia
Comment[ru]=роектирование макетов железных дорог
Exec=xtrkcad
Icon=xtrkcad
Terminal=false
Type=Application
Categories=Graphics;2DGraphics
EOF

%suse_update_desktop_file %{name} Graphics 2DGraphics

# Fix bugs rpmlint warning
%fdupes %{buildroot}%{_datadir}/%{name}/html/png.d/
       
%find_lang %{name} 

%files
%defattr(-,root,root)
%license app/COPYING
%_docdir/%name
%{_bindir}/%{name}
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png
%{_datadir}/mime/packages/xtrkcad.xml
%files lang -f %{name}.lang

%changelog
*Sun Apr 18 20:37:50 UTC 2021 - Laffite Gilles <gilles.laffite76@gmail.com>
-Version 5.2.0Beta3.0 merge into version 5.2.0GA Release
 -Bugs: -COPYING shebang (no modifications)
        -Lang cy_GB build refuse (no modifications)
         
*Sat Mar 06 20:10:50 UTC 2021 - Laffite Gilles <gilles.laffite76@gmail.com>
-Import source xtrkcad 5.2.0Beta3.0
 -Utilise Pandoc for files doc and replace locate
 -Fix bugs rpmlint duplicate file
 -Bugs COPYING shebang (no modifications)
 -Insert New Desktop file (.spec) with new translations
 
*Mon Nov 02 19:16:50 UTC 2020 - Laffite Gilles <gilles.laffite76@gmail.com>
-Import source xtrkcad 5.2.0Beta3.0
 -Modified source
-Fix xtrkcad.desktop
-Modified xtrkcad.spec
 -Insert Xtrkcad use gtk cairo
 
*Thu Sep 03 15:41:22 UTC 2020 - Laffite Gilles <gilles.laffite76@gmail.com>
-Import xtrkcad-source 5.2.0Beta2.1
-Modified xtrkcad.spec
-Fix xtrkcad.desktop
-Modified source xtrkcad-source 5.2.0Beta2.1
-  Insert XTRKCAD_USE_GETTEXT ON
-  Modified flags
-Source imported lang Ru

*Sat Apr 18 07:46:05 UTC 2020 - Laffite Gilles <gilles.laffite76@gmail.com>
- modified xtrkcad.spec
  -insert BuildRequires: doxygen
  -insert BuildRequires: gettext-runtime
  
*Tue Apr  7 16:15:29 UTC 2020 - gilles.laffite76@gmail.com
- Initial import xtrkcad 5.1.2a

*Wed May 30 23:19:41 UTC 2018 - gboiko@suse.com
- Initial import
   
