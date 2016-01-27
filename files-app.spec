%define debug_package %nil
%define snap %nil

Summary:	File manager
Name:		files-app
Version:	0.0.5
Release:	1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/papyros/files-app
# git clone https://github.com/papyros/files-app.git
# git archive --format=tar --prefix files-app-0.0.5-$(date +%Y%m%d)/ HEAD | xz -vf > files-app-0.0.5-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{version}.tar.gz
BuildRequires:	pkgconfig(Qt5Core)
BuildRequires:	pkgconfig(Qt5Quick)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	pkgconfig(Qt5Widgets)
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	qml-material
BuildRequires:	pkgconfig(taglib)
BuildRequires:	intltool

%description
The file manager for Papyros

%prep
%setup -q

%build
%cmake_qt5
%make

%install
%makeinstall_std -C build
%find_lang io.papyros.files

%files -f io.papyros.files.lang
%{_bindir}/papyros-files
%{_datadir}/applications/io.papyros.files.desktop
%{_datadir}/papyros-files/qml/
%{_qt5_libdir}/qt5/qml/com
%{_qt5_libdir}/qt5/qml/org
