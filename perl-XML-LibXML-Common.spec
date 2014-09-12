#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	XML
%define		pnam	LibXML-Common
Summary:	XML::LibXML::Common - routines and constants common for XML::LibXML and XML::GDOME
Summary(pl.UTF-8):	XML::LibXML::Common - procedury i stałe wspólne dla XML::LibXML i XML::GDOME
Name:		perl-XML-LibXML-Common
Version:	0.13
Release:	7
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/XML/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	13b6d93f53375d15fd11922216249659
URL:		http://search.cpan.org/dist/XML-LibXML-Common/
BuildRequires:	libxml2-devel >= 2.4.8
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	libxml2 >= 2.4.8
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
	CC="%{__cc}" \
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
%attr(755,root,root) %{perl_vendorarch}/auto/XML/LibXML/Common/Common.so
%{_mandir}/man3/*
