#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	LibXML-Common
Summary:	XML::LibXML::Common Perl module
Summary(cs):	Modul XML::LibXML::Common pro Perl
Summary(da):	Perlmodul XML::LibXML::Common
Summary(de):	XML::LibXML::Common Perl Modul
Summary(es):	Módulo de Perl XML::LibXML::Common
Summary(fr):	Module Perl XML::LibXML::Common
Summary(it):	Modulo di Perl XML::LibXML::Common
Summary(ja):	XML::LibXML::Common Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	XML::LibXML::Common ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul XML::LibXML::Common
Summary(pl):	Modu³ Perla XML::LibXML::Common
Summary(pt):	Módulo de Perl XML::LibXML::Common
Summary(pt_BR):	Módulo Perl XML::LibXML::Common
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl XML::LibXML::Common
Summary(sv):	XML::LibXML::Common Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl XML::LibXML::Common
Summary(zh_CN):	XML::LibXML::Common Perl Ä£¿é
Name:		perl-XML-LibXML-Common
Version:	0.12
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	libxml2-devel >= 2.4.8
BuildRequires:	perl-devel >= 5.6.1
BuildRequires:	rpm-perlprov >= 4.0.2-56
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Requires:	libxml2 >= 2.4.8

%description
XML::LibXML::Common Perl module contains several constants and
functions that are shared by XML::LibXML, XML::GDOME and XML::LibXSLT
(not all done, yet).

%description -l pl
Modu³ Perla XML::LibXML::Common zawiera sta³e oraz funkcje wspólne
dla XML::LibXML, XML::GDOME i XML::LibXSLT (nie zosta³ on jeszcze
skoñczony).

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%dir %{perl_sitearch}/XML/LibXML
%{perl_sitearch}/XML/LibXML/*.pm
%dir %{perl_sitearch}/auto/XML/LibXML
%dir %{perl_sitearch}/auto/XML/LibXML/Common
%{perl_sitearch}/auto/XML/LibXML/Common/Common.bs
%attr(755,root,root) %{perl_sitearch}/auto/XML/LibXML/Common/Common.so
%{_mandir}/man3/*
