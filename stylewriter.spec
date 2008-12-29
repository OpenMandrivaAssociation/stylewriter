Summary:	Non-MacOS StyleWriter driver
Name:		stylewriter
Version:	0.9.9
Release:	%mkrel 7
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
