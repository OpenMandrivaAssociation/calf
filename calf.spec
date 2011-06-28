%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %branch
%define git_snapshot git20110507
%endif

Name:           calf
Summary:        Pack of multi-standard audio plugins and host for JACK
Version:        0.0.19

%if %branch
Release:        %mkrel -c %git_snapshot 1
%else
Release:        %mkrel 5
%endif

%if %branch
Source:         http://repo.or.cz/w/%{name}.git/snapshot/457380c144f1aee7563ec0b58d1c7d5f3da1204a.tar.gz
Patch0:         calf_git_fix_strfmt.patch
%else
Source:         http://dl.sf.net/%{name}/%{name}-%{version}.tar.gz
%endif
URL:            http://%{name}.sourceforge.net/
License:        GPLv2
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  desktop-file-utils dssi-devel expat-devel pango-devel
BuildRequires:  ladspa-devel jackit-devel lv2core-devel readline-devel
Requires:       redland dssi lv2core ladspa

%description
Calf is a pack of audio plugins for the DSSI, LV2, and LADSPA interface.
Calf contains the following audio effects: vintage delay,
rotary speaker, reverb, multi chorus, flanger, phaser, filter,
compressor. It also contains two full-blown synthesizers: monosynth and
organ.

%prep
%if %branch
%setup -q -n calf
%patch0 -p0
%else
%setup -q
%endif

%build
%if %branch
./autogen.sh
%endif
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
%{_libdir}/dssi/%{name}.so
%{_libdir}/dssi/%{name}/%{name}_gtk
%{_libdir}/ladspa/%{name}.so
%{_libdir}/lv2/%{name}.lv2

%{_libdir}/%{name}/%{name}.so
%{_libdir}/%{name}/%{name}.la
%{_libdir}/%{name}/%{name}_gtk


%{_datadir}/%{name}/*
%{_datadir}/ladspa/rdf/*

%{_datadir}/icons/hicolor/16x16/apps/calf.png
%{_datadir}/icons/hicolor/24x24/apps/calf.png
%{_datadir}/icons/hicolor/32x32/apps/calf.png
%{_datadir}/icons/hicolor/48x48/apps/calf.png

%{_mandir}/man1/calfjackhost.1.*
%{_mandir}/man7/calf.7.*

%{_datadir}/applications/%{name}.desktop

%changelog
* Sat Dec 19 2009 Frank Kober <emuse@mandriva.org> 0.0.18.5-1mdv2010.1
- import calf

