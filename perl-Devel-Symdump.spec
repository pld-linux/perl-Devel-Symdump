%define	pdir	Devel
%define	pnam	Symdump
%include	/usr/lib/rpm/macros.perl
Summary:	Devel-Symdump perl module
Summary(pl):	Modu³ perla Devel-Symdump
Name:		perl-Devel-Symdump
Version:	2.01
Release:	7

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel-Symdump - dump symbol names or the symbol table.

%description -l pl
Modu³ perla Devel-Symdump.

%prep
%setup -q -n Devel-Symdump-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf ChangeLog README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Devel/Symdump.pm
%{perl_sitelib}/Devel/Symdump
%{_mandir}/man3/*
