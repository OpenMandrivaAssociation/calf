%define name    calf
%define version 0.0.18.6
%define release %mkrel 5

Name:           %{name}
Summary:        Pack of multi-standard audio plugins and host for JACK
Version:        %{version}
Release:        %{release}

Source:         http://dl.sf.net/calf/%{name}-%{version}.tar.gz
URL:            http://calf.sourceforge.net/
License:        GPLv2
Group:          Sound
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:  desktop-file-utils dssi-devel expat-devel gtk2-devel
BuildRequires:  ladspa-devel jackit-devel libglade2-devel lv2core-devel readline-devel
Requires:       redland dssi lv2core ladspa

%description
Calf is a pack of audio plugins for the DSSI, LV2, and LADSPA interface.
Calf contains the following audio effects: vintage delay,
rotary speaker, reverb, multi chorus, flanger, phaser, filter,
compressor. It also contains two full-blown synthesizers: monosynth and
organ.

%prep
%setup -q

%build
%configure2_5x --with-ladspa-dir=%{_libdir}/ladspa \
                --with-dssi-dir=%{_libdir}/dssi \
                --with-lv2-dir=%{_libdir}/lv2 \
                --without-lash
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std
desktop-file-install --add-category="X-MandrivaLinux-Multimedia-Sound;" \
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

