%global kf5_version 5.107.0

Name: opt-kf5-kdbusaddons
Version: 5.107.0
Release: 1%{?dist}
Summary: KDE Frameworks 5 Tier 1 addon with various classes on top of QtDBus

License: LGPLv2+
URL:     https://invent.kde.org/frameworks/kdbusaddons

Source0: %{name}-%{version}.tar.bz2

%{?opt_kf5_default_filter}

BuildRequires: opt-extra-cmake-modules >= %{kf5_version}
BuildRequires: opt-kf5-rpm-macros >= %{kf5_version}
BuildRequires: opt-qt5-qtbase-devel
BuildRequires: opt-qt5-qttools-devel

%{?_opt_qt5:Requires: %{_opt_qt5}%{?_isa} = %{_opt_qt5_version}}

%description
KDBusAddons provides convenience classes on top of QtDBus, as well as an API to
create KDED modules.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       opt-qt5-qtbase-devel
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}/upstream -p1


%build
export QTDIR=%{_opt_qt5_prefix}
touch .git

mkdir -p build
pushd build

%_opt_cmake_kf5 ../
%make_build

popd

%install
pushd build
make DESTDIR=%{buildroot} install
popd

%find_lang_kf5 kdbusaddons5_qt


%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%doc README.md
%license LICENSES/*.txt
%{_opt_kf5_datadir}/qlogging-categories5/kdbusaddons*
%{_opt_kf5_bindir}/kquitapp5
%{_opt_kf5_libdir}/libKF5DBusAddons.so.*
%{_opt_kf5_datadir}/locale/

%files devel
%{_opt_kf5_includedir}/KF5/KDBusAddons/
%{_opt_kf5_libdir}/libKF5DBusAddons.so
%{_opt_kf5_libdir}/cmake/KF5DBusAddons/
%{_opt_kf5_archdatadir}/mkspecs/modules/qt_KDBusAddons.pri
