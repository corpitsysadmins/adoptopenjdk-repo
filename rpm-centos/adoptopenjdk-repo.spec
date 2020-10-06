%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}

Name:		adoptopenjdk-repo
Version:	0.1
Release:	1.centos7
Summary:	Repo file for AdoptOpenJDK (jfrog.io)

License:	GPL v2 with Classpath Exception
URL:		https://adoptopenjdk.net/installation.html#linux-pkg
Source0:	https://github.com/corpitsysadmins/%{name}/releases/download/%{version}/%{name}-%{version}.tar.gz

BuildArch:	noarch
Requires:	/usr/bin/yum
Provides:	adoptopenjdk-repo
Conflicts:	adoptopenjdk-repo

%description
Configuration files for the AdoptOpenJDK yum repository.

%prep
%setup

%install
mkdir --parents %{buildroot}/etc/yum.repos.d
mv adoptopenjdk.centos.repo %{buildroot}/etc/yum.repos.d/adoptopenjdk.repo

%files
%attr(644, root, root) /etc/yum.repos.d/adoptopenjdk.repo

%changelog
* Mon Sep 5 2020 Irving Leonard <mm-irvingleonard@github.com> 0.1-1
- Initial RPM release
