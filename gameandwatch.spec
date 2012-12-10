%define		svn	131

Name:		gameandwatch
Version:	0.3
Release:	%mkrel %{svn}.1
Summary:	A generic engine for simulation of Game & Watch-like games
Group:		Emulators
License:	GPL
URL:		http://www.rangelreale.com/programming/game-watch-simulator
# fetched from svn
Source0:	%{name}-%{version}-%{svn}.tar.bz2
Patch0:		gameandwatch-0.3-131-type.patch
BuildRequires:	boost-devel
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_gfx-devel
BuildRequires:	SDL_ttf-devel
BuildRequires:	SDL_mixer-devel
BuildRequires:	pkgconfig(zziplib)

%description
This is a generic engine for simulation of Game & Watch games,
starting with ports of the Madrigal Game & Watch Simulators
(http://www.madrigaldesign.it/sim/).

It is designed to run anywhere SDL is available, withemphasis
in handheld machines.

Currently 6 games from VTECH are simulated:
- MONKEY
- PIRATE
- DEFENDO
- CONDOR
- PANCAKE
- ROLLER COASTER

%prep
%setup -q -n %{name}-%{version}-%{svn}
%patch0 -p1

%build
autoreconf -fi
%configure2_5x
%make

%install
%__rm -rf %{buildroot}
%makeinstall_std

# menu-entry, overwrite the default one
%__mkdir_p  %{buildroot}%{_datadir}/applications
%__cat > %{buildroot}%{_datadir}/applications/%{name}.desktop << EOF
[Desktop Entry]
[Desktop Entry]
Version=1.0
Name=Game & Watch Simulator
Comment=Game & Watch-like games simulator
Exec=gameandwatch %U
Icon=gameandwatch
Terminal=false
Type=Application
Categories=Game;Emulator;
EOF

%__rm -rf %{buildroot}%{_docdir}

%clean
%__rm -rf %{buildroot}

%files
%doc doc/README
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/pixmaps/%{name}.png


%changelog
* Wed Mar 14 2012 Andrey Bondrov <abondrov@mandriva.org> 0.3-131.1
+ Revision: 784962
- Update BuildRequires
- imported package gameandwatch

