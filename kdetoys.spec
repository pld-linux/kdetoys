
%define		_state		stable
%define		_ver		3.1.4

Summary:	Toys for KDE
Summary(ja):	KDEデスクトップ環境 - おもちゃ
Summary(ko):	K 汽什滴転 発井 - 舌貝暗軒
Summary(pl):	Zabawki dla KDE
Summary(zh_CN):	KDE嚔赤殻會
Name:		kdetoys
Version:	%{_ver}
Release:	0.3
Epoch:		8
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	58c9a31f31564513414fbaf09fc13b29
# generated from kde-i18n
Source1:	ftp://blysk.ds.pg.gda.pl/linux/kde-i18n-package/%{version}/kde-i18n-%{name}-%{version}.tar.bz2
# Source1-md5:	0a4143c50c420724165373f911b69860
Patch0:		%{name}-fix-amor.patch
Patch1:		%{name}-screensavers.patch
Icon:		kde-icon.xpm
BuildRequires:	ed
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel = %{epoch}:%{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	zlib-devel
Obsoletes:	amor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_htmldir	/usr/share/doc/kde/HTML

%define		no_install_post_chrpath		1

%description
The kdetoys package includes various toys for the K Desktop
Environment (KDE), including:
- kmoon - displays the phases of the moon,
- kworldwatch - graphically displays the Earth's day and night
- kodo - a mouse odometer which shows how far your mouse has traveled.

%description -l ja
KDEデスクトップ環境用のおもちゃ 以下のようなパッケージが入っています。

- kmoon - 月齢表示ツール
- kworldwatch - 世界時計
- kodo - デスクトップの大きさを測ろう

%description -l pl
Pakiet kdetoys zawiera r鷽ne zabawki dla KDE, w tym:
- kmoon - wy�wietlaj�cy fazy ksi蠖yca,
- kworldwatch - pokazuj�cy graficznie dzie� i noc,
- kodo - licznik pokazuj�cy jak d�ug� drog� pokona�a mysz.

%package	amor
Summary:	Comic figures above your windows
Summary(pl):	Postacie z komiks�w nad okienkami
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}

%description amor
Amusing Misuse Of Resources put's comic figures above your windows.

%description amor -l pl
Zabawne, acz niew�a�ciwe wykorzystanie zasob�w, aby umie�ci� postacie
z komiks�w nad okienkami.

%package	fifteen
Summary:	Order 15 pieces in a 4x4 square by moving them
Summary(pl):	Uporz�dkuj 15 element�w przesuwaj�c sie w polu 4x4
Group:		X11/Applications
Requires:	kdebase-kicker >= %{version}

%description fifteen
Order 15 pieces in a 4x4 square by moving them.

%description fifteen -l pl
Uporz�dkuj 15 element�w przesuwaj�c sie w polu 4x4.

%package kaphorism
Summary:	Displays aphorisms
Summary(pl):	Wy�wietlanie aforyzm�w
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}

%description kaphorism
Displays aphorisms.

%description kaphorism -l pl
Wy�wietlanie aforyzm�w.

%package kmoon
Summary:	System tray applet showing the moon phase
Summary(pl):	Applet dla zasobnika systemowego pokazuj�cy faz� ksi蠖yca
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}

%description kmoon
system tray applet showing the moon phase.

%description kmoon -l pl
Applet dla zasobnika systemowego pokazuj�cy faz� ksi蠖yca.

%package kodo
Summary:	Mouse movement meter
Summary(pl):	Licznik dystansu pokonanego przez mysz
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}

%description kodo
Mouse movement meter.

%description kodo -l pl
Licznik dystansu pokonanego przez mysz.

%package kteatime
Summary:	System tray applet that makes sure your tea doesn't get too strong
Summary(pl):	Applet zasobika systemowego przypominaj�cy o herbacie
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}

%description kteatime
System tray applet that makes sure your tea doesn't get too strong.

%description kteatime -l pl
Applet zasobika systemowego, kt�ry upewnia si�, �e twoja herbata nie
stanie si� zbyt mocna.

%package ktux
Summary:	Tux-in-a-Spaceship screen saver
Summary(pl):	Wygaszacz ekranu Tux-w-statku-kosmicznym
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}

%description ktux
Tux-in-a-Spaceship screen saver.

%description ktux -l pl
Wygaszacz ekranu Tux-w-statku-kosmicznym.

%package	kweather
Summary:	Kicker applet that will display the current weather outside
Summary(pl):	Applet kickera wy�wietlaj�cy pogod� na zewn�trz
Group:		X11/Applications
Requires:	kdebase-kicker >= %{version}
Provides:	kweather
Obsoletes:	kweather
Obsoletes:	kdetoys

%description kweather
Kicker applet that will display the current weather outside.

%description kweather -l pl
Applet kickera wy�wietlaj�cy pogod� na zewn�trz.

