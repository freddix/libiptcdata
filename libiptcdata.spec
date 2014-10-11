Summary:	Library for IPTC metadata manipulation
Name:		libiptcdata
Version:	1.0.4
Release:	5
License:	GPL v2
Group:		Libraries
Source0:	http://download.sourceforge.net/libiptcdata/%{name}-%{version}.tar.gz
# Source0-md5:	af886556ecb129b694f2d365d03d95a8
URL:		http://libiptcdata.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libiptcdata is a library, written in C, for manipulating the
International Press Telecommunications Council (IPTC) metadata stored
within multimedia files such as images. This metadata can include
captions and keywords, often used by popular photo management
applications. The library provides routines for parsing, viewing,
modifying, and saving this metadata.

%package devel
Summary:	Header files for libiptcdata library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libiptcdata library.

%package apidocs
Summary:	libiptcdata API documentation
Group:		Documentation
Requires:	gtk-doc-common

%description apidocs
libiptcdata API documentation.

%prep
%setup -q

%build
%{__gtkdocize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /usr/sbin/ldconfig
%postun	-p /usr/sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %ghost %{_libdir}/lib*.so.?
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_includedir}/libiptcdata
%{_pkgconfigdir}/*.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/libiptcdata

