Summary:	A language for typesetting graphs
Summary(pl):	J�zyk do sk�adu graf�w
Name:		grap
Version:	1.30
Release:	1
License:	BSD
Group:		Applications/Publishing
Source0:	http://www.lunabase.org/~faber/Vault/software/grap/%{name}-%{version}.tar.gz
# Source0-md5:	f84c99b1746a963328f38d050529b778
Patch0:		%{name}-debian.patch
URL:		http://www.lunabase.org/~faber/Vault/software/grap/
BuildRequires:	autoconf
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Grap is a language for typesetting graphs specified and first
implemented by Brian Kernighan and Jon Bentley at Bell Labs. It is an
expressive language for describing graphs and incorporating them in
typeset documents. It is implemented as a preprocessor to Kernighan's
pic language for describing languages, so any system that can use pic
can use grap. For sure, TeX and groff can use it.

%description -l pl
Grap to j�zyk do sk�adu graf�w zdefiniowany i po raz pierwszy
zaimplementowany przez Briana Kernighana i Jona Bentleya w Bell Labs.
Jest to j�zyk wyra�e� do opisu graf�w i w��czania ich do sk�adanych
dokument�w. Jest zaimplementowany jako preprocesor dla j�zyka pic
Kernighana s�u��cego do opisu j�zyk�w, wi�c dowolny system u�ywaj�cy
j�zyka pic mo�e u�ywa� j�zyka grap. Na pewno mog� go u�ywa� TeX i
groff.

%prep
%setup -q
%patch0 -p1

%build
%{__autoconf}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	DEFINESDIR=$RPM_BUILD_ROOT%{_datadir}/misc \
	DOCDIR=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
	MANDIR=RPM_BUILD_ROOT%{_mandir}/man1 \
	EXAMPLEDIR=RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/misc/*
