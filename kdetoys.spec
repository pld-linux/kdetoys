
%define		_state		stable
%define		_ver		3.2.0	
##%define		_snap		040110
#
# Conditional build:
%bcond_without	i18n	# don't build i18n subpackages
#
Summary:	Toys for KDE
Summary(ja):	KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ - ¤ª¤â¤Á¤ã
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - Àå³­°Å¸®
Summary(pl):	Zabawki dla KDE
Summary(zh_CN):	KDEÓéÀÖ³ÌÐò
Name:		kdetoys
Version:	%{_ver}
Release:	4
Epoch:		9
License:	GPL
Group:		X11/Applications/Graphics
####Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
# Source0-md5:	b9fdd2b51a25501322e3dd3301760a41
%if %{with i18n}
Source1:	http://ep09.pld-linux.org/~djurban/kde/i18n/kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	fa44500a6aa6417b45433ef54ac0fd64
%endif
Patch0:		%{name}-3.2branch.diff
Patch1:		%{name}-fix-amor.patch
Patch2:		%{name}-screensavers.patch
Icon:		kde-icon.xpm
URL:		http://www.kde.org/
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
Summary:	An xeyes KDE clone
Summary(pl):	Klon xeyes dla KDE
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}
Obsoletes:	%{name}-amor < 9:3.1.93.031105-2

%description eyes
An xeyes KDE clone.

%description eyes -l pl
Klon xeyes dla KDE.

%package fifteen
Summary:	A game: order 15 pieces in a 4x4 square by moving them
Summary(pl):	Gra polegaj±ca na uporz±dkowaniu 15 elementów przesuwaj±c siê w polu 4x4
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}

%description fifteen
Game: Order 15 pieces in a 4x4 square by moving them.

%description fifteen -l pl
Gra polegaj±ca na uporz±dkowaniu 15 elementów przesuwaj±c siê w polu
4x4.

%package kmoon
Summary:	System tray applet showing the moon phase
Summary(pl):	Aplet dla zasobnika systemowego pokazuj±cy fazê ksiê¿yca
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}

%description kmoon
system tray applet showing the moon phase.

%description kmoon -l pl
Aplet dla zasobnika systemowego pokazuj±cy fazê ksiê¿yca.

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
Summary(pl):	Aplet zasobnika systemowego przypominaj±cy o herbacie
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}

%description kteatime
System tray applet that makes sure your tea doesn't get too strong.

%description kteatime -l pl
Applet zasobnika systemowego pilnuj±cy ¿eby herbata nie sta³a siê zbyt
mocna.

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
Summary(pl):	Aplet kickera wy¶wietlaj±cy pogodê na zewn±trz
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}
Obsoletes:	kdetoys

%description kweather
Kicker applet that will display the current weather outside.

%description kweather -l pl
Aplet kickera wy¶wietlaj±cy pogodê na zewn±trz.

%package kworldclock
Summary:	Daylight area on the world globe
Summary(pl):	D³ugo¶æ dnia na ca³ym ¶wiecie
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}
Requires:	konqueror >= 9:%{version}

%description kworldclock
Application and kicker applet showing daylight area on the world
globe.

%description kworldclock -l pl
Aplikacja i aplet kickera pokazuj±ca d³ugo¶æ dnia na ca³ym ¶wiecie.

%package ww
Summary:	World Wide Watch applet
Summary(pl):	Aplet World Wide Watch
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}

%description ww
World Wide Watch applet.

%description ww -l pl
Aplet World Wide Watch.

%package i18n
Summary:	Common internationalization and localization files for kdetoys
Summary(pl):	Wspó³dzielone pliki umiêdzynarodawiaj±ce dla kdetoys
Group:		X11/Applications
Requires:	kdelibs-i18n >= 9:%{version}

%description i18n
Common internationalization and localization files for kdetoys.

%description i18n -l pl
Wspó³dzielone pliki umiêdzynarodawiaj±ce dla kdetoys.

%package amor-i18n
Summary:	Internationalization and localization files for amor
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla amora
Group:		X11/Applications
Requires:	%{name}-amor = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description amor-i18n
Internationalization and localization files for amor.

%description amor-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla amora.

%package kmoon-i18n
Summary:	Internationalization and localization files for kmoon
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kmoon
Group:		X11/Applications
Requires:	%{name}-kmoon = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kicker-i18n >= 9:%{version}

%description kmoon-i18n
Internationalization and localization files for kmoon.

%description kmoon-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kmoon.

%package kodo-i18n
Summary:	Internationalization and localization files for kodo
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kodo
Group:		X11/Applications
Requires:	%{name}-kodo = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kodo-i18n
Internationalization and localization files for kodo.

%description kodo-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kodo.

