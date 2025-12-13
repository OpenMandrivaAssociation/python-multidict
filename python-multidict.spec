%global modname multidict

Name:		python-%{modname}
Version:	6.7.0
Release:	1
Summary:	MultiDict implementation
License:	ASL 2.0
URL:		https://github.com/aio-libs/multidict
Source0:	%{url}/archive/v%{version}%{?rctag:%{rctag}}/%{modname}-%{version}%{?rctag:%{rctag}}.tar.gz
BuildSystem:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(cython)
%rename python3-multidict

%description
Multidicts are useful for working with HTTP headers, URL query args etc.
The code was extracted from aiohttp library.

%prep -a

%install -a
rm -vf %{buildroot}%{python_sitearch}/%{modname}/*.{c,pyx}

%files
%license LICENSE
%doc README.rst
%{python_sitearch}/%{modname}-%{version}.dist-info
%{python_sitearch}/%{modname}/
