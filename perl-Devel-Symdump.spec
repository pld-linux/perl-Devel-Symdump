%include	/usr/lib/rpm/macros.perl
Summary:	Devel-Symdump perl module
Summary(pl):	Modu� perla Devel-Symdump
Name:		perl-Devel-Symdump
Version:	2.00
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Devel/Devel-Symdump-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Devel-Symdump - dump symbol names or the symbol table.

%description -l pl
Modu� perla Devel-Symdump.

%prep
%setup -q -n Devel-Symdump-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Devel/Symdump
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/Devel/Symdump.pm
%{perl_sitelib}/Devel/Symdump
%{perl_sitearch}/auto/Devel/Symdump

%{_mandir}/man3/*
