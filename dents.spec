Summary: This is the DENTS nameserver
%define PACKAGE_NAME dents
NAME: %PACKAGE_NAME
VERSION: 0.3.1
Release: 1
Source: dents-0.3.1.tar.gz
Copyright: GPL
BuildRoot: /tmp/dents-0.3.1-rpm-build-root
Group: Utilities/Network
Provides: dents

%description

Dents. It's a name server that doesn't suck.

%prep
%setup -n %{PACKAGE_NAME}-%{PACKAGE_VERSION}
%build
./configure --prefix=$RPM_BUILD_ROOT/usr/local
make
%install

make install
%clean
rm -rf $RPM_BUILD_ROOT
%files
/usr/local/sbin/dents
/usr/local/lib/dents/mod_frl.so.0.0.0        
/usr/local/lib/dents/mod_recursive.so.0
/usr/local/lib/dents/mod_frl.la
/usr/local/lib/dents/mod_recursive.so.0.0.0
/usr/local/lib/dents/mod_frl.so
/usr/local/lib/dents/mod_recursive.la
/usr/local/lib/dents/mod_frl.so.0
/usr/local/lib/dents/mod_recursive.so
/usr/local/lib/dents/mod_msg_tgl.la
/usr/local/lib/dents/mod_msg_tgl.so.0.0.0
/usr/local/lib/dents/mod_msg_tgl.so
