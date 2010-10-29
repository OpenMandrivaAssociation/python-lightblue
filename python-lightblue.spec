Name:    python-lightblue
Version: 0.4
Release: %mkrel 2

Summary: A cross-platform Python Bluetooth API
Group:   Development/Python

License:   GPLv3
URL:       http://lightblue.sourceforge.net
BuildRoot: %{_tmppath}/%{name}-%{version}-buildroot

Source0: lightblue-%{version}.tar.gz

BuildRequires: python-devel
BuildRequires: python-pybluez
BuildRequires: openobex
BuildRequires: libbluez-devel
BuildRequires: libopenobex-devel


%description
LightBlue is a cross-platform Bluetooth API for Python which provides simple
access to Bluetooth operations.

%prep
%setup -q -n lightblue-%{version}

%build
python setup.py build

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{py_platsitedir}/lightblue
%{py_platsitedir}/_lightblueobex.so
%{py_platsitedir}/_lightblueutil.so
%{py_platsitedir}/*.egg-info
