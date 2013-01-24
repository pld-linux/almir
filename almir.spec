Summary:	Bacula web administration written in Pyramid
Name:		almir
Version:	0.1.3
Release:	0.1
License:	GPL v3
Group:		Applications/WWW
Source0:	https://github.com/iElectric/almir/archive/%{version}.tar.gz?/%{name}-%{version}.tgz
# Source0-md5:	7c272ef13c4565b463cddd56a2fe178e
URL:		https://almir.readthedocs.org/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	pythonegg(colander)
Requires:	pythonegg(deform)
Requires:	pythonegg(deform-bootstrap)
Requires:	pythonegg(docutils)
Requires:	pythonegg(mysql-connector-repackaged)
Requires:	pythonegg(pg8000)
Requires:	pythonegg(pyramid)
Requires:	pythonegg(pyramid-beaker)
Requires:	pythonegg(pyramid-exclog)
Requires:	pythonegg(pyramid-jinja2)
Requires:	pythonegg(pyramid-tm)
Requires:	pythonegg(pytz)
Requires:	pythonegg(sqlalchemy)
Requires:	pythonegg(transaction)
Requires:	pythonegg(waitress)
Requires:	pythonegg(webhelpers)
Requires:	pythonegg(zope.sqlalchemy)
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Almir is a bacula web interface for administrators written in Python.
It is designed with simplicity in mind, although backup management is
never simple.

%prep
%setup -q

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{py_sitescriptdir}/almir/tests

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/almir_parse_console_commands
%{py_sitescriptdir}/almir
%{py_sitescriptdir}/almir-%{version}-py*.egg-info
