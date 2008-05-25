Summary:	A language for typesetting graphs
Summary(pl.UTF-8):	Język do składu grafów
Name:		grap
Version:	1.41
Release:	1
License:	BSD
Group:		Applications/Publishing
Source0:	http://www.lunabase.org/~faber/Vault/software/grap/%{name}-%{version}.tar.gz
# Source0-md5:	e5c105a50669016f66bcc1517783ef67
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

%description -l pl.UTF-8
Grap to język do składu grafów zdefiniowany i po raz pierwszy
zaimplementowany przez Briana Kernighana i Jona Bentleya w Bell Labs.
Jest to język wyrażeń do opisu grafów i włączania ich do składanych
dokumentów. Jest zaimplementowany jako preprocesor dla języka pic
Kernighana służącego do opisu języków, więc dowolny system używający
języka pic może używać języka grap. Na pewno mogą go używać TeX i
groff.

%prep
%setup -q

%build
%{__autoconf}
CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	DEFINESDIR=$RPM_BUILD_ROOT%{_datadir}/grap \
	DOCDIR=$RPM_BUILD_ROOT%{_docdir}/%{name}-%{version} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	EXAMPLEDIR=$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/grap
%{_mandir}/man1/grap*
%{_examplesdir}/%{name}-%{version}
