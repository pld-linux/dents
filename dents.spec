Summary:	This is the DENTS nameserver
Name:		dents
Version:	0.3.1
Release:	1
License:	GPL
Group:		Networking/Daemons
Group(de):	Netzwerkwesen/Server
Group(pl):	Sieciowe/Serwery
Source0:	http://ftp1.sourceforge.net/dents/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/dents/
BuildRequires:	glib-devel
Prereq:		rc-scripts
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dents. It's a name server that doesn't suck.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%post
DESC="dents DNS server"; %chkconfig_add

%preun
%chkconfig_del

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/dents
%dir %{_libdir}/dents
%attr(755,root,root) %{_libdir}/dents/mod_*.so*
