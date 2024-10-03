%global pes_events_build_date 20240821

%define dist_list almalinux centos eurolinux oraclelinux rocky cloudlinux
%define conflict_dists() %(for i in almalinux centos eurolinux oraclelinux rocky cloudlinux; do if [ "${i}" != "%{dist_name}" ]; then echo -n "leapp-data-${i} "; fi; done)

Name:		leapp-data-%{dist_name}
Version:	0.3
Release:	3%{?dist}.%{pes_events_build_date}
Summary:	data for migrating tool
Group:		Applications/Databases
License:	ASL 2.0
URL:		https://github.com/AlmaLinux/leapp-data
Source0:	leapp-data-%{version}.tar.gz
BuildArch:  noarch

BuildRequires: bc
BuildRequires: python3
BuildRequires: python36-jsonschema

Conflicts: %{conflict_dists}

%description
%{dist_name} %{summary}


%prep
%setup -q

%build
make all && make test

%install
make install PREFIX=%{buildroot}

%files
%doc LICENSE NOTICE README.md
%if 0%{?rhel} == 8
%{_sysconfdir}/leapp/repos.d/system_upgrade/common/files/rpm-gpg/9/
%endif

%if 0%{?rhel} == 7
%{_sysconfdir}/leapp/repos.d/system_upgrade/common/files/rpm-gpg/8/
%endif
%{_sysconfdir}/leapp/files/*



%changelog
* Thu Sep 26 2024 Yuriy Kohut <ykohut@almalinux.org> - 0.3-3.cloudlinux
- Move GeoIP package if epel vendor is enabled
- Pack gpg keys inside the package to avoid "Detected unknown GPG keys" error (CLOS-2946)
- Do not use public CloudLinux repos during upgrade (CLOS-2970)

* Wed Aug 21 2024 Oleksandr Shyshatskyi <oshyshatskyi@cloudlinux.com> - 0.3-0.cloudlinux
- Rebase onto AlmaLinux

* Thu Jun 13 2024 Roman Prilipskii <rprilpskii@cloudlinux.com> - 0.2-9.cloudlinux
- Make EA4 repository optional

* Mon Feb 12 2024 Roman Prilipskii <rprilpskii@cloudlinux.com> - 0.2-8.cloudlinux
- Rebase data files on updated upstream

* Fri Jan 19 2024 Roman Prilipskii <rprilpskii@cloudlinux.com> - 0.2-7.cloudlinux
- Remove cPanel-related data from the vendor files

* Thu Dec 07 2023 Roman Prilipskii <rprilpskii@cloudlinux.com> - 0.2-6.cloudlinux
- Add CL Elevate package repository to the leapp repository map
- Add support for NGINX/MariaDB/PostgreSQL from upstream
- Add vendors.d files with EPEL support from upstream

* Mon Sep 25 2023 Roman Prilipskii <rprilpskii@cloudlinux.com> - 0.2-5.cloudlinux
- Add brotli to the PES mapping file

* Thu Jul 27 2023 Sloane Bernstein <sloane@cpanel.net>, Roman Prilipskii <rprilpskii@cloudlinux.com> - 0.2-4.cloudlinux
- Provide vendor data for WP Toolkit software
- Modify repo mapping for CL Hybrid installations

* Mon Mar 27 2023 Andrew Lukoshko <alukoshko@almalinux.org> - 0.2-3
- Add 8 to 9 migration support for Rocky Linux, EuroLinux, CentOS Stream

* Fri Sep 30 2022 Andrew Lukoshko <alukoshko@almalinux.org> - 0.2-2
- Split repomap.json

* Fri Sep 30 2022 Andrew Lukoshko <alukoshko@almalinux.org> - 0.2-1
- Add 8 to 9 migration support for AlmaLinux

* Thu Sep 1 2022 Roman Prilipskii <rprilpskii@cloudlinux.com> - 0.1-7
- made third-party files accessible for all supported distributions

* Wed Aug 17 2022 Andrew Lukoshko <alukoshko@almalinux.org> - 0.1-6
- added repomap.json file for all distributions

* Thu Mar 24 2022 Tomasz Podsiadły <tp@euro-linux.com> - 0.1-5
- Add EuroLinux to supported distributions

* Wed Mar 23 2022 Andrew Lukoshko <alukoshko@almalinux.org> - 0.1-4
- added ResilientStorage and updated repo URLs for AlmaLinux and Rocky

* Thu Oct 21 2021 Andrew Lukoshko <alukoshko@almalinux.org> - 0.1-3
- updated PES data for Oracle and Rocky

* Thu Aug 26 2021 Avi Miller <avi.miller@oracle.com> - 0.1-2
- switched to using the full oraclelinux name
- switched the Oracle Linux repos to use https
- added Apache-2.0 NOTICE attribution file

* Wed Aug 25 2021 Sergey Fokin <sfokin@almalinux.org> - 0.1-1
- initial project
