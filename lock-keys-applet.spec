%define name lock-keys-applet
%define version 1.0
%define release %mkrel 1

Summary: Gnome applet that shows the status of the caps-, num- and scroll-lock keys
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://www.wh-hms.uni-ulm.de/~mfcn/shared/lock-keys/lock-keys-applet-1.0.tar.gz
patch0:	new-tooltips-api.patch	
patch1:	fix-deprecated.patch
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://www.wh-hms.uni-ulm.de/~mfcn/lock-keys-applet/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: libgnomeui2-devel
BuildRequires: libglade2.0-devel
BuildRequires: libpanel-applet-2-devel
BuildRequires: scrollkeeper
Requires(post): scrollkeeper
Requires(postun): scrollkeeper

%description
Lock keys applet is a GNOME-applet, that shows the status of the caps-, 
num- and scroll-lock keys of your keyboard. This isn't especially useful 
for normal keyboards, as they got leds for that. But some keyboards 
(especially wireless keyboards) don't have. One more feature of the applet 
is that it saves the status of the lock-keys and restores it, when starting 
Gnome.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall_std
%find_lang %{name}

%clean
rm -rf %{buildroot}

%post
%update_scrollkeeper

%postun
%clean_scrollkeeper

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog README TODO
%{_datadir}/gnome/help/%{name}
%{_datadir}/omf/%{name}
%{_datadir}/pixmaps/%{name}.png
%{_libdir}/bonobo/servers/*.server
%{_libexecdir}/%{name}
