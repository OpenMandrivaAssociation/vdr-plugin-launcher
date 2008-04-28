
%define plugin	launcher
%define name	vdr-plugin-%plugin
%define version	0.0.2a
%define rel	14

Summary:	VDR plugin: launch other plugins
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://people.freenet.de/cwieninger/html/vdr-launcher.html
Source:		http://people.freenet.de/cwieninger/vdr_1.3.11-%plugin-%version.tar.bz2
Patch0:		launcher-0.0.2a-i18n-1.6.patch
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This is a little plugin, that allows you to select and start other
plugins, even if there are not shown in the main menu. You can also
access the setup menu of a plugin.

%prep
%setup -q -n %plugin-%version
%patch0 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY


