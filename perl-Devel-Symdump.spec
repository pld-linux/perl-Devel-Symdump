%include	/usr/lib/rpm/macros.perl
%define	pdir	Devel
%define	pnam	Symdump
Summary:	Devel::Symdump Perl module
Summary(cs):	Modul Devel::Symdump pro Perl
Summary(da):	Perlmodul Devel::Symdump
Summary(de):	Devel::Symdump Perl Modul
Summary(es):	M�dulo de Perl Devel::Symdump
Summary(fr):	Module Perl Devel::Symdump
Summary(it):	Modulo di Perl Devel::Symdump
Summary(ja):	Devel::Symdump Perl �⥸�塼��
Summary(ko):	Devel::Symdump �� ����
Summary(no):	Perlmodul Devel::Symdump
Summary(pl):	Modu� Perla Devel::Symdump
Summary(pt):	M�dulo de Perl Devel::Symdump
Summary(pt_BR):	M�dulo Perl Devel::Symdump
Summary(ru):	������ ��� Perl Devel::Symdump
Summary(sv):	Devel::Symdump Perlmodul
Summary(uk):	������ ��� Perl Devel::Symdump
Summary(zh_CN):	Devel::Symdump Perl ģ��
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
Modu� perla Devel::Symdump - zrzucaj�cy symbole lub tablic� symboli.

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
