
%define		_state		snapshots
%define		_ver		3.2.91	
%define		_snap		040704

%define		_minlibsevr	9:3.2.91.040629
%define		_minbaseevr	9:3.2.91.040629

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
Source0:	ftp://ftp.pld-linux.org/software/kde/%{name}-%{_snap}.tar.bz2
Patch0:		%{name}-screensavers.patch
URL:		http://www.kde.org/
BuildRequires:	ed
BuildRequires:	gettext-devel
BuildRequires:	kdebase-devel >= %{_minbaseevr}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040511
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
Requires:	kdelibs-devel >= %{_minlibsevr}

%description devel
Header files for kdetoys.

%description devel -l pl
Pliki nag³ówkowe dla kdetoys.

%package amor
Summary:	Comic figures above your windows
Summary(pl):	Postacie z komiksów nad okienkami
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description amor
Amusing Misuse Of Resources put's comic figures above your windows.

%description amor -l pl
Zabawne, acz niew³a¶ciwe wykorzystanie zasobów, aby umie¶ciæ postacie
z komiksów nad okienkami.

%package eyes
Summary:	An xeyes KDE clone
Summary(pl):	Klon xeyes dla KDE
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdetoys-amor < 9:3.1.93.031105-2

%description eyes
An xeyes KDE clone.

%description eyes -l pl
Klon xeyes dla KDE.

%package fifteen
Summary:	A game: order 15 pieces in a 4x4 square by moving them
Summary(pl):	Gra polegaj±ca na uporz±dkowaniu 15 elementów przesuwaj±c siê w polu 4x4
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}

%description fifteen
Game: Order 15 pieces in a 4x4 square by moving them.

%description fifteen -l pl
Gra polegaj±ca na uporz±dkowaniu 15 elementów przesuwaj±c siê w polu
4x4.

%package kmoon
Summary:	System tray applet showing the moon phase
Summary(pl):	Aplet dla zasobnika systemowego pokazuj±cy fazê ksiê¿yca
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}

%description kmoon
system tray applet showing the moon phase.

%description kmoon -l pl
Aplet dla zasobnika systemowego pokazuj±cy fazê ksiê¿yca.

%package kodo
Summary:	Mouse movement meter
Summary(pl):	Licznik dystansu pokonanego przez mysz
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description kodo
Mouse movement meter.

%description kodo -l pl
Licznik dystansu pokonanego przez mysz.

%package kteatime
Summary:	System tray applet that makes sure your tea doesn't get too strong
Summary(pl):	Aplet zasobnika systemowego przypominaj±cy o herbacie
Group:		X11/Applications
Requires:	kdebase-kicker >= %{_minbaseevr}

%description kteatime
System tray applet that makes sure your tea doesn't get too strong.

%description kteatime -l pl
Applet zasobnika systemowego pilnuj±cy ¿eby herbata nie sta³a siê zbyt
mocna.

%package ktux
Summary:	Tux-in-a-Spaceship screen saver
Summary(pl):	Wygaszacz ekranu Tux-w-statku-kosmicznym
Group:		X11/Applications
Requires:	kdebase-screensavers >= %{_minbaseevr}

%description ktux
Tux-in-a-Spaceship screen saver.

%description ktux -l pl
Wygaszacz ekranu Tux-w-statku-kosmicznym.

%package kweather
Summary:	Kicker applet that will display the current weather outside
Summary(pl):	Aplet kickera wy¶wietlaj±cy pogodê na zewn±trz
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdetoys

%description kweather
Kicker applet that will display the current weather outside.

%description kweather -l pl
Aplet kickera wy¶wietlaj±cy pogodê na zewn±trz.

%package kworldclock
Summary:	Daylight area on the world globe
Summary(pl):	D³ugo¶æ dnia na ca³ym ¶wiecie
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}

%description kworldclock
Application and kicker applet showing daylight area on the world
globe.

%description kworldclock -l pl
Aplikacja i aplet kickera pokazuj±ca d³ugo¶æ dnia na ca³ym ¶wiecie.

