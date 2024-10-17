Name:    python-lightblue
Version: 0.4
Release: 4
Summary: A cross-platform Python Bluetooth API
Group:   Development/Python
License:   GPLv3
URL:       https://lightblue.sourceforge.net
Source0: lightblue-%{version}.tar.gz
BuildRequires: python-devel
BuildRequires: python-pybluez
BuildRequires: openobex
BuildRequires: pkgconfig(bluez)
BuildRequires: libopenobex-devel


%description
LightBlue is a cross-platform Bluetooth API for Python which provides simple
access to Bluetooth operations.

%prep
%setup -q -n lightblue-%{version}

%build
python setup.py build

%install
python setup.py install --root=%{buildroot}

%files
%{py_platsitedir}/lightblue
%{py_platsitedir}/_lightblueobex.so
%{py_platsitedir}/_lightblueutil.so
%{py_platsitedir}/*.egg-info


%changelog
* Fri Oct 29 2010 Michael Scherer <misc@mandriva.org> 0.4-2mdv2011.0
+ Revision: 590005
- rebuild for python 2.7

* Tue Jul 27 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 0.4-1mdv2011.0
+ Revision: 561920
- import python-lightblue


