%define debug_package %nil
%define snap	20150325

Summary:	File manager
Name:		files-app
Version:	0.0.0
Release:	0.%{snap}.1
License:	GPLv2
Group:		Graphical desktop/Other
URL:		https://github.com/quantum-os/files-app
# git clone https://github.com/papyros/files-app.git
# git archive --format=tar --prefix files-app-0.0.0-$(date +%Y%m%d)/ HEAD | xz -vf > files-app-0.0.0-$(date +%Y%m%d).tar.xz
Source0:	%{name}-%{version}-%{snap}.tar.xz
BuildRequires:	qt5-devel
BuildRequires:	pkgconfig(Qt5QuickTest)
BuildRequires:	pkgconfig(Qt5Qml)
BuildRequires:	cmake(KF5Declarative)
BuildRequires:	qml-material
BuildRequires:	pkgconfig(taglib)

%description
The file manager for Papyros

%prep
%setup -qn %{name}-%{version}-%{snap}

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
