Summary:	Toys for KDE
Summary(pl):	Zabawki dla KDE
Name:		kdetoys
Version:	2.2
Release:	5
Epoch:		7
License:	GPL
Group:		X11/Applications/Graphics
Group(de):	X11/Applikationen/Grafik
Group(pl):	X11/Aplikacje/Grafika
Group(pt):	X11/Aplicações/Gráficos
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
Patch0:		%{name}-2.2-kworldclock.patch
Patch1:		%{name}-2.2-cvsfixes.patch
Icon:		kde-icon.xpm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Prereq:		/sbin/ldconfig
BuildRequires:	kdelibs-devel >= 2.2

%define		_prefix		/usr/X11R6
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

%prep
%setup -q
%patch -p1
%patch1 -p1

%build
%{__make} -f Makefile.cvs
KDEDIR=%{_prefix}; export KDEDIR
QTDIR=%{_prefix}; export QTDIR

CFLAGS="-D_GNU_SOURCE %{rpmcflags} -DNDEBUG -DNO_DEBUG" \
CXXFLAGS="-D_GNU_SOURCE %{rpmcflags} -DNDEBUG -DNO_DEBUG -fno-check-new" \
./configure --prefix=%{_prefix}

LANG=C %{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_datadir}/icons/locolor/16x16/apps/kteatime.png
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/locolor/16x16/apps/ktux.png
rm -f $RPM_BUILD_ROOT%{_datadir}/icons/locolor/32x32/apps/ktux.png

cd $RPM_BUILD_ROOT%{_docdir}/HTML/en
for i in *; do
  [ -d $i -a -L $i/common ] && ln -nfs ../common $i/common
done
cd $RPM_BUILD_ROOT%{_datadir}/apps/amor && ln -nfs tips-en tips

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_includedir}/*
%attr(755,root,root) %{_libdir}/*
%{applnkdir}/System/ScreenSavers/ktux.desktop
%{_datadir}/apps/amor
%{_datadir}/apps/kdesktop/programs/kdeworld.desktop
%{_datadir}/apps/kicker/applets/*
%{_applnkdir}/Toys
%{_datadir}/kmoon
%{_datadir}/kodo
%{_datadir}/ktux
%{_datadir}/kworldclock
%{_docdir}/HTML/en/*
%{_pixmapsdir}/*/*/apps/*