%package kworldclock
Summary:	Daylight area on the world globe
Summary(pl):	D�ugo倶 dnia na ca�ym �wiecie
Group:		X11/Applications
Requires:	kdelibs >= 8:%{version}

%description kworldclock
Application and kicker applet showing daylight area on the world
globe.

%description kworldclock -l pl
Aplikacja i applet kickera pokazuj�ca d�ugo倶 dnia na ca�ym �wiecie.

%package	ww
Summary:	World Wide Watch applet
Summary(pl):	Applet World Wide Watch
Group:		X11/Applications
Requires:	kdebase-kicker >= %{version}


%description ww
World Wide Watch applet.

%description ww -l pl
Applet World Wide Watch.

%package devel
Summary:	Header files for kdetoys
Summary(pl):	Pliki nag鞄wkowe dla kdetoys
Group:		X11/Development/Libraries
Requires:	kdelibs >= 8:%{version}

%description devel
Header files for kdetoys.

%description devel -l pl
Pliki nag鞄wkowe dla kdetoys.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"

for plik in `find ./ -name *.desktop | grep -l '\[nb\]'` ; do
	echo $plik
	echo -e ',s/\[nb\]/[no]/\n,w' | ed $plik
done

%configure \
	--enable-final \
	--%{?debug:en}%{!?debug:dis}able-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_applnkdir}/{Toys,Amusements}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%find_lang	amor		--with-kde
%find_lang	kaphorism	--with-kde
%find_lang	kfifteenapplet 	--with-kde
%find_lang	kmoon		--with-kde
%find_lang	kodo		--with-kde
%find_lang	kteatime	--with-kde
%find_lang	ktux 		--with-kde
%find_lang	kweather	--with-kde
%find_lang	kworldclock	--with-kde
#%find_lang	keyesapplet	--with-kde

# propably should be in other packages - kde-i18n to fix:
#%find_lang	kscoreapplet	--with-kde

install debian/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%{_includedir}/*

%files amor -f amor.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/amor
%{_libdir}/kde3/eyes_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/eyes_panelapplet.so
%{_datadir}/apps/amor
%{_datadir}/apps/kicker/applets/eyesapplet.desktop
%{_applnkdir}/Amusements/amor.desktop
%{_pixmapsdir}/*/*/*/amor*
%{_mandir}/man1/amor.*

%files fifteen -f kfifteenapplet.lang
%defattr(644,root,root,755)
%{_libdir}/kde3/fifteen_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/fifteen_panelapplet.so
%{_datadir}/apps/kicker/applets/kfifteenapplet.desktop

%files kaphorism -f kaphorism.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kaphorism
%{_datadir}/apps/kaphorism
%{_applnkdir}/Amusements/kaphorism.desktop
%{_pixmapsdir}/*/*/*/kaphorism*
%{_mandir}/man1/kaphorism.*

%files kmoon -f kmoon.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kmoon
%{_datadir}/apps/kmoon
%{_applnkdir}/Amusements/kmoon.desktop
%{_pixmapsdir}/*/*/*/kmoon*
%{_mandir}/man1/kmoon.*

%files kodo -f kodo.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kodo
%{_datadir}/apps/kodo
%{_applnkdir}/Amusements/kodo.desktop
%{_pixmapsdir}/*/*/*/kodo*
%{_mandir}/man1/kodo.*

%files kteatime -f kteatime.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kteatime
%{_datadir}/apps/kteatime
%{_applnkdir}/Amusements/kteatime.desktop
%{_pixmapsdir}/*/*/*/kteatime*
%{_mandir}/man1/kteatime.*

%files ktux -f ktux.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/ktux
%{_datadir}/apps/ktux
%{_datadir}/apps/kscreensaver/ktux.desktop
%{_mandir}/man1/ktux.*

%files kweather -f kweather.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kweatherservice
%attr(0755,root,root) %{_bindir}/reportview
%{_libdir}/kde3/weather_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/weather_panelapplet.so
%{_datadir}/apps/kicker/applets/kweather.desktop
%{_datadir}/services/kweatherservice.desktop
%{_datadir}/apps/kweather
%{_mandir}/man1/kweatherservice.*
%{_mandir}/man1/reportview.*

%files kworldclock -f kworldclock.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kworldclock
%{_datadir}/apps/kworldclock
%{_datadir}/apps/kdesktop/programs/kdeworld.desktop
%{_applnkdir}/Amusements/kworldclock.desktop
%{_pixmapsdir}/*/*/*/kworldclock*
%{_mandir}/man1/kworldclock.*

%files ww
%defattr(644,root,root,755)
%{_libdir}/kde3/ww_panelapplet.la
%attr(0755,root,root) %{_libdir}/kde3/ww_panelapplet.so
%{_datadir}/apps/kicker/applets/kwwapplet.desktop
