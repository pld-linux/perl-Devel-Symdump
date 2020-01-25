#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Devel
%define		pnam	Symdump
Summary:	Devel::Symdump - dump symbol names or the symbol table
Summary(pl.UTF-8):	Devel::Symdump - zrzucanie nazw symboli lub tablicy symboli
Name:		perl-Devel-Symdump
Version:	2.18
Release:	1
Epoch:		1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Devel/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	3dd7e1c7779a37c31a3eb60c0a97ea9f
URL:		http://search.cpan.org/dist/Devel-Symdump/
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.45_02
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Compress-Zlib
BuildRequires:	perl-Test-Pod-Coverage
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This little package serves to access the symbol table of perl. It
dumps symbol names or the symbol table.

%description -l pl.UTF-8
Ten niewielki pakiet służy do dostępu do tablicy symboli Perla.
Pobiera on nazwy symboli lub tablicę symboli.

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
%doc Changes
%{perl_vendorlib}/Devel/Symdump.pm
%{perl_vendorlib}/Devel/Symdump
%{_mandir}/man3/Devel::Symdump.3pm*
