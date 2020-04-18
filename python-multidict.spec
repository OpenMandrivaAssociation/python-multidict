%global modname multidict

Name:           python-%{modname}
Version:        4.7.5
Release:        1
Summary:        MultiDict implementation
License:        ASL 2.0
URL:            https://github.com/aio-libs/multidict
Source0:        %{url}/archive/v%{version}%{?rctag:%{rctag}}/%{modname}-%{version}%{?rctag:%{rctag}}.tar.gz

%global _description \
Multidicts are useful for working with HTTP headers, URL query args etc.\
\
The code was extracted from aiohttp library.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python-setuptools
BuildRequires:  python-cython

%description -n python3-%{modname} %{_description}

%prep
%autosetup -n %{modname}-%{version}%{?rctag:%{rctag}}
sed -i -e '/addopts/d' setup.cfg

%build
%py3_build

%install
%py3_install
rm -vf %{buildroot}%{python3_sitearch}/%{modname}/*.{c,pyx}

%files -n python3-%{modname}
%license LICENSE
%doc README.rst
%{python3_sitearch}/%{modname}-*.egg-info/
%{python3_sitearch}/%{modname}/
