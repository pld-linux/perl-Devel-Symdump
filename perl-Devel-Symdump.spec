%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Symdump
Summary:	Devel::Symdump Perl module
Summary(cs):	Modul Devel::Symdump pro Perl
Summary(da):	Perlmodul Devel::Symdump
Summary(de):	Devel::Symdump Perl Modul
Summary(es):	Módulo de Perl Devel::Symdump
Summary(fr):	Module Perl Devel::Symdump
Summary(it):	Modulo di Perl Devel::Symdump
Summary(ja):	Devel::Symdump Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	Devel::Symdump ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul Devel::Symdump
Summary(pl):	Modu³ Perla Devel::Symdump
Summary(pt):	Módulo de Perl Devel::Symdump
Summary(pt_BR):	Módulo Perl Devel::Symdump
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl Devel::Symdump
Summary(sv):	Devel::Symdump Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl Devel::Symdump
Summary(zh_CN):	Devel::Symdump Perl Ä£¿é
Name:		perl-Devel-Symdump
Version:	2.03
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel::Symdump - dump symbol names or the symbol table.

%description -l pl
Modu³ perla Devel::Symdump - zrzucaj±cy symbole lub tablicê symboli.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
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
