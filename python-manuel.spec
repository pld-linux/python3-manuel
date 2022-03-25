#
# Conditional build:
%bcond_without	tests	# unit tests
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Building tested documentation
Summary(pl.UTF-8):	Budowanie przetestowanej dokumentacji
Name:		python-manuel
Version:	1.10.1
Release:	2
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/manuel/
Source0:	https://files.pythonhosted.org/packages/source/m/manuel/manuel-%{version}.tar.gz
# Source0-md5:	5f481f0644df718f6154728444f0eb7d
URL:		https://pypi.org/project/manuel/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-six
BuildRequires:	python-zope.testing
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-six
BuildRequires:	python3-zope.testing
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manuel lets you build tested documentation.

%description -l pl.UTF-8
Manuel pozwala budować przetestowaną dokumentację.

%package -n python3-manuel
Summary:	Building tested documentation
Summary(pl.UTF-8):	Budowanie przetestowanej dokumentacji
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-manuel
Manuel lets you build tested documentation.

%description -n python3-manuel -l pl.UTF-8
Manuel pozwala budować przetestowaną dokumentację.

%package apidocs
Summary:	API documentation for Python manuel module
Summary(pl.UTF-8):	Dokumentacja API modułu Pythona manuel
Group:		Documentation

%description apidocs
API documentation for Python manuel module.

%description apidocs -l pl.UTF-8
Dokumentacja API modułu Pythona manuel.

%prep
%setup -q -n manuel-%{version}

%build
%if %{with python2}
%py_build %{?with_tests:test}
%endif

%if %{with python3}
%py3_build %{?with_tests:test}
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.rst README.rst
%{py_sitescriptdir}/manuel
%{py_sitescriptdir}/manuel-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-manuel
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.rst README.rst
%{py3_sitescriptdir}/manuel
%{py3_sitescriptdir}/manuel-%{version}-py*.egg-info
%endif
