
%define		_state		snapshots
%define		_ver		3.1.94
%define		_snap		031204

Summary:	Toys for KDE
Summary(ja):	KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ - ¤ª¤â¤Á¤ã
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - Àå³­°Å¸®
Summary(pl):	Zabawki dla KDE
Summary(zh_CN):	KDEÓéÀÖ³ÌÐò
Name:		kdetoys
Version:	%{_ver}.%{_snap}
Release:	1
Epoch:		9
License:	GPL
Group:		X11/Applications/Graphics
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:	http://ep09.pld-linux.org/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	6493f65454ca37b8d7ac8dd218ebef59
Patch0:		%{name}-fix-amor.patch
Patch1:		%{name}-screensavers.patch
Icon:		kde-icon.xpm
BuildRequires:	ed
BuildRequires:	gettext-devel
BuildRequires:	kdebase-devel >= 9:%{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	zlib-devel
Obsoletes:	amor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The kdetoys package includes various toys for the K Desktop
Environment (KDE), including:
- kmoon - displays the phases of the moon,
- kworldwatch - graphically displays the Earth's day and night
- kodo - a mouse odometer which shows how far your mouse has traveled.

%description -l ja
KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ÍÑ¤Î¤ª¤â¤Á¤ã °Ê²¼¤Î¤è¤¦¤Ê¥Ñ¥Ã¥±¡¼¥¸¤¬Æþ¤Ã¤Æ¤¤¤Þ¤¹¡£

- kmoon - ·îÎðÉ½¼¨¥Ä¡¼¥ë
- kworldwatch - À¤³¦»þ·×
- kodo - ¥Ç¥¹¥¯¥È¥Ã¥×¤ÎÂç¤­¤µ¤òÂ¬¤í¤¦

%description -l pl
Pakiet kdetoys zawiera ró¿ne zabawki dla KDE, w tym:
- kmoon - wy¶wietlaj±cy fazy ksiê¿yca,
- kworldwatch - pokazuj±cy graficznie dzieñ i noc,
- kodo - licznik pokazuj±cy jak d³ug± drogê pokona³a mysz.

%package devel
Summary:	Header files for kdetoys
Summary(pl):	Pliki nag³ówkowe dla kdetoys
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= 9:%{version}

%description devel
Header files for kdetoys.

%description devel -l pl
Pliki nag³ówkowe dla kdetoys.

%package amor
Summary:	Comic figures above your windows
Summary(pl):	Postacie z komiksów nad okienkami
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description amor
Amusing Misuse Of Resources put's comic figures above your windows.

%description amor -l pl
Zabawne, acz niew³a¶ciwe wykorzystanie zasobów, aby umie¶ciæ postacie
z komiksów nad okienkami.

%package eyes
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}
Obsoletes:	%{name}-amor < 9:3.1.93.031105-2

%description eyes
TODO.

%description eyes -l pl
TODO.

%package fifteen
Summary:	Order 15 pieces in a 4x4 square by moving them
Summary(pl):	Uporz±dkuj 15 elementów przesuwaj±c sie w polu 4x4
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}

%description fifteen
Order 15 pieces in a 4x4 square by moving them.

%description fifteen -l pl
Uporz±dkuj 15 elementów przesuwaj±c sie w polu 4x4.

%package kmoon
Summary:	System tray applet showing the moon phase
Summary(pl):	Applet dla zasobnika systemowego pokazuj±cy fazê ksiê¿yca
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}

%description kmoon
system tray applet showing the moon phase.

%description kmoon -l pl
Applet dla zasobnika systemowego pokazuj±cy fazê ksiê¿yca.

%package kodo
Summary:	Mouse movement meter
Summary(pl):	Licznik dystansu pokonanego przez mysz
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}

%description kodo
Mouse movement meter.

%description kodo -l pl
Licznik dystansu pokonanego przez mysz.

%package kteatime
Summary:	System tray applet that makes sure your tea doesn't get too strong
Summary(pl):	Applet zasobika systemowego przypominaj±cy o herbacie
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}

%description kteatime
System tray applet that makes sure your tea doesn't get too strong.

%description kteatime -l pl
Applet zasobika systemowego, który upewnia siê, ¿e twoja herbata nie
stanie siê zbyt mocna.

%package ktux
Summary:	Tux-in-a-Spaceship screen saver
Summary(pl):	Wygaszacz ekranu Tux-w-statku-kosmicznym
Group:		X11/Applications
Requires:	kdebase-screensavers >= 9:%{version}

