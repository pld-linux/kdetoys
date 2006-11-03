
%define		_state		stable
%define		_minlibsevr	9:%{version}
%define		_minbaseevr	9:%{version}

Summary:	Toys for KDE
Summary(ja):	KDE¥Ç¥¹¥¯¥È¥Ã¥×´Ä¶­ - ¤ª¤â¤Á¤ã
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - Àå³­°Å¸®
Summary(pl):	Zabawki dla KDE
Summary(zh_CN):	KDEÓéÀÖ³ÌÐò
Name:		kdetoys
Version:	3.5.5
Release:	1
Epoch:		9
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	2b03fd068209cf324396b75334f39aba
#Patch100:	%{name}-branch.diff
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-screensavers.patch
Patch2:		kde-ac260-lt.patch
URL:		http://www.kde.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	kdebase-devel >= %{_minbaseevr}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	zlib-devel
BuildConflicts:	kdetoys-ww
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
AMOR is an acronym which stands for Amusing Misuse of Resources. It is
actually an animation which sits on top of your active window. In its
default configuration, AMOR takes the form of a yellow spot which
performs many tricks. AMOR also has many different themes which change
the appearance and behavior of the animation.

Since AMOR works with the KDE window manager KWin, the application
will only work from within KDE. It is possible that AMOR would work
from within another KDE-compliant window manager, but has not been
tested.

%description amor -l pl
AMOR to skrót od Amusing Misuse of Resources, czyli zabawne, acz
niew³a¶ciwe wykorzystanie zasobów. Jest to animacja umieszczona nad
aktywnym okienkiem. W domy¶lnej konfiguracji AMOR przyjmuje postaæ
¿ó³tej plamki wykonuj±cej ró¿ne tricki. AMOR ma tak¿e wiele ró¿nych
motywów zmieniaj±cych wygl±d i zachowanie animacji.

Poniewa¿ AMOR dzia³a z zarz±dc± okien KDE, bêdzie dzia³aæ tylko w KDE.
Mo¿liwe, ¿e AMOR dzia³a z niektórymi innymi zarz±dcami okien zgodnymi
z KDE, ale nie by³o to testowane.

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
A game which goal is to order 15 pieces in a 4x4 square by moving
them.

%description fifteen -l pl
Gra polegaj±ca na uporz±dkowaniu 15 elementów przesuwaj±c siê w polu
4x4.

%package kmoon
Summary:	System tray applet showing the moon phase
Summary(pl):	Aplet dla zasobnika systemowego pokazuj±cy fazê ksiê¿yca
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}

%description kmoon
System tray applet showing the current moon phase.

%description kmoon -l pl
Aplet dla zasobnika systemowego pokazuj±cy fazê ksiê¿yca.

%package kodo
Summary:	Mouse movement meter
Summary(pl):	Licznik dystansu pokonanego przez mysz
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}

%description kodo
Mouse movement and mileage meter.

%description kodo -l pl
Licznik dystansu pokonanego przez mysz.

%package kteatime
Summary:	System tray applet that makes sure your tea doesn't get too strong
Summary(pl):	Aplet zasobnika systemowego przypominaj±cy o herbacie
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}

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
Summary(pl):	Aplet kickera wy¶wietlaj±cy aktualn± pogodê na zewn±trz
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdetoys

%description kweather
kweather is an application that provides both a panel icon, allowing
you to watch the weather as reported by a local weather station, and
providing a weather service that can track multiple weather stations
and provide this information to other applications including
Konqueror's sidebar and Kontact's summary page.

%description kweather -l pl
kweather to aplikacja dostarczaj±ca ikonê panelu, umo¿liwiaj±c±
ogl±danie pogody og³aszanej przez lokaln± stacjê oraz dostarczaj±c±
serwis pogodowy potrafi±cy ¶ledziæ wiele stacji pogodowych, a tak¿e
dostarczaj±ca te informacje dla innych aplikacji, w³±cznie z paskiem
Konquerora oraz stron± podsumowuj±c± Kontacta.

%package kworldclock
Summary:	Daylight area on the world globe
Summary(pl):	D³ugo¶æ dnia na ca³ym ¶wiecie
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdetoys-ww

%description kworldclock
Application and kicker applet showing daylight area on the world
globe.

%description kworldclock -l pl
Aplikacja i aplet kickera pokazuj±ca d³ugo¶æ dnia na ca³ym ¶wiecie.

%prep
%setup -q
#%%patch100 -p1
%patch0 -p1
%patch1 -p1
%patch2 -p1

for f in `find . -name \*.desktop`; do
	if grep -q '\[ven\]' $f; then
		sed -i -e 's/\[ven\]/[ve]/' $f
	fi
done

%build
cp %{_datadir}/automake/config.sub admin

%{__make} -f admin/Makefile.common cvs

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?debug:--disable-rpath} \
	--disable-final \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-qt-libraries=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
rm -rf *.lang

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

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

%files kodo -f kodo.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kodo
%{_datadir}/apps/kodo
%{_desktopdir}/kde/kodo.desktop
%{_iconsdir}/*/*/*/kodo*

%files kteatime -f kteatime.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kteatime
%{_datadir}/apps/kteatime
%{_desktopdir}/kde/kteatime.desktop
%{_iconsdir}/*/*/*/kteatime*

%files ktux
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktux
%{_datadir}/apps/ktux
%{_datadir}/apps/kscreensaver/ktux.desktop
%{_iconsdir}/*/*/*/ktux.*

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

%files kworldclock -f kworldclock.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kworldclock
%{_datadir}/apps/kworldclock
%{_datadir}/apps/kdesktop/programs/kdeworld.desktop
%{_desktopdir}/kde/kworldclock.desktop
%{_iconsdir}/*/*/*/kworldclock*
%{_libdir}/kde3/ww_panelapplet.la
%attr(755,root,root) %{_libdir}/kde3/ww_panelapplet.so
%{_datadir}/apps/kicker/applets/kwwapplet.desktop