%package ww
Summary:	World Wide Watch applet
Summary(pl):	Aplet World Wide Watch
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}

%description ww
World Wide Watch applet.

%description ww -l pl
Aplet World Wide Watch.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1

echo "KDE_OPTIONS = nofinal" >> kmoon/Makefile.am

%build
cp /usr/share/automake/config.sub admin

export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir} \

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%find_lang amor		--with-kde
%find_lang kmoon	--with-kde
%find_lang kodo		--with-kde
%find_lang kteatime	--with-kde
%find_lang kweather	--with-kde
%find_lang kworldclock	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h

%files amor -f amor.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/amor
%{_datadir}/apps/amor
%{_desktopdir}/kde/amor.desktop
%{_iconsdir}/*/*/*/amor*
%{_mandir}/man1/amor.1*

%files eyes
%defattr(644,root,root,755)
%{_libdir}/kde3/eyes_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/eyes_panelapplet.so
%{_datadir}/apps/kicker/applets/eyesapplet.desktop

%files fifteen
%defattr(644,root,root,755)
%{_libdir}/kde3/fifteen_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/fifteen_panelapplet.so
%{_datadir}/apps/kicker/applets/kfifteenapplet.desktop

%files kmoon -f kmoon.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/kmoon_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/kmoon_panelapplet.so
%{_datadir}/apps/kicker/applets/kmoonapplet.desktop
%{_datadir}/apps/kmoon
%{_iconsdir}/*/*/*/kmoon*
%{_mandir}/man1/kmoon.1*

%files kodo -f kodo.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kodo
%{_datadir}/apps/kodo
%{_desktopdir}/kde/kodo.desktop
%{_iconsdir}/*/*/*/kodo*
%{_mandir}/man1/kodo.1*

%files kteatime -f kteatime.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kteatime
%{_datadir}/apps/kteatime
%{_desktopdir}/kde/kteatime.desktop
%{_iconsdir}/*/*/*/kteatime*
%{_mandir}/man1/kteatime.1*

%files ktux
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktux
%{_datadir}/apps/ktux
%{_datadir}/apps/kscreensaver/ktux.desktop
%{_mandir}/man1/ktux.1*

%files kweather -f kweather.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kweatherreport
%attr(755,root,root) %{_bindir}/kweatherservice
%{_libdir}/libkdeinit_kweatherreport.la
%attr(755,root,root) %{_libdir}/libkdeinit_kweatherreport.so
%{_libdir}/kde3/kcm_weather.la
%attr(755,root,root) %{_libdir}/kde3/kcm_weather.so
%{_libdir}/kde3/kcm_weatherservice.la
%attr(755,root,root) %{_libdir}/kde3/kcm_weatherservice.so
%{_libdir}/kde3/kweatherreport.la
%attr(755,root,root) %{_libdir}/kde3/kweatherreport.so
%{_libdir}/kde3/weather_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/weather_panelapplet.so
%{_datadir}/apps/kicker/applets/kweather.desktop
%{_datadir}/apps/kweatherservice
%{_datadir}/services/kcmweather.desktop
%{_datadir}/services/kcmweatherservice.desktop
%{_datadir}/services/kweatherservice.desktop
%{_datadir}/apps/kweather
%{_iconsdir}/*/*/apps/kweather.png
%{_mandir}/man1/kweatherreport.1*
%{_mandir}/man1/kweatherservice.1*

%files kworldclock -f kworldclock.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kworldclock
%{_datadir}/apps/kworldclock
%{_datadir}/apps/kdesktop/programs/kdeworld.desktop
%{_desktopdir}/kde/kworldclock.desktop
%{_iconsdir}/*/*/*/kworldclock*
%{_mandir}/man1/kworldclock.1*

%files ww
%defattr(644,root,root,755)
%{_libdir}/kde3/ww_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/ww_panelapplet.so
%{_datadir}/apps/kicker/applets/kwwapplet.desktop
