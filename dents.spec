# TODO:
# - init script
Summary:	This is the DENTS nameserver
Summary(pl):	Serwer nazw DENTS
Name:		dents
Version:	0.3.1
Release:	1
License:	GPL
Group:		Networking/Daemons
Source0:	http://dl.sourceforge.net/dents/%{name}-%{version}.tar.gz
# Source0-md5:	b7ffc0305143731b70934240acd426b6
URL:		http://sourceforge.net/projects/dents/
BuildRequires:	glib-devel
PreReq:		rc-scripts
Requires(post,preun):	/sbin/chkconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dents. It's a name server that doesn't suck.

%description -l pl
Dents. Jest to serwer nazw, który nie obsysa.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
/sbin/chkconfig --add dents
if [ -f /var/lock/subsys/dents ]; then
	/etc/rc.d/init.d/dents restart 1>&2
else
	echo "Run \"/etc/rc.d/init.d/dents start\" to start dents DNS server."
fi

%preun
if [ "$1" = "0" ]; then
	if [ -f /var/lock/subsys/dents ]; then
		/etc/rc.d/init.d/dents stop 1>&2
	fi
	/sbin/chkconfig --del dents
fi

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/dents
%dir %{_libdir}/dents
%attr(755,root,root) %{_libdir}/dents/mod_*.so*
