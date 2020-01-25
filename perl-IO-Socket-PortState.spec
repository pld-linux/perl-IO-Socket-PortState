#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	IO
%define		pnam	Socket-PortState
Summary:	IO::Socket::PortState - Perl extension for checking the open or closed status of a port.
Name:		perl-IO-Socket-PortState
Version:	0.03
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/IO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ba82446a68380e8bd79ab49a5948d6c1
URL:		http://search.cpan.org/dist/IO-Socket-PortState/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
You can use it to check if a port is open or closed for a given host and protocol.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/IO/Socket/PortState.pm
%{_mandir}/man3/*
