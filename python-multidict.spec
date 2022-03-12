%global modname multidict

Name:		python-%{modname}
Version:	4.7.5
Release:	2
Summary:	MultiDict implementation
License:	ASL 2.0
URL:		https://github.com/aio-libs/multidict
Source0:	%{url}/archive/v%{version}%{?rctag:%{rctag}}/%{modname}-%{version}%{?rctag:%{rctag}}.tar.gz
BuildRequires:	pkgconfig(python)
BuildRequires:	python-setuptools
BuildRequires:	python-cython
%rename python3-multidict

%description
Multidicts are useful for working with HTTP headers, URL query args etc.
The code was extracted from aiohttp library.

%prep
%autosetup -n %{modname}-%{version}%{?rctag:%{rctag}}
sed -i -e '/addopts/d' setup.cfg

%build
%py_build

%install
%py_install
rm -vf %{buildroot}%{python3_sitearch}/%{modname}/*.{c,pyx}

%files
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{modname}-*.egg-info/
%{python3_sitearch}/%{modname}/
