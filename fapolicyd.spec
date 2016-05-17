Summary: File Access Policy Daemon
Name: fapolicyd
Version: 0.8
Release: 1
License: GPLv2+
Group: System Environment/Daemons
URL: http://people.redhat.com/sgrubb/fapolicyd
Source0: http://people.redhat.com/sgrubb/fapolicyd/%{name}-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: kernel-headers >=  2.6.36
BuildRequires: systemd-devel libgcrypt-devel rpm-devel file-devel
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
Fapolicyd is a daemon that uses the fanotify interface to decide file
access rights.

%prep
%setup -q

%build
%configure --sbindir=/sbin 

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR="${RPM_BUILD_ROOT}" INSTALL='install -p' install

%post
%systemd_post fapolicyd.service

%preun
%systemd_preun fapolicyd.service

%postun
%systemd_postun_with_restart fapolicyd.service

%files
%defattr(-,root,root,-)
%attr(750,root,root) %dir /etc/fapolicyd
%config(noreplace) %attr(640,root,root) /etc/fapolicyd/fapolicyd.rules
%config(noreplace) %attr(640,root,root) /etc/fapolicyd/fapolicyd.mounts
%attr(640,root,root) %{_unitdir}/fapolicyd.service
%attr(755,root,root) /sbin/fapolicyd
%attr(644,root,root) %{_mandir}/man8/fapolicyd.8.gz
%attr(644,root,root) %{_mandir}/man5/fapolicyd.rules.5.gz

%changelog
* Tue May 17 2016 Steve Grubb <sgrubb@redhat.com> 0.8-1
- Initial public release

