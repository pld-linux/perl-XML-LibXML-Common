#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	LibXML-Common
Summary:	XML::LibXML::Common Perl module
Summary(cs.UTF-8):	Modul XML::LibXML::Common pro Perl
Summary(da.UTF-8):	Perlmodul XML::LibXML::Common
Summary(de.UTF-8):	XML::LibXML::Common Perl Modul
Summary(es.UTF-8):	Módulo de Perl XML::LibXML::Common
Summary(fr.UTF-8):	Module Perl XML::LibXML::Common
Summary(it.UTF-8):	Modulo di Perl XML::LibXML::Common
Summary(ja.UTF-8):	XML::LibXML::Common Perl モジュール
Summary(ko.UTF-8):	XML::LibXML::Common 펄 모줄
Summary(nb.UTF-8):	Perlmodul XML::LibXML::Common
Summary(pl.UTF-8):	Moduł Perla XML::LibXML::Common
Summary(pt.UTF-8):	Módulo de Perl XML::LibXML::Common
Summary(pt_BR.UTF-8):	Módulo Perl XML::LibXML::Common
Summary(ru.UTF-8):	Модуль для Perl XML::LibXML::Common
Summary(sv.UTF-8):	XML::LibXML::Common Perlmodul
Summary(uk.UTF-8):	Модуль для Perl XML::LibXML::Common
Summary(zh_CN.UTF-8):	XML::LibXML::Common Perl 模块
Name:		perl-XML-LibXML-Common
Version:	0.13
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	13b6d93f53375d15fd11922216249659
BuildRequires:	libxml2-devel >= 2.4.8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	libxml2 >= 2.4.8

%description
XML::LibXML::Common Perl module contains several constants and
functions that are shared by XML::LibXML, XML::GDOME and XML::LibXSLT
(not all done, yet).

%description -l pl.UTF-8
Moduł Perla XML::LibXML::Common zawiera stałe oraz funkcje wspólne
dla XML::LibXML, XML::GDOME i XML::LibXSLT (nie został on jeszcze
skończony).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_vendorarch}/XML/LibXML
%{perl_vendorarch}/XML/LibXML/*.pm
%dir %{perl_vendorarch}/auto/XML/LibXML
%dir %{perl_vendorarch}/auto/XML/LibXML/Common
%{perl_vendorarch}/auto/XML/LibXML/Common/Common.bs
%attr(755,root,root) %{perl_vendorarch}/auto/XML/LibXML/Common/Common.so
%{_mandir}/man3/*
