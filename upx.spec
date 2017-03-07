Summary:	The Ultimate Packer for eXecutables
Name:		upx
Version:	3.93
Release:	1
License:	GPLv2+
Group:		Archiving/Compression
URL:		https://upx.github.io/
Source0:	https://github.com/upx/upx/releases/download/v%{version}/%{name}-%{version}-src.tar.xz
BuildRequires:	ucl-devel
BuildRequires:	pkgconfig(zlib)

%description
UPX is an advanced executable file compressor. UPX will typically
reduce the file size of programs and DLLs by around 50%-70%, thus
reducing disk space, network load times, download times and other
distribution and storage costs.

Programs and libraries compressed by UPX are completely self-contained
and run exactly as before, with no runtime or memory penalty for most
of the supported formats.

UPX supports a number of different executable formats, including
Win95/98/ME/NT/2000 programs and DLLs, DOS programs, and Linux executables.

UPX is rated number one in the well known Archive Comparison Test. Visit
http://compression.ca/act-exepack.html

%files
%doc BUGS LICENSE NEWS PROJECTS README* THANKS doc/upx.doc doc/upx.html doc/*.txt
%{_bindir}/*
%attr(644,root,man) %{_mandir}/man1/*

#----------------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}-src

%build
%setup_compile_flags

# building the docs
%make -C doc
export UCLDIR=%{_prefix}
%make -C src

%install
install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m 755 src/upx.out %{buildroot}%{_bindir}/upx
install -m 644 doc/upx.1 %{buildroot}%{_mandir}/man1/

