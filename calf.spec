Summary:	Pack of multi-standard audio plugins for LV2 and host for JACK
Name:	calf
Version:	0.90.9
Release:	1
License:	GPLv2
Group:	Sound
Url:	https://calf-studio-gear.org/
Source0:	https://github.com/calf-studio-gear/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch0: calf-0.90.7-use-ladish-in-place-of-lash.patch
BuildRequires:	cmake >= 3.15
BuildRequires:	desktop-file-utils
BuildRequires:	ladspa-devel
BuildRequires:	pkgconfig(bash-completion)
BuildRequires:	pkgconfig(cairo)
BuildRequires:	pkgconfig(dssi)
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(fluidsynth)
BuildRequires:	pkgconfig(fftw3)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(liblash) >= 1.1.1
BuildRequires:	pkgconfig(libglade-2.0)
BuildRequires:	pkgconfig(lv2) >= 1.14.0
BuildRequires:	pkgconfig(readline)
Requires:	fluidsynth
Requires:	lv2 >= 1.14.0
Requires:	redland

%description
Calf is a pack of audio plugins for the LV2 interface.
- Instruments and tone generators (Organ, Monosynth, Wavetable, Fluidsynth).
- Modulation effects (Multi Chorus, Phaser, Flanger, Rotary, Pulsator, Ring
  Modulator).
- Delay effects (Reverb, Vintage Delay,Compensation Delay Line, Reverse Delay)
- Dynamic processors (Compressor, Sidechain Compressor, Multiband Compressor,
  Mono Compressor, Deesser, Gate, Sidechain Gate, Multiband Gate, Limiter,
  Multiband Limiter, Sidechain Limiter, Transient Designer).
- Filters and equalizers (Filter, Filterclavier, Envelope Filter, Equalizer 5
  Band, Equalizer 8 Band, Equalizer 12 Band, Equalizer 30 Band, Vocoder,
  Emphasis).
- Distortion and enhancement (Saturator, Exciter, Bass Enhancer, Tape
  Simulator, Vinyl, Crusher).
- Tools (Mono Input, Stereo Tools, Haas Stereo Enhancer, Multi Spread,
  Analyzer, X-Over 2 Band, X-Over 3 Band, X-Over 4 Band).
The plugins are available in LV2 and Standalone JACK formats.
This package contains common files and the JACK standalone program.

%files
%doc README.md AUTHORS COPYING
%doc %{_docdir}/%{name}/*
%{_bindir}/%{name}jackhost
%{_libdir}/%{name}/libcalf.so
%{_libdir}/%{name}/libcalflv2gui.so
%{_datadir}/%{name}
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/icons/hicolor/*/apps/%{name}_plugin.png
%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
%{_datadir}/icons/hicolor/scalable/apps/%{name}_plugin.svg
%{_mandir}/man1/%{name}jackhost.1.*
%{_mandir}/man7/%{name}.7.*
%{_datadir}/applications/%{name}.desktop
%{_datadir}/bash-completion/completions/%{name}

#-----------------------------------------------------------------------------

%package -n lv2-%{name}-plugins
Summary:	Calf plugins in LV2 format
Group:	Sound
License:	GPLv2+ and LGPLv2+ and Public Domain
Requires:	%{name} = %{version}-%{release}

%description -n lv2-%{name}-plugins
Calf is a pack of audio plugins for the LV2 interface.
- Instruments and tone generators (Organ, Monosynth, Wavetable, Fluidsynth).
- Modulation effects (Multi Chorus, Phaser, Flanger, Rotary, Pulsator, Ring
  Modulator).
- Delay effects (Reverb, Vintage Delay,Compensation Delay Line, Reverse Delay)
- Dynamic processors (Compressor, Sidechain Compressor, Multiband Compressor,
  Mono Compressor, Deesser, Gate, Sidechain Gate, Multiband Gate, Limiter,
  Multiband Limiter, Sidechain Limiter, Transient Designer).
- Filters and equalizers (Filter, Filterclavier, Envelope Filter, Equalizer 5
  Band, Equalizer 8 Band, Equalizer 12 Band, Equalizer 30 Band, Vocoder,
  Emphasis).
- Distortion and enhancement (Saturator, Exciter, Bass Enhancer, Tape
  Simulator, Vinyl, Crusher).
- Tools (Mono Input, Stereo Tools, Haas Stereo Enhancer, Multi Spread,
  Analyzer, X-Over 2 Band, X-Over 3 Band, X-Over 4 Band).
The plugins are available in LV2 and Standalone JACK formats.
This package contains LV2 synthesizers and effects, MIDI I/O and GUI
extensions.

%files -n lv2-%{name}-plugins
%{_libdir}/lv2/%{name}.lv2/

#-----------------------------------------------------------------------------

%prep
%autosetup -p1


%build
%cmake -DWANT_EXPERIMENTAL=YES \
%ifarch x86_64 %{ix86}
			-DWANT_SSE=ON
%else
			-DWANT_SSE=OFF
%endif

%make_build


%install
%make_install -C build

# Fix .desktop file for the JACK host
desktop-file-edit \
     --remove-category="Application" \
     --remove-category="GNOME" \
     --add-category="X-Midi" \
     --add-category="X-OpenMandriva-CrossDesktop" \
     --remove-key="Version" \
     %{buildroot}%{_datadir}/applications/%{name}.desktop
