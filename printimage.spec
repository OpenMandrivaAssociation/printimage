%undefine _debugsource_packages

Name: printimage
Version: 0.0
Release: 1
Source0: https://gist.githubusercontent.com/jart/7428b2b955dfd6eff7b6d31e00414508/raw/64de3169b0445e4deb7e729e67a92b5709790d5b/printimage.c
Summary: Tool to convert an image to ASCII and "print" it in a terminal
URL: https://justine.lol/printimage.html
License: Unlicense
Group: Graphics
Requires: imagemagick

%description
Tool to convert an image to ASCII and "print" it in a terminal

%build
%{__cc} %{build_cflags} -o printimage %{S:0}

%install
mkdir -p %{buildroot}%{_bindir}
mv printimage %{buildroot}%{_bindir}/

%files
%{_bindir}/printimage
