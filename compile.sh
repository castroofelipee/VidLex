#!/bin/bash

set -e  

EXECUTABLE_NAME="VidLex"
MAIN_SCRIPT="src/main.py"
DIST_DIR="dist"

if [ ! -f "$MAIN_SCRIPT" ]; then
    echo "Script file '$MAIN_SCRIPT' does not exist."
    exit 1
fi

pyinstaller --onefile --noconsole --icon=src/assets/images/logo.png --name $EXECUTABLE_NAME $MAIN_SCRIPT

rm -rf build
rm -rf __pycache__
rm -rf *.spec

echo "Conteúdo da pasta dist:"
ls $DIST_DIR

DEBIAN_DIR="debian"
mkdir -p $DEBIAN_DIR/usr/local/bin
mkdir -p $DEBIAN_DIR/usr/local/share/VidLex
mkdir -p $DEBIAN_DIR/usr/local/share/applications

if [ -f "$DIST_DIR/$EXECUTABLE_NAME" ]; then
    cp $DIST_DIR/$EXECUTABLE_NAME $DEBIAN_DIR/usr/local/bin/
else
    echo "Arquivo executável não encontrado em '$DIST_DIR/$EXECUTABLE_NAME'."
    exit 1
fi

cp -r src/assets $DEBIAN_DIR/usr/local/share/VidLex/
cp requirements.txt $DEBIAN_DIR/usr/local/share/VidLex/

cat <<EOF > $DEBIAN_DIR/usr/local/share/applications/VidLex.desktop
[Desktop Entry]
Name=VidLex
Comment=VidLex Application
Exec=/usr/local/bin/VidLex
Icon=/usr/local/share/VidLex/assets/images/logo.png
Terminal=false
Type=Application
Categories=Utility;Application;
EOF

dpkg-deb --build $DEBIAN_DIR vidlex_1.0.0_all.deb


RPM_DIR="rpm"
mkdir -p $RPM_DIR/usr/local/bin
mkdir -p $RPM_DIR/usr/local/share/VidLex
mkdir -p $RPM_DIR/usr/local/share/applications

if [ -f "$DIST_DIR/$EXECUTABLE_NAME" ]; then
    cp $DIST_DIR/$EXECUTABLE_NAME $RPM_DIR/usr/local/bin/
else
    echo "Arquivo executável não encontrado em '$DIST_DIR/$EXECUTABLE_NAME'."
    exit 1
fi

cp -r src/assets $RPM_DIR/usr/local/share/VidLex/
cp requirements.txt $RPM_DIR/usr/local/share/VidLex/

cat <<EOF > vidlex.spec
Name: VidLex
Version: 1.0.0
Release: 1%{?dist}
Summary: VidLex - A versatile application for various tasks

License: MIT
URL: https://github.com/castroofelipee/VidLex
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

cp %{_sourcedir}/$EXECUTABLE_NAME %{buildroot}/usr/local/bin/
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
* Thu Jun 15 2024 Felipe Castro <castroofelipee19@gmail.com> - 1.0.0-1
- Initial package
EOF

tar -czvf VidLex-1.0.0.tar.gz -C $RPM_DIR .
rpmbuild -ta VidLex-1.0.0.tar.gz


rm -rf $DIST_DIR
rm -rf $DEBIAN_DIR
rm -rf $RPM_DIR
rm VidLex-1.0.0.tar.gz

mkdir -p ~/.local/bin
mkdir -p ~/.local/share/applications

cp $DIST_DIR/$EXECUTABLE_NAME ~/.local/bin/
cat <<EOF > ~/.local/share/applications/VidLex.desktop
[Desktop Entry]
Name=VidLex
Comment=VidLex Application
Exec=$HOME/.local/bin/VidLex
Icon=$HOME/.local/share/VidLex/assets/images/logo.png
Terminal=false
Type=Application
Categories=Utility;Application;
EOF

cp -r src/assets ~/.local/share/VidLex/
echo "O executável foi copiado para ~/.local/bin e a entrada do aplicativo foi criada em ~/.local/share/applications"

echo "ready"
