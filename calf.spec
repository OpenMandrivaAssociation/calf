Name:           calf
Summary:        Pack of multi-standard audio plugins for LV2 and host for JACK
Version:        0.90.4
Release:        1
License:        GPLv2
Group:          Sound/Midi
URL:            https://calf-studio-gear.org/
Source0:        https://github.com/%{name}-studio-gear/%{name}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  desktop-file-utils
BuildRequires:	pkgconfig(bash-completion)
BuildRequires:  pkgconfig(dssi)
BuildRequires:  pkgconfig(expat)
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(gtk+-2.0)
BuildRequires:  pkgconfig(fftw3)
BuildRequires:  pkgconfig(libglade-2.0)
BuildRequires:  pkgconfig(jack)
BuildRequires:  pkgconfig(lv2) >= 1.12.0
BuildRequires:  readline-devel
BuildRequires:  ladspa-devel
BuildRequires:  pkgconfig(fluidsynth)
BuildRequires:  pkgconfig(lash-1.0)
Requires:       redland
Requires:       lv2 >= 1.12.0
Requires:       fluidsynth

%description
Calf is a pack of audio plugins for the LV2 interface.
- Instruments and tone generators (Organ, Monosynth, Wavetable,
Fluidsynth)
- Modulation effects (Multi Chorus, Phaser, Flanger, Rotary, Pulsator,
Ring Modulator)
- Delay effects (Reverb, Vintage Delay,Compensation Delay Line, 
Reverse Delay)
- Dynamic processors (Compressor, Sidechain Compressor, Multiband 
Compressor, Mono Compressor, Deesser, Gate, Sidechain Gate, 
Multiband Gate, Limiter, Multiband Limiter, Sidechain Limiter, 
Transient Designer)
- Filters and equalizers (Filter, Filterclavier, Envelope Filter, 
Equalizer 5 Band, Equalizer 8 Band, Equalizer 12 Band, 
Equalizer 30 Band, Vocoder, Emphasis)
- Distortion and enhancement (Saturator, Exciter, Bass Enhancer, 
Tape Simulator, Vinyl, Crusher)
- Tools (Mono Input, Stereo Tools, Haas Stereo Enhancer, Multi Spread, 
Analyzer, X-Over 2 Band, X-Over 3 Band, X-Over 4 Band)

The plugins are available in LV2 and Standalone JACK formats.

This package contains common files and JACK standalone program.

%package -n lv2-%{name}-plugins
Summary:        Calf plugins in LV2 format
Group:          Sound/Midi
License:        GPLv2+ and LGPLv2+ and Public Domain
Requires:       %{name} = %{version}-%{release}

%description -n lv2-%{name}-plugins
Calf is a pack of audio plugins for the LV2 interface.
- Instruments and tone generators (Organ, Monosynth, Wavetable,
Fluidsynth)
- Modulation effects (Multi Chorus, Phaser, Flanger, Rotary, Pulsator,
Ring Modulator)
- Delay effects (Reverb, Vintage Delay,Compensation Delay Line, 
Reverse Delay)
- Dynamic processors (Compressor, Sidechain Compressor, Multiband 
Compressor, Mono Compressor, Deesser, Gate, Sidechain Gate, 
Multiband Gate, Limiter, Multiband Limiter, Sidechain Limiter, 
Transient Designer)
- Filters and equalizers (Filter, Filterclavier, Envelope Filter, 
Equalizer 5 Band, Equalizer 8 Band, Equalizer 12 Band, 
Equalizer 30 Band, Vocoder, Emphasis)
- Distortion and enhancement (Saturator, Exciter, Bass Enhancer, 
Tape Simulator, Vinyl, Crusher)
- Tools (Mono Input, Stereo Tools, Haas Stereo Enhancer, Multi Spread, 
Analyzer, X-Over 2 Band, X-Over 3 Band, X-Over 4 Band)

This package contains LV2 synthesizers and effects, MIDI I/O and GUI
extensions.

%prep
%autosetup -p1

%build
# Need to use GCC, because compilation failing with Clang. Bug in upstream: https://github.com/calf-studio-gear/calf/issues/156
#export CC=gcc
#export CXX=g++
export NOCONFIGURE=1
./autogen.sh

%configure  --with-lv2-dir=%{_libdir}/lv2 \
            --with-ladspa-dir=%{_libdir}/ladspa/ \
            --with-dssi-dir=%{_libdir}/dssi/ \
%ifarch x86_64 %ix86
	          --enable-sse \
%endif
            --enable-ladspa \
            --enable-static=false \
            --libdir=%{_libdir} \
            --enable-experimental=yes
%make_build

%install
%make_install
# JACK host
desktop-file-install \
     --remove-category="Application" \
     --remove-category="GNOME" \
     --add-category="X-Midi" \
     --add-category="X-Mageia-CrossDesktop" \
     --remove-key="Version" \
     --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

rm -f %{buildroot}/%{_datadir}/icons/hicolor/icon-theme.cache

find %{buildroot} -name '*.la' -delete

%files
%doc README AUTHORS COPYING
%doc %{_docdir}/%{name}/*
%{_bindir}/%{name}jackhost
%{_libdir}/%{name}/%{name}.so

%{_datadir}/%{name}

%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}_plugin.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}_plugin.svg

%{_mandir}/man1/%{name}jackhost.1.*
%{_mandir}/man7/%{name}.7.*

%{_datadir}/applications/%{name}.desktop
%{_datadir}/bash-completion/completions/%{name}

%files -n lv2-%{name}-plugins
%{_libdir}/lv2/%{name}.lv2/
