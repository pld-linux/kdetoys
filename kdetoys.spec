%define		_ver		3.0.2
#define		_sub_ver
%define		_rel		0.1

%{?_sub_ver:	%define	_version	%{_ver}%{_sub_ver}}
%{!?_sub_ver:	%define	_version	%{_ver}}
%{?_sub_ver:	%define	_release	0.%{_sub_ver}.%{_rel}}
%{!?_sub_ver:	%define	_release	%{_rel}}
%{!?_sub_ver:	%define	_ftpdir	stable}
%{?_sub_ver:	%define	_ftpdir	unstable/kde-%{version}%{_sub_ver}}

Summary:	Toys for KDE
Summary(pl):	Zabawki dla KDE
Name:		kdetoys
Version:	%{_version}
Release:	%{_release}
Epoch:		8
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_ftpdir}/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Icon:		kde-icon.xpm
BuildRequires:	kdelibs-devel = %{version}
BuildRequires:	gettext-devel
BuildRequires:	zlib-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		/sbin/ldconfig

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML
%define		_mandir		%{_prefix}/man

%description
The kdetoys package includes various toys for the K Desktop
Environment (KDE), including: kmoon, which displays the phases of the
moon; kworldwatch, which graphically displays the Earth's day and
night; and kodo, a mouse odometer which shows how far your mouse has
traveled.

%description -l pl
Pakiet kdetoys zawiera ró¿ne zabawki dla KDE, w tym: kmoon
(wy¶wietlaj±cy fazy ksiê¿yca), kworldwatch (pokazuj±cy graficznie
dzieñ i noc), oraz kodo (licznik pokazuj±cy jak d³ug± drogê pokona³a
mysz).

%package	amor
Summary:	Comic figures above your windows
Summary(pl):	Postacie z komiksów nad okienkami
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description amor
Amusing Misuse Of Resources put's comic figures above your windows.

%description amor -l pl
Zabawne, acz niew³a¶ciwe wykorzystanie zasobów, aby umie¶ciæ postacie z
komiksów nad okienkami.

%package	fifteen
Summary:	Order 15 pieces in a 4x4 square by moving them
Summary(pl):	Uporz±dkuj 15 elementów przesuwaj±c sie w polu 4x4
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description fifteen
Order 15 pieces in a 4x4 square by moving them.

%description fifteen -l pl
Uporz±dkuj 15 elementów przesuwaj±c sie w polu 4x4.

%package kaphorism
Summary:	Displays aphorisms
Summary(pl):	Wy¶wietlanie foryzmy
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kaphorism
Displays aphorisms.

%description kaphorism -l pl
Wy¶wietlanie foryzmy.

%package kmoon
Summary:	System tray applet showing the moon phase
Summary(pl):	Applet dla zasobnika systemowego pokazuj±cy fazê ksiê¿yca
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kmoon
system tray applet showing the moon phase.

%description kmoon -l pl
Applet dla zasobnika systemowego pokazuj±cy fazê ksiê¿yca.

%package kodo
Summary:	Mouse movement meter.
Summary(pl):	Licznik dystansu pokonanego przez mysz.
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kodo
Mouse movement meter.

%description kodo -l pl
Licznik dystansu pokonanego przez mysz.

%package kteatime
Summary:	System tray applet that makes sure your tea doesn't get too strong
Summary(pl):	Applet zasobika systemowego przypominaj±cy o herbacie.
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kteatime
System tray applet that makes sure your tea doesn't get too strong.

%description kteatime -l pl
Applet zasobika systemowego, który upewnia siê, ¿e twoja herbata nie stanie siê
zbyt mocna..

%package ktux
Summary:	Tux-in-a-Spaceship screen saver
Summary(pl):	Wygaszacz ekranu Tux-w-statku-kosmicznym
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description ktux
Tux-in-a-Spaceship screen saver.

%description ktux -l pl
Wygaszacz ekranu Tux-w-statku-kosmicznym.

%package	kweather
Summary:	Kicker applet that will display the current weather outside
Summary(pl):	Applet kickera wy¶wietlaj±cy pogodê na zewn±trz
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kweather
Kicker applet that will display the current weather outside.

