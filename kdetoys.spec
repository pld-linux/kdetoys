%define sourcedir stable/%{version}/distribution/tar/generic/source
%define is_release 1
%define beta %{nil}
%define DATE 20010823
%define rel 5
Version: 2.2

Name: kdetoys
Prefix: /usr
%if %{is_release}
%if "%{beta}" != ""
Release: 1.%{beta}.%{rel}
Source: ftp://ftp.kde.org/pub/kde/%{sourcedir}/%{name}-%{version}-%{beta}.tar.bz2
%else
Release: %{rel}
Source: ftp://ftp.kde.org/pub/kde/%{sourcedir}/%{name}-%{version}.tar.bz2
%endif
%else
Release: 1.cvs%{DATE}.%{rel}
Source: ftp://ftp.kde.org/pub/kde/%{sourcedir}/%{name}-%{DATE}.tar.bz2
%endif
Patch: kdetoys-2.2-kworldclock.patch
Patch1: kdetoys-2.2-cvsfixes.patch
Icon: kde-icon.xpm
Summary: Toys for KDE.
Epoch: 7
Group: Amusements/Graphics
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL
Prereq: /sbin/ldconfig
Requires: kdelibs >= 2.2

%description
The kdetoys package includes various toys for the K Desktop
Environment (KDE), including: kmoon, which displays the phases of the
moon; kworldwatch, which graphically displays the Earth's day and
night; and kodo, a mouse odometer which shows how far your mouse has
traveled.

%prep

%if %{is_release}
%setup -q
%else
%setup -q -n %{name}
%endif
%patch -p1 -b .kdetoys
%patch1 -p1 -b .cvs
make -f Makefile.cvs

%build
export KDEDIR=%{prefix}
unset QTDIR || : ; . /etc/profile.d/qt.sh

CFLAGS="-D_GNU_SOURCE $RPM_OPT_FLAGS -DNDEBUG -DNO_DEBUG" \
CXXFLAGS="-D_GNU_SOURCE $RPM_OPT_FLAGS -DNDEBUG -DNO_DEBUG -fno-check-new" \
./configure --prefix=%{prefix}

LANG=C make

%install
rm -rf $RPM_BUILD_ROOT

make install-strip DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT/usr/share/icons/locolor/16x16/apps/kteatime.png
rm -f $RPM_BUILD_ROOT/usr/share/icons/locolor/16x16/apps/ktux.png
rm -f $RPM_BUILD_ROOT/usr/share/icons/locolor/32x32/apps/ktux.png

cd $RPM_BUILD_ROOT/usr/share/doc/HTML/en
for i in *; do
  [ -d $i -a -L $i/common ] && ln -nfs ../common $i/common
done
cd $RPM_BUILD_ROOT/usr/share/apps/amor && ln -nfs tips-en tips

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{prefix}/bin/*
%{prefix}/include/*
%{prefix}/lib/*
%{prefix}/share/applnk/System/ScreenSavers/ktux.desktop
%{prefix}/share/apps/amor
%{prefix}/share/apps/kdesktop/programs/kdeworld.desktop
%{prefix}/share/apps/kicker/applets/*
%{prefix}/share/applnk/Toys
%{prefix}/share/apps/kmoon
%{prefix}/share/apps/kodo
%{prefix}/share/apps/ktux
%{prefix}/share/apps/kworldclock
%{prefix}/share/doc/HTML/en/*
%{prefix}/share/icons/*/*/apps/*

%changelog
* Wed Sep 12 2001 Tim Powers <timp@redhat.com>
- rebuild with new gcc and binutils

* Thu Aug 23 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-4
- Remove duplicates from kdeartwork-locolor (part of #51589)

* Wed Aug 22 2001 Than Ngo <than@redhat.com> 2.2-3
- fix kworldclock crashes (bug #52210)

* Thu Aug 16 2001 Than Ngo <than@redhat.com> 2.2-2
- fix bug #51856

* Mon Jul 23 2001 Bernhard Rosenkraenzer <bero@redhat.com> 2.2-0.cvs20010723.1
- Update

* Wed Feb 21 2001 Than Ngo <than@redhat.com>
- 2.1-respin

* Tue Feb 20 2001 Than Ngo <than@redhat.com>
- update to 2.1

* Mon Feb 05 2001 Than Ngo <than@redhat.com>
- updated
- fixed absolute-pathname symlinks (bug #24795)

* Mon Jan 22 2001 Bernhard Rosenkraenzer <bero@redhat.com>
- Update

* Wed Dec 20 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- update to CVS 
- Don't exclude ia64

* Mon Oct 23 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.0 final


* Wed Oct  4 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.0

* Thu Aug 24 2000 Than Ngo <than@redhat.com>
- update to kdetoys-1.93

* Mon Aug  7 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- new version

* Thu Jul 13 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- SMPify
- don't hardcode QTDIR

* Tue Jul 11 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- use gcc 2.96
- new snapshot

* Wed Jun 21 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- new snapshot
- ExcludeArch ia64 for now

* Mon Apr 10 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- 2.0 snapshot

* Sat Jan  8 2000 Bernhard Rosenkraenzer <bero@redhat.com>
- KDE_1_1_BRANCH
- rebuild for 6.2

* Fri Sep 24 1999 Preston Brown <pbrown@redhat.com>
- marked docs files as such.

* Tue Sep 14 1999 Preston Brown <pbrown@redhat.com>
- got 1.1.2 release.

* Thu Sep 09 1999 Preston Brown <pbrown@redhat.com>
- built for 6.1

* Fri Jun 11 1999 Preston Brown <pbrown@redhat.com>
- snapshot, includes kde 1.1.1 + fixes