%package kteatime-i18n
Summary:	Internationalization and localization files for kteatime
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kteatime
Group:		X11/Applications
Requires:	%{name}-kteatime = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kicker-i18n >= 9:%{version}

%description kteatime-i18n
Internationalization and localization files for kteatime.

%description kteatime-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kteatime.

%package kweather-i18n
Summary:	Internationalization and localization files for kweather
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kweather
Group:		X11/Applications
Requires:	%{name}-kweather = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kicker-i18n >= 9:%{version}

%description kweather-i18n
Internationalization and localization files for kweather.

%description kweather-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kweather.

%package kworldclock-i18n
Summary:	Internationalization and localization files for kworldclock
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla kworldclocka
Group:		X11/Applications
Requires:	%{name}-kworldclock = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kicker-i18n >= 9:%{version}
Requires:	konqueror-i18n >= 9:%{version}

%description kworldclock-i18n
Internationalization and localization files for kworldclock.

%description kworldclock-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla kworldclocka.

%package ktux-i18n
Summary:	Internationalization and localization files for ktux
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla ktuksa
Group:		X11/Applications
Requires:	%{name}-ktux = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-screensavers-i18n >= 9:%{version}

%description ktux-i18n
Internationalization and localization files for ktux.

%description ktux-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla ktuksa.

%package fifteen-i18n
Summary:	Internationalization and localization files for fifteen
Summary(pl):	Pliki umiêdzynarodawiaj±ce dla fifteen
Group:		X11/Applications
Requires:	%{name}-fifteen = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kicker-i18n >= 9:%{version}

%description fifteen-i18n
Internationalization and localization files for fifteen.

%description fifteen-i18n -l pl
Pliki umiêdzynarodawiaj±ce dla fifteen.

%prep
%setup -q
%patch0 -p1
%patch2 -p1

%build
cp /usr/share/automake/config.sub admin
%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir} \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%if %{with i18n}
if [ -f "%{SOURCE1}" ] ; then
	bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
	for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
		if [ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] ; then
			rm -f $f
		fi
	done
else
	echo "No i18n sources found and building --with i18n. FIXIT!"
	exit 1
fi
%endif

%find_lang amor			--with-kde
%find_lang kmoon		--with-kde
%find_lang kodo			--with-kde
%find_lang kteatime		--with-kde
%find_lang kweather		--with-kde
%find_lang kworldclock		--with-kde

files="amor \
kmoon \
kodo \
kteatime \
kweather \
kworldclock"

%if %{with i18n}
%find_lang kfifteenapplet	--with-kde
%find_lang ktux			--with-kde
%find_lang desktop_kdetoys	--with-kde
%endif

for i in $files; do
	> ${i}_en.lang
	echo "%defattr(644,root,root,755)" > ${i}_en.lang
	grep en\/ ${i}.lang|grep -v apidocs >> ${i}_en.lang
	grep -v apidocs $i.lang|grep -v en\/ > ${i}.lang.1
	mv ${i}.lang.1 ${i}.lang
done

durne=`ls -1 *.lang|grep -v _en`

for i in $durne; 
do
	echo $i >> control
	grep -v en\/ $i|grep -v apidocs >> ${i}.1
	if [ -f ${i}.1 ] ; then
		mv ${i}.1 ${i}
	fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with i18n}
%files i18n -f desktop_kdetoys.lang
%files amor-i18n -f amor.lang
%files kmoon-i18n -f kmoon.lang
%files kodo-i18n -f kodo.lang
%files kteatime-i18n -f kteatime.lang
%files kweather-i18n -f kweather.lang
%files kworldclock-i18n -f kworldclock.lang
%files fifteen-i18n -f kfifteenapplet.lang
%files ktux-i18n -f ktux.lang
%endif

%files devel
%defattr(644,root,root,755)
%{_includedir}/*.h

%files amor -f amor_en.lang
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

%files kmoon -f kmoon_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmoon
%{_datadir}/apps/kmoon
%{_desktopdir}/kde/kmoon.desktop
%{_iconsdir}/*/*/*/kmoon*
%{_mandir}/man1/kmoon.1*

%files kodo -f kodo_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kodo
%{_datadir}/apps/kodo
%{_desktopdir}/kde/kodo.desktop
%{_iconsdir}/*/*/*/kodo*
%{_mandir}/man1/kodo.1*

%files kteatime -f kteatime_en.lang
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

%files kweather -f kweather_en.lang
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
%{_datadir}/apps/kweatherservice/stations.dat
%{_datadir}/services/kcmweather.desktop
%{_datadir}/services/kcmweatherservice.desktop
%{_datadir}/services/kweatherservice.desktop
%{_datadir}/apps/kweather
%{_iconsdir}/*/*/apps/kweather.png
%{_mandir}/man1/kweatherreport.1*
%{_mandir}/man1/kweatherservice.1*

%files kworldclock -f kworldclock_en.lang
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