%description kweather -l pl
Applet kickera wy¶wietlaj±cy pogodê na zewn±trz.

%package kworldclock
Summary:	Daylight area on the world globe
Summary(pl):	D³ugo¶æ dnia na ca³ym ¶wiecie
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kworldclock
Application and kicker applet showing daylight area on the world globe.

%description kworldclock -l pl
Aplikacja i applet kickera pokazuj±ca d³ugo¶æ dnia na ca³ym ¶wiecie.

%package	ww
Summary:	World Wide Watch applet
Summary(pl):	Applet World Wide Watch
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description ww
World Wide Watch applet.

%description ww -l pl
Applet World Wide Watch.

%package devel
Summary:	Header files for kdetoys
Summary(pl):	Pliki nag³ówkowe dla kdetoys
Group:		X11/Developement
Requires:	kdelibs = %{version}

%description devel
Header files for kdetoys.

%description devel -l pl
Pliki nag³ówkowe dla kdetoys.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
        CPPFLAGS="`pkg-config libpng12 --cflags`"
fi
CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_applnkdir}/{Toys,Amusements}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%find_lang amor --with-kde
%find_lang kmoon --with-kde
%find_lang kodo --with-kde
%find_lang kteatime --with-kde
%find_lang kweather --with-kde
%find_lang kworldclock --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)

%files amor -f amor.lang
%defattr(644,root,root,755)
%{_bindir}/amor
%{_libdir}/kde3/eyes_*.la
%{_libdir}/kde3/eyes_*.so.*.*.*
%{_datadir}/apps/amor
%{_datadir}/apps/kicker/applets/eyesapplet.desktop
%{_applnkdir}/Amusements/amor.desktop
%{_pixmapsdir}/*/*/*/amor*

%files fifteen
%defattr(644,root,root,755)
%{_libdir}/kde3/fifteen_*.la
%{_libdir}/kde3/fifteen_*.so.*.*.*
%{_datadir}/apps/kicker/applets/kfifteenapplet.desktop

%files kaphorism
%defattr(644,root,root,755)
%{_bindir}/kaphorism
%{_datadir}/apps/kaphorism
%{_applnkdir}/Amusements/kaphorism.desktop
%{_pixmapsdir}/*/*/*/kaphorism*

%files kmoon -f kmoon.lang
%defattr(644,root,root,755)
%{_bindir}/kmoon
%{_datadir}/apps/kmoon
%{_applnkdir}/Amusements/kmoon.desktop
%{_pixmapsdir}/*/*/*/kmoon*

%files kodo -f kodo.lang
%defattr(644,root,root,755)
%{_bindir}/kodo
%{_datadir}/apps/kodo
%{_applnkdir}/Amusements/kodo.desktop
%{_pixmapsdir}/*/*/*/kodo*

%files kteatime -f kteatime.lang
%defattr(644,root,root,755)
%{_bindir}/kteatime
%{_applnkdir}/Amusements/kteatime.desktop
%{_pixmapsdir}/*/*/*/kteatime*

%files ktux
%defattr(644,root,root,755)
%{_bindir}/ktux
%{_datadir}/apps/ktux
%{_applnkdir}/System/ScreenSavers/ktux.desktop
%{_pixmapsdir}/*/*/*/ktux*

%files kweather -f kweather.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/weather_*.la
%{_libdir}/kde3/weather_*.so.*.*.*
%{_datadir}/apps/kicker/applets/kweather.desktop
%{_datadir}/apps/kweather

%files kworldclock -f kworldclock.lang
%defattr(644,root,root,755)
%{_bindir}/kworldclock
%{_datadir}/apps/kworldclock
%{_datadir}/apps/kdesktop/programs/kdeworld.desktop
%{_applnkdir}/Amusements/kworldclock.desktop
%{_pixmapsdir}/*/*/*/kworldclock*

%files ww
%defattr(644,root,root,755)
%{_libdir}/kde3/ww_*.la
%{_libdir}/kde3/ww_*.so.*.*.*
%{_datadir}/apps/kicker/applets/kwwapplet.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/kde3/fifteen_*.so
%{_libdir}/kde3/eyes_*.so
%{_libdir}/kde3/weather_*.so
%{_libdir}/kde3/ww_*.so
