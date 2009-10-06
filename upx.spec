Summary:	The Ultimate Packer for eXecutables
Name:		upx
Version:	3.03
Release:	%mkrel 3
License:	GPL
Group:		Archiving/Compression
URL:		http://upx.sourceforge.net/
Source0:	http://upx.sourceforge.net/download/%{name}-%{version}-src.tar.bz2
Patch0:		upx-3.03-src-format_not_a_string_literal_and_no_format_arguments.diff
BuildRequires:	libucl-devel >= 1.03
BuildRequires:	zlib-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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

%prep

%setup -q -n %{name}-%{version}-src
%patch0 -p0

%build
# building the docs
%make -C doc
export UCLDIR=%{_prefix}
%make -C src CXXFLAGS="%{optflags} -Wcast-align -Wcast-qual -Wpointer-arith -Wwrite-strings"

%install
rm -rf %{buildroot}

install -d %{buildroot}%{_bindir}
install -d %{buildroot}%{_mandir}/man1

install -m 755 src/upx.out %{buildroot}%{_bindir}/upx
install -m 644 doc/upx.1 %{buildroot}%{_mandir}/man1/

%clean
rm -rf %{buildroot}

%files
%defattr (-,root,root)
%doc BUGS LICENSE NEWS PROJECTS README* THANKS doc/upx.doc doc/upx.html doc/*.txt
%{_bindir}/*
%attr(644,root,man) %{_mandir}/man1/*


