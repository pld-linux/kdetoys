Summary:	Toys for KDE
Summary(ja):	KDEデスクトップ環境 - おもちゃ
Summary(ko):	K 汽什滴転 発井 - 舌貝暗軒
Summary(pl):	Zabawki dla KDE
Summary(zh_CN):	KDE嚔赤殻會
Name:		kdetoys
Version:	3.0.4
Release:	1
Epoch:		8
License:	GPL
Group:		X11/Applications/Graphics
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Patch0:		%{name}-applets-no-version.patch
Patch1:		%{name}-fix-amor.patch
Patch2:		%{name}-fix-kmoon-mem-leak.patch
Icon:		kde-icon.xpm
BuildRequires:	gettext-devel
BuildRequires:	kdelibs-devel = %{version}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
BuildRequires:	libtiff-devel
BuildRequires:	zlib-devel
Prereq:		/sbin/ldconfig
Obsoletes:	amor
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML
%define		_mandir		%{_prefix}/man

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
Requires:	kdelibs = %{version}

%description amor
Amusing Misuse Of Resources put's comic figures above your windows.

%description amor -l pl
Zabawne, acz niew�a�ciwe wykorzystanie zasob�w, aby umie�ci� postacie
z komiks�w nad okienkami.

%package	fifteen
Summary:	Order 15 pieces in a 4x4 square by moving them
Summary(pl):	Uporz�dkuj 15 element�w przesuwaj�c sie w polu 4x4
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description fifteen
Order 15 pieces in a 4x4 square by moving them.

%description fifteen -l pl
Uporz�dkuj 15 element�w przesuwaj�c sie w polu 4x4.

%package kaphorism
Summary:	Displays aphorisms
Summary(pl):	Wy�wietlanie foryzmy
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kaphorism
Displays aphorisms.

%description kaphorism -l pl
Wy�wietlanie foryzmy.

%package kmoon
Summary:	System tray applet showing the moon phase
Summary(pl):	Applet dla zasobnika systemowego pokazuj�cy faz� ksi蠖yca
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kmoon
system tray applet showing the moon phase.

%description kmoon -l pl
Applet dla zasobnika systemowego pokazuj�cy faz� ksi蠖yca.

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
Summary(pl):	Applet zasobika systemowego przypominaj�cy o herbacie.
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kteatime
System tray applet that makes sure your tea doesn't get too strong.

%description kteatime -l pl
Applet zasobika systemowego, kt�ry upewnia si�, �e twoja herbata nie
stanie si� zbyt mocna..

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
Summary(pl):	Applet kickera wy�wietlaj�cy pogod� na zewn�trz
Group:		X11/Applications
Requires:	kdelibs = %{version}
Provides:	kweather
Obsoletes:	kweather

%description kweather
Kicker applet that will display the current weather outside.

%description kweather -l pl
Applet kickera wy�wietlaj�cy pogod� na zewn�trz.

%package kworldclock
Summary:	Daylight area on the world globe
Summary(pl):	D�ugo倶 dnia na ca�ym �wiecie
Group:		X11/Applications
Requires:	kdelibs = %{version}

%description kworldclock
Application and kicker applet showing daylight area on the world
globe.

%description kworldclock -l pl
Aplikacja i applet kickera pokazuj�ca d�ugo倶 dnia na ca�ym �wiecie.

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
Summary(pl):	Pliki nag鞄wkowe dla kdetoys
Group:		X11/Development/Libraries
Requires:	kdelibs = %{version}

%description devel
Header files for kdetoys.

%description devel -l pl
Pliki nag鞄wkowe dla kdetoys.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags}"
%configure \
	--enable-final \
	--%{?debug:en}%{!?debug:dis}able-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_applnkdir}/{Toys,Amusements}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

%find_lang amor		--with-kde
%find_lang kaphorism	--with-kde
%find_lang kfifteenapplet --with-kde
%find_lang kmoon	--with-kde
%find_lang kodo		--with-kde
%find_lang kteatime	--with-kde
%find_lang ktux 	--with-kde
%find_lang kweather	--with-kde
%find_lang kworldclock	--with-kde

# propably should be in other packages - kde-i18n to fix:
%find_lang kfortune	--with-kde
%find_lang kscoreapplet	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)

%files amor -f amor.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/amor
%attr(0755,root,root) %{_libdir}/kde3/eyes_*
%{_datadir}/apps/amor
%{_datadir}/apps/kicker/applets/eyesapplet.desktop
%{_applnkdir}/Amusements/amor.desktop
%{_pixmapsdir}/*/*/*/amor*

%files fifteen -f kfifteenapplet.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_libdir}/kde3/fifteen_*
%{_datadir}/apps/kicker/applets/kfifteenapplet.desktop

%files kaphorism -f kaphorism.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kaphorism
%{_datadir}/apps/kaphorism
%{_applnkdir}/Amusements/kaphorism.desktop
%{_pixmapsdir}/*/*/*/kaphorism*

%files kmoon -f kmoon.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kmoon
%{_datadir}/apps/kmoon
%{_applnkdir}/Amusements/kmoon.desktop
%{_pixmapsdir}/*/*/*/kmoon*

%files kodo -f kodo.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kodo
%{_datadir}/apps/kodo
%{_applnkdir}/Amusements/kodo.desktop
%{_pixmapsdir}/*/*/*/kodo*

%files kteatime -f kteatime.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kteatime
%{_applnkdir}/Amusements/kteatime.desktop
%{_pixmapsdir}/*/*/*/kteatime*

%files ktux -f ktux.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/ktux
%{_datadir}/apps/ktux
%{_applnkdir}/System/ScreenSavers/ktux.desktop
%{_pixmapsdir}/*/*/*/ktux*

%files kweather -f kweather.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_libdir}/kde3/weather_*
%{_datadir}/apps/kicker/applets/kweather.desktop
%{_datadir}/apps/kweather

%files kworldclock -f kworldclock.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %{_bindir}/kworldclock
%{_datadir}/apps/kworldclock
%{_datadir}/apps/kdesktop/programs/kdeworld.desktop
%{_applnkdir}/Amusements/kworldclock.desktop
%{_pixmapsdir}/*/*/*/kworldclock*

%files ww
%defattr(644,root,root,755)
%attr(0755,root,root) %{_libdir}/kde3/ww_*
%{_datadir}/apps/kicker/applets/kwwapplet.desktop

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
