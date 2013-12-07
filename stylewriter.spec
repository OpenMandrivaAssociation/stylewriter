Summary:	Non-MacOS StyleWriter driver
Name:		stylewriter
Version:	0.9.9
Release:	16
License:	GPL
Group:		System/Printing
URL:		http://homepage.mac.com/monroe/styl/
Source:		http://homepage.mac.com/monroe/styl/stylewriter.tar.gz
Patch0:		stylewriter-gcc4.patch
#BuildRequires:	netatalk-devel
Conflicts:	printer-utils = 2007
Conflicts:	printer-filters = 2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This is a driver for certain types of Apple StyleWriter printers. 

%prep

%setup -q -n %{name}
%patch0 -p0

%build

gcc %{optflags} %{ldflags} -o lpstyl lpstyl.c

# it will not build...
#gcc %{optflags} -DATALK=1 lpstyl.c adsp.c -o lpstyl-atalk -latalk

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}

install -m0755 lpstyl %{buildroot}%{_bindir}
#install -m0755 lpstyl-atalk %{buildroot}%{_bindir}

%clean
rm -rf %{buildroot}

%files
%defattr(0644,root,root,0755)
%doc scripts README* printcap* styl.ppd
%attr(0755,root,root) %{_bindir}/*


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.9.9-11mdv2011.0
+ Revision: 670219
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.9-10mdv2011.0
+ Revision: 607755
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.9-9mdv2010.1
+ Revision: 524136
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.9.9-8mdv2010.0
+ Revision: 427217
- rebuild

* Mon Dec 29 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.9-7mdv2009.1
+ Revision: 321053
- use %%ldflags

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.9.9-6mdv2009.0
+ Revision: 225505
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.9.9-5mdv2008.1
+ Revision: 179549
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Aug 30 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.9-4mdv2008.0
+ Revision: 75358
- fix deps (pixel)

* Wed Aug 22 2007 Thierry Vignaud <tv@mandriva.org> 0.9.9-3mdv2008.0
+ Revision: 68995
- fix description

* Sun Aug 19 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.9-2mdv2008.0
+ Revision: 66563
- use the new System/Printing RPM GROUP

* Sat Aug 11 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.9-1mdv2008.0
+ Revision: 62009
- Import stylewriter



* Sat Aug 11 2007 Oden Eriksson <oeriksson@mandriva.com> 0.9.9-1mdv2008.0
- initial Mandriva package
