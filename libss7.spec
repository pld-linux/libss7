Summary:	SS7 protocol services library
Summary(pl.UTF-8):	Biblioteka usług protokołu SS7
Name:		libss7
Version:	2.0.0
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://downloads.asterisk.org/pub/telephony/libss7/%{name}-%{version}.tar.gz
# Source0-md5:	93e43adde507d622fd92898b66f8caef
URL:		http://www.asterisk.org/
BuildRequires:	dahdi-tools-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libss7 is a userspace library that is used for providing SS7 protocol
services to applications. It has a working MTP2, MTP3, and ISUP for
ITU and ANSI style SS7, however it was written in a manner that will
easily allow support for other various national specific variants in
the future.

%description -l pl.UTF-8
libss7 to biblioteka przestrzeni użytkownika, mająca za zadanie
dostarczyć usługi protokołu SS7 dla aplikacji. Zawiera działające
MTP2, MTP3 oraz ISUP dla ITU oraz SS7 wg ANSI, ale została napisana
tak, aby w przyszłości łatwo umożliwić obsługę innych krajowych
wariantów.

%package devel
Summary:	Header files for libss7 library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libss7
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libss7 library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libss7.

%package static
Summary:	libss7 static library
Summary(pl.UTF-8):	Statyczna biblioteka libss7
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libss7 static library.

%description static -l pl.UTF-8
Statyczna biblioteka libss7.

%prep
%setup -q

%build
%{__make} \
	CC="%{__cc}" \
	COVERAGE_CFLAGS="%{rpmcflags} %{rpmcppflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_PREFIX=$RPM_BUILD_ROOT \
	libdir=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog NEWS-* README libss7-%{version}-summary.txt
%attr(755,root,root) %{_libdir}/libss7.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libss7.so
%{_includedir}/libss7.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libss7.a
