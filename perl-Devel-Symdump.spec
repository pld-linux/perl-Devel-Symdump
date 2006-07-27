#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Devel
%define		pnam	Symdump
Summary:	Devel::Symdump - dump symbol names or the symbol table
Summary(pl):	Devel::Symdump - zrzucanie nazw symboli lub tablicy symboli
Name:		perl-Devel-Symdump
Version:	2.0602
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	53c2b6aefd3e805970c84e33ce6655b7
URL:		http://search.cpan.org/dist/Devel-Symdump/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Pod-Coverage
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This little package serves to access the symbol table of perl. It
dumps symbol names or the symbol table.

%description -l pl
Ten niewielki pakiet s³u¿y do dostêpu do tablicy symboli Perla.
Pobiera on nazwy symboli lub tablicê symboli.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_vendorlib}/Devel/Symdump.pm
%{perl_vendorlib}/Devel/Symdump
%{_mandir}/man3/*
