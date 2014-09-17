# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.27
# 

Name:       kservice

# >> macros
# << macros

# >> bcond_with
# << bcond_with

# >> bcond_without
# << bcond_without

Summary:    KDE Frameworks 5 Tier 3 solution for working with .desktop files
Version:    5.2.0
Release:    1
Group:      System/Base
License:    GPLv2+
URL:        http://www.kde.org
Source0:    %{name}-%{version}.tar.xz
Source100:  kservice.yaml
Source101:  kservice-rpmlintrc
Requires:   kf5-filesystem
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Xml)
BuildRequires:  pkgconfig(Qt5Network)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Widgets)
BuildRequires:  pkgconfig(Qt5Concurrent)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  kf5-rpm-macros
BuildRequires:  extra-cmake-modules
BuildRequires:  kconfig-devel
BuildRequires:  kconfig-gui
BuildRequires:  kcoreaddons-devel
BuildRequires:  kcrash-devel
BuildRequires:  kdbusaddons-devel
BuildRequires:  kwindowsystem-devel
BuildRequires:  ki18n-devel
BuildRequires:  kdoctools-devel

%description
KDE Frameworks 5 Tier 3 solution for working with .desktop files.


%package devel
Summary:    Development files for %{name}
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}
Requires:   kconfig-devel
Requires:   kconfig-gui
Requires:   kcoreaddons-devel
Requires:   kcrash-devel
Requires:   kdbusaddons-devel
Requires:   kwindowsystem-devel
Requires:   ki18n-devel
Requires:   kdoctools-devel

%description devel
The %{name}-devel package contains the files necessary to develop applications
that use %{name}.


%prep
%setup -q -n %{name}-%{version}/upstream

# >> setup
# << setup

%build
# >> build pre
%kf5_make
# << build pre



# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
%kf5_make_install
# << install pre

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%doc COPYING COPYING.LIB README.md
%{_kf5_bindir}/kbuildsycoca5
%{_kf5_libdir}/libKF5Service.so.*
%{_kf5_configdir}/menus/applications.menu
%{_kf5_servicetypesdir}/*.desktop
%{_mandir}/man8/*
# >> files
# << files

%files devel
%defattr(-,root,root,-)
%{_kf5_includedir}/kservice_version.h
%{_kf5_includedir}/KService
%{_kf5_bindir}/desktoptojson
%{_kf5_libdir}/libKF5Service.so
%{_kf5_cmakedir}/KF5Service
%{_kf5_mkspecsdir}/qt_KService.pri
# >> files devel
# << files devel