%description ktux
Tux-in-a-Spaceship screen saver.

%description ktux -l pl
Wygaszacz ekranu Tux-w-statku-kosmicznym.

%package kweather
Summary:	Kicker applet that will display the current weather outside
Summary(pl):	Applet kickera wy¶wietlaj±cy pogodê na zewn±trz
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}
Obsoletes:	kdetoys

%description kweather
Kicker applet that will display the current weather outside.

%description kweather -l pl
Applet kickera wy¶wietlaj±cy pogodê na zewn±trz.

%package kworldclock
Summary:	Daylight area on the world globe
Summary(pl):	D³ugo¶æ dnia na ca³ym ¶wiecie
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}
Requires:	konqueror >= %{version}

%description kworldclock
Application and kicker applet showing daylight area on the world
globe.

%description kworldclock -l pl
Aplikacja i applet kickera pokazuj±ca d³ugo¶æ dnia na ca³ym ¶wiecie.

%package ww
Summary:	World Wide Watch applet
Summary(pl):	Applet World Wide Watch
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}

%description ww
World Wide Watch applet.

%description ww -l pl
Applet World Wide Watch.

%prep
%setup -q -n %{name}-%{_snap}
#%patch0 -p1
%patch1 -p1

%build
for f in `find . -name \*.desktop | xargs grep -l '\[nb\]'` ; do
	echo -e ',s/\[nb\]=/[no]=/\n,w' | ed $f 2>/dev/null
done

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang amor			--with-kde
%find_lang kmoon		--with-kde
%find_lang kodo			--with-kde
%find_lang kteatime		--with-kde
%find_lang kweather		--with-kde
%find_lang kworldclock		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%{_includedir}/*

%files amor -f amor.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/amor
%{_datadir}/apps/amor
%{_desktopdir}/kde/amor.desktop
%{_iconsdir}/*/*/*/amor*

%files eyes
%defattr(644,root,root,755)
%{_libdir}/kde3/eyes_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/eyes_panelapplet.so
%{_datadir}/apps/kicker/applets/eyesapplet.desktop

%files fifteen
%defattr(644,root,root,755)
%{_libdir}/kde3/fifteen_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/fifteen_panelapplet.so
%{_datadir}/apps/kicker/applets/kfifteenapplet.desktop

%files kmoon -f kmoon.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kmoon
%{_datadir}/apps/kmoon
%{_desktopdir}/kde/kmoon.desktop
%{_iconsdir}/*/*/*/kmoon*

%files kodo -f kodo.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kodo
%{_datadir}/apps/kodo
%{_desktopdir}/kde/kodo.desktop
%{_iconsdir}/*/*/*/kodo*

%files kteatime -f kteatime.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kteatime
%{_datadir}/apps/kteatime
%{_desktopdir}/kde/kteatime.desktop
%{_iconsdir}/*/*/*/kteatime*

%files ktux
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/ktux
%{_datadir}/apps/ktux
%{_datadir}/apps/kscreensaver/ktux.desktop

%files kweather -f kweather.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kweatherreport
%attr(0755,root,root) %{_bindir}/kweatherservice
%{_libdir}/libkdeinit_kweatherreport.la
%attr(0755,root,root) %{_libdir}/libkdeinit_kweatherreport.so
%{_libdir}/kde3/kcm_weather.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_weather.so
%{_libdir}/kde3/kcm_weatherservice.la
%attr(0755,root,root) %{_libdir}/kde3/kcm_weatherservice.so
%{_libdir}/kde3/kweatherreport.la
%attr(0755,root,root) %{_libdir}/kde3/kweatherreport.so
%{_libdir}/kde3/weather_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/weather_panelapplet.so
%{_datadir}/apps/kicker/applets/kweather.desktop
%{_datadir}/apps/kweatherservice/stations.dat
%{_datadir}/services/kcmweather.desktop
%{_datadir}/services/kcmweatherservice.desktop
%{_datadir}/services/kweatherservice.desktop
%{_datadir}/apps/kweather
%{_iconsdir}/*/*/apps/kweather.png

%files kworldclock -f kworldclock.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kworldclock
%{_datadir}/apps/kworldclock
%{_datadir}/apps/kdesktop/programs/kdeworld.desktop
%{_desktopdir}/kde/kworldclock.desktop
%{_iconsdir}/*/*/*/kworldclock*

%files ww
%defattr(644,root,root,755)
%{_libdir}/kde3/ww_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/ww_panelapplet.so
%{_datadir}/apps/kicker/applets/kwwapplet.desktop
