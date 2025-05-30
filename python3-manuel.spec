#
# Conditional build:
%bcond_without	doc	# Sphinx documentation
%bcond_without	tests	# unit tests

Summary:	Building tested documentation
Summary(pl.UTF-8):	Budowanie przetestowanej dokumentacji
Name:		python3-manuel
Version:	1.13.0
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/manuel/
Source0:	https://files.pythonhosted.org/packages/source/m/manuel/manuel-%{version}.tar.gz
# Source0-md5:	42caa321f5244b6ec38da5b9bc440d94
Patch0:		manuel-escape.patch
URL:		https://pypi.org/project/manuel/
BuildRequires:	python3-modules >= 1:3.7
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-zope.testing
%endif
%if %{with doc}
BuildRequires:	python3-myst_parser
BuildRequires:	python3-sphinx_copybutton
BuildRequires:	sphinx-pdg-3
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Manuel lets you build tested documentation.

%description -l pl.UTF-8
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
%patch -P0 -p1

%build
%py3_build

%if %{with tests}
PYTHONPATH=$(pwd)/src \
%{__python3} -c '__import__("manuel.tests").tests.test_suite()'
%endif

%if %{with doc}
sphinx-build-3 -b html -c sphinx src/manuel sphinx/_build/html
%endif

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES.rst COPYRIGHT.rst README.rst
%{py3_sitescriptdir}/manuel
%{py3_sitescriptdir}/manuel-%{version}-py*.egg-info

%if %{with doc}
%files apidocs
%defattr(644,root,root,755)
%doc sphinx/_build/html/{_static,*.html,*.js}
%endif
