%define __spec_install_post %{nil}
%define __os_install_post %{_dbpath}/brp-compress
%define debug_package %{nil}
#BuildRequires: systemd-rpm-macros

Name: stackable-agent
Summary: An Agent to orchestrate a big data tools
Version: @@VERSION@@
Release: @@RELEASE@@%{?dist}
License: ASL 2.0
Group: Applications/System
Source0: %{name}-%{version}.tar.gz

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

%description
%{summary}

%prep
%setup -q

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}
cp -a * %{buildroot}
#ls -al %{buildroot}
cp -a %{buildroot}
#install -m 0755 %{name} /opt/stackable-agent-<version>/agent

#%post
#%systemd_post stackable-agent.service
#    /usr/bin/systemctl daemon-reload

%clean
rm -rf %{buildroot}

%files
#/etc/stackableagent/agent.conf
#/etc/systemd/system/stackable-agent.service


#%defattr(file mode, user, group, dir mode)
#The %defattr directive allows setting of default attributes for files and directives.
#The default permissions, or "mode" for files.
#The default user id.
#The default group id.
#The default permissions, or "mode" for directories.

%defattr(-,root,root,-)
#/src/bin/*