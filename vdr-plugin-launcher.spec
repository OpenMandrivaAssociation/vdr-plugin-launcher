
%define plugin	launcher
%define name	vdr-plugin-%plugin
%define version	0.0.2a
%define rel	17

Summary:	VDR plugin: launch other plugins
Name:		%name
Version:	%version
Release:	%mkrel %rel
Group:		Video
License:	GPL
URL:		http://people.freenet.de/cwieninger/html/vdr-launcher.html
Source:		http://people.freenet.de/cwieninger/vdr_1.3.11-%plugin-%version.tar.bz2
Patch0:		launcher-0.0.2a-i18n-1.6.patch
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
%vdr_plugin_install

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README* HISTORY




%changelog
* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2a-16mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2a-15mdv2009.1
+ Revision: 359330
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2a-14mdv2009.0
+ Revision: 197942
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2a-13mdv2009.0
+ Revision: 197684
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2a-12mdv2008.1
+ Revision: 145107
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2a-11mdv2008.1
+ Revision: 103147
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2a-10mdv2008.0
+ Revision: 50012
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2a-9mdv2008.0
+ Revision: 42098
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2a-8mdv2008.0
+ Revision: 22743
- rebuild for new vdr


* Tue Dec 05 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2a-7mdv2007.0
+ Revision: 90936
- rebuild for new vdr

* Tue Oct 31 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2a-6mdv2007.1
+ Revision: 74034
- rebuild for new vdr
- Import vdr-plugin-launcher

* Thu Sep 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2a-5mdv2007.0
- rebuild for new vdr

* Thu Aug 24 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2a-4mdv2007.0
- stricter abi requires

* Mon Aug 07 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2a-3mdv2007.0
- rebuild for new vdr

* Wed Jul 26 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2a-2mdv2007.0
- rebuild for new vdr

* Fri Jul 14 2006 Anssi Hannula <anssi@mandriva.org> 0.0.2a-1mdv2007.0
- initial Mandriva release

