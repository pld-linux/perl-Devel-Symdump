%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Symdump
Summary:	Devel::Symdump perl module
Summary(pl):	Modu� perla Devel::Symdump
Name:		perl-Devel-Symdump
Version:	2.03
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Symdump - dump symbol names or the symbol table.

%description -l pl
Modu� perla Devel::Symdump - zrzucaj�cy symbole lub tablic� symboli.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%{perl_sitelib}/Devel/Symdump.pm
%{perl_sitelib}/Devel/Symdump
%{_mandir}/man3/*
