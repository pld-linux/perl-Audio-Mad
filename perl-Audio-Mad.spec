#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	Mad
Summary:	Audio::Mad Perl module - interface to the mad MPEG decoder library
Summary(pl):	Modu³ Perla Audio::Mad - interfejs do biblioteki dekodera MPEG mad
Name:		perl-Audio-Mad
Version:	0.6
Release:	1
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ede73e114efea0956f8abdb4072fa0bf
BuildRequires:	libmad-devel
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Audio::Mad is a Perl module designed to provide an abstract interface
to the low level mad mpeg decoder library. Interfaces for mad_stream,
mad_frame, mad_synth, and mad_timer_t are provided. Two addon
interfaces Mad::Resample and Mad::Dither provide methods for
manipulating raw mad_fixed_t data into usable strings.

%description -l pl
Audio::Mad to modu³ Perla stworzony by udostêpniæ abstrakcyjny
interfejs do niskopoziomowej biblioteki dekodera MPEG - mad. Dostarcza
interfejsy do mad_stream, mad_frame, mad_synth i mad_timer_t. Dwa
dodatkowe interfejsy Mad::Resample i Mad::Dither udostêpniaj± metody
do przekszta³cania surowych danych mad_fixed_t na u¿yteczne ci±gi.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} OPTIMIZE="%{rpmcflags}"

%{!?_without_tests:%{__make} test}

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
%{perl_vendorarch}/auto/Audio/Mad/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Audio/Mad/*.so
%{_mandir}/man3/*
