Name: VidLex
Version: 1.0.0
Release: 1%{?dist}
Summary: VidLex - A versatile application for various tasks

License: MIT
URL: https://github.com/yourusername/my_project
Source0: %{name}-%{version}.tar.gz

BuildArch: noarch
Requires: python3, python3-pip

%description
VidLex is a versatile application for various tasks.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/usr/local/share/VidLex
mkdir -p %{buildroot}/usr/local/share/applications

cp %{_sourcedir}/VidLex %{buildroot}/usr/local/bin/
cp -r %{_sourcedir}/src/assets %{buildroot}/usr/local/share/VidLex/
cp %{_sourcedir}/requirements.txt %{buildroot}/usr/local/share/VidLex/
cat << DESKTOP > %{buildroot}/usr/local/share/applications/VidLex.desktop
[Desktop Entry]
Name=VidLex
Comment=VidLex Application
Exec=/usr/local/bin/VidLex
Icon=/usr/local/share/VidLex/assets/images/logo.png
Terminal=false
Type=Application
Categories=Utility;Application;
DESKTOP

%files
/usr/local/bin/VidLex
/usr/local/share/VidLex
/usr/local/share/applications/VidLex.desktop

%post
pip3 install -r /usr/local/share/VidLex/requirements.txt
chmod +x /usr/local/bin/VidLex

%changelog
* Thu Jun 15 2024 Your Name <your.email@example.com> - 1.0.0-1
- Initial package
