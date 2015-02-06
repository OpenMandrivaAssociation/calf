%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define git_snapshot git20120421
%endif

Name:           calf
Summary:        Pack of multi-standard audio plugins and host for JACK
Version:        0.0.19

%if %branch
Release:        %mkrel -c %git_snapshot 1
%else
Release:        6
%endif

%if %branch
Source:         http://repo.or.cz/w/%{name}.git/snapshot/%{name}-f63124a88bff1c6444639e6969854e5ed162f24d.tar.gz
%else
Source:         http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
%endif
URL:            http://%{name}.sourceforge.net/
License:        GPLv2
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  desktop-file-utils expat-devel cairo-devel
BuildRequires:  gtk2-devel
BuildRequires:  fftw2-devel
BuildRequires:  pkgconfig
BuildRequires:  pkgconfig(gconf-2.0)
BuildRequires:  jackit-devel lv2-devel readline-devel
BuildRequires:  fluidsynth-devel
Requires:       redland lv2 fluidsynth

%description
Calf is a pack of audio plugins for the LV2 interface.
Calf contains the following audio effects: vintage delay,
rotary speaker, reverb, multi chorus, flanger, phaser, filter,
compressor. It also contains two full-blown synthesizers: monosynth and
organ.

%prep
%if %branch
%setup -q -n calf
%else
%setup -q
%endif

%build
%if %branch
./autogen.sh
%endif
LDFLAGS='-lgthread-2.0' \
%configure  --with-ladspa-dir=%{_libdir}/ladspa \
                --with-dssi-dir=%{_libdir}/dssi \
                --with-lv2-dir=%{_libdir}/lv2 \
                --enable-static=false \
                --libdir=%{_libdir} \
                --without-lash --enable-experimental=yes
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
desktop-file-install --add-category=";X-MandrivaLinux-Multimedia-Sound;" \
                     --add-category="GTK;" \
                     --remove-key="Version" \
                     --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

rm -f %{buildroot}/%{_datadir}/icons/hicolor/icon-theme.cache

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING AUTHORS
%{_bindir}/calfjackhost
%{_libdir}/lv2/%{name}.lv2
%{_libdir}/%{name}/%{name}.so


%{_datadir}/%{name}/*

%{_datadir}/icons/hicolor/16x16/apps/calf.png
%{_datadir}/icons/hicolor/24x24/apps/calf.png
%{_datadir}/icons/hicolor/32x32/apps/calf.png
%{_datadir}/icons/hicolor/48x48/apps/calf.png
%{_datadir}/icons/hicolor/128x128/apps/calf.png
%{_datadir}/icons/hicolor/128x128/apps/calf_plugin.png
%{_datadir}/icons/hicolor/16x16/apps/calf_plugin.png
%{_datadir}/icons/hicolor/22x22/apps/calf.png
%{_datadir}/icons/hicolor/22x22/apps/calf_plugin.png
%{_datadir}/icons/hicolor/24x24/apps/calf_plugin.png
%{_datadir}/icons/hicolor/256x256/apps/calf.png
%{_datadir}/icons/hicolor/256x256/apps/calf_plugin.png
%{_datadir}/icons/hicolor/32x32/apps/calf_plugin.png
%{_datadir}/icons/hicolor/48x48/apps/calf_plugin.png
%{_datadir}/icons/hicolor/64x64/apps/calf.png
%{_datadir}/icons/hicolor/64x64/apps/calf_plugin.png
%{_datadir}/icons/hicolor/scalable/apps/calf.svg
%{_datadir}/icons/hicolor/scalable/apps/calf_plugin.svg

%{_mandir}/man1/calfjackhost.1.*
%{_mandir}/man7/calf.7.*

%{_datadir}/applications/%{name}.desktop



%changelog
* Wed Apr 25 2012 Frank Kober <emuse@mandriva.org> 0.0.19-0.git20120421.1mdv2012.0
+ Revision: 793444
- new git snapshot
  o adjust file list
  o adapt BR names
  o drop strfmt fix patch

* Tue Jun 28 2011 Frank Kober <emuse@mandriva.org> 0.0.19-0.git20110507.1
+ Revision: 687626
- try included autogen.sh instead of autoreconf
- bump version to 0.0.19
- add string format fix
- update to latest git version from 2011-05-07
  o keep official version tarball

* Sun Feb 27 2011 Funda Wang <fwang@mandriva.org> 0.0.18.6-5
+ Revision: 640427
- rebuild to obsolete old packages

* Mon Feb 14 2011 Frank Kober <emuse@mandriva.org> 0.0.18.6-4
+ Revision: 637747
- disable lash, fix hicolor icon cache conflict

* Sun Feb 13 2011 Frank Kober <emuse@mandriva.org> 0.0.18.6-3
+ Revision: 637570
- fix icon paths
- rebuild for fixed redland

* Wed Feb 09 2011 Frank Kober <emuse@mandriva.org> 0.0.18.6-2
+ Revision: 637055
- rebuild for new raptor

* Tue Aug 24 2010 Frank Kober <emuse@mandriva.org> 0.0.18.6-1mdv2011.0
+ Revision: 572936
- new version 0.18.6 (bugfix)
  o replace autoreconf by configure2_5x

* Tue Jan 05 2010 Stéphane Téletchéa <steletch@mandriva.org> 0.0.18.5-1mdv2010.1
+ Revision: 486367
- Another missing BR
- Missing BR readline
- Precise plugins path

  + Frank Kober <emuse@mandriva.org>
    - manpage compression format generalized
    - Update rpm group tag
    - Update rpm group tag
    - import calf


* Sat Dec 19 2009 Frank Kober <emuse@mandriva.org> 0.0.18.5-1mdv2010.0
- import calf
