Summary:	Non-MacOS StyleWriter driver
Name:		stylewriter
Version:	0.9.9
Release:	%mkrel 2
License:	GPL
Group:		System/Printing
URL:		http://homepage.mac.com/monroe/styl/
Source:		http://homepage.mac.com/monroe/styl/stylewriter.tar.gz
Patch0:		stylewriter-gcc4.patch
#BuildRequires:	netatalk-devel
Conflicts:	printer-utils-2006 printer-utils-2007
Conflicts:	printer-filters-2006 printer-filters-2007
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
This is a driver for certain types of Apple StyleWriter printers that works
under various flavors of unix. It was originally developed under NetBSD-mac68k,
and is reported to work under NetBSD-i386, Linux-i386, and recent versions of
MkLinux-PPC and linux-pmac with some tweaking and/or the right cables. Note
that the driver needs to talk to the printer (and vice-versa) at 57600 baud,
so you may have trouble if your serial drivers are not quite ready for
prime-time. I have heard that some beta versions of the mklinux 2.0 kernel
don't deal well with baud rates this high. I have also heard at least one
report that it does work on "recent" versions of linux-pmac. Caveat emptor,
YMMV, etc, etc.

%prep

%setup -q -n %{name}
%patch0 -p0

%build

gcc %{optflags} -o lpstyl lpstyl.c

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
