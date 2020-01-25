#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Audio
%define		pnam	Mad
Summary:	Audio::Mad Perl module - interface to the mad MPEG decoder library
Summary(pl.UTF-8):	Moduł Perla Audio::Mad - interfejs do biblioteki dekodera MPEG mad
Name:		perl-Audio-Mad
Version:	0.6
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ede73e114efea0956f8abdb4072fa0bf
URL:		http://search.cpan.org/dist/Audio-Mad/
BuildRequires:	libmad-devel
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio::Mad is a Perl module designed to provide an abstract interface
to the low level mad mpeg decoder library. Interfaces for mad_stream,
mad_frame, mad_synth, and mad_timer_t are provided. Two addon
interfaces Mad::Resample and Mad::Dither provide methods for
manipulating raw mad_fixed_t data into usable strings.

%description -l pl.UTF-8
Audio::Mad to moduł Perla stworzony by udostępnić abstrakcyjny
interfejs do niskopoziomowej biblioteki dekodera MPEG - mad. Dostarcza
interfejsy do mad_stream, mad_frame, mad_synth i mad_timer_t. Dwa
dodatkowe interfejsy Mad::Resample i Mad::Dither udostępniają metody
do przekształcania surowych danych mad_fixed_t na użyteczne ciągi.

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
%{perl_vendorarch}/Audio/Mad.pm
%{perl_vendorarch}/Audio/Mad
%dir %{perl_vendorarch}/auto/Audio/Mad
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/Mad/*.so
%{_mandir}/man3/*
