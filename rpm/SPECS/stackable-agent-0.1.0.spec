BuildRequires: systemd-rpm-macros

Name:       stackable-agent
Version:    0.1.0
Release:    1%{?dist}
Summary:    Binarius package

Group:      System Environment/Base
License:    GPLv3+
Source0:    stackable-agent-0.1.0.tar.gz

%description
Testing package.

%prep
%setup -q #unpack tarball

%build

%install
cp -rfa * %{buildroot}

%post
%systemd_post %{pkgname}.service
    /usr/bin/systemctl daemon-reload
    /usr/bin/systemctl start %{pkgname}.service


%files
/*