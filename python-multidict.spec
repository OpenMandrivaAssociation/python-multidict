%define module multidict

Name:		python-multidict
Version:	6.7.1
Release:	1
Summary:	MultiDict implementation
License:	Apache-2.0
Group:		Development/Python
URL:		https://github.com/aio-libs/multidict
Source0:	%{URL}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildSystem:	python
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(cython)
%rename python3-multidict

%description
Multidicts are useful for working with HTTP headers, URL query args etc.
The code was extracted from aiohttp library.

%build -p
export LDFLAGS="%{ldflags} -lpython%{py_ver}"

%install -a
rm -vf %{buildroot}%{python_sitearch}/%{module}/*.{c,pyx}

%files
%doc README.rst
%license LICENSE
%{python_sitearch}/%{module}
%{python_sitearch}/%{module}-%{version}.dist-info
