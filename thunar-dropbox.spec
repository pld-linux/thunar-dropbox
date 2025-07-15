# TODO
# - system waf is broken (can't find compiler)
Summary:	Dropbox extension for Thunar
Name:		thunar-dropbox
Version:	0.2.1
Release:	1
Source0:	http://softwarebakery.com/maato/files/thunar-dropbox/%{name}-%{version}.tar.bz2
# Source0-md5:	52bb2caa26afaf80835a56b9ad3d2155
Patch0:		%{name}-thunarx-3.patch
License:	GPL v3+
Group:		X11/Applications
URL:		http://www.softwarebakery.com/maato/thunar-dropbox.html
BuildRequires:	Thunar-devel >= 1.2.0
BuildRequires:	python
BuildRequires:	sed >= 4.0
#BuildRequires:	waf
Requires:	Thunar >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Thunar Dropbox is a plugin for thunar that adds context-menu items
from dropbox.

%prep
%setup -q
%patch -P0 -p1
%{__sed} -i -e 's,${PREFIX}/lib,%{_libdir},' wscript

%build
./waf configure \
	--prefix=%{_prefix}
./waf build

%install
rm -rf $RPM_BUILD_ROOT
rm -rf $RPM_BUILD_ROOT
./waf install \
	--destdir=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -name '*.so' | xargs chmod a+rx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/thunarx-3/thunar-dropbox.so
%{_iconsdir}/hicolor/*/apps/thunar-dropbox.png
