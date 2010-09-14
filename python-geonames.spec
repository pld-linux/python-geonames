%define 	module	geonames
Summary:	Python wrapper to Geonames webservice
Name:		python-%{module}
Version:	0.1
Release:	1
License:	unknown
Group:		Development/Languages/Python
Source0:	http://download.github.com/gregrobbins-geonames-python-fb6aafd.tar.gz
# Source0-md5:	e92d695d4194155d9d4056a911c53108
URL:		http://github.com/gregrobbins/geonames-python
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This wrapper uses simplejson to simply convert the Geonames data into
python objects.

%prep
%setup -q -n gregrobbins-geonames-python-fb6aafd

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{py_sitescriptdir}

install geonames.py $RPM_BUILD_ROOT%{py_sitescriptdir}

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/geonames.py[co]
