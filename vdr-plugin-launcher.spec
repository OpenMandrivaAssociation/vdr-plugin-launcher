%define plugin	launcher

Summary:	VDR plugin: launch other plugins
Name:		vdr-plugin-%plugin
Version:	0.0.2a
Release:	18
Group:		Video
License:	GPL
URL:		http://people.freenet.de/cwieninger/html/vdr-launcher.html
Source:		http://people.freenet.de/cwieninger/vdr_1.3.11-%plugin-%{version}.tar.bz2
Patch0:		launcher-0.0.2a-i18n-1.6.patch
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
This is a little plugin, that allows you to select and start other
plugins, even if there are not shown in the main menu. You can also
access the setup menu of a plugin.

%prep
%setup -q -n %plugin-%{version}
%patch0 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README* HISTORY




