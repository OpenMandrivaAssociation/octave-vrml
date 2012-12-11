%define	pkgname vrml
%define name	octave-%{pkgname}
%define version 1.0.11

Summary:	VRML graphics for Octave
Name:		%{name}
Version:	%{version}
Release:        2
Source0:	%{pkgname}-%{version}.tar.gz
License:	GPLv2+
Group:		Sciences/Mathematics
Url:		http://octave.sourceforge.net/vrml/
Conflicts:	octave-forge <= 20090607
Requires:	octave >= 2.9.7, octave-miscellaneous >= 0.0.0
Requires:	octave-struct >= 0.0.0, octave-statistics >= 0.0.0
BuildRequires:  octave-devel >= 2.9.9
BuildRequires:  mesagl-devel
BuildRequires:  mesaglu-devel
BuildArch:	noarch

%description
VRML graphics for Octave.

%prep
%setup -q -c %{pkgname}-%{version}
cp %SOURCE0 .

%install
%__install -m 755 -d %{buildroot}%{_datadir}/octave/packages/
export OCT_PREFIX=%{buildroot}%{_datadir}/octave/packages
octave -q --eval "pkg prefix $OCT_PREFIX; pkg install -verbose -nodeps -local %{pkgname}-%{version}.tar.gz"

tar zxf %SOURCE0 
mv %{pkgname}/COPYING .
mv %{pkgname}/DESCRIPTION .

find %{buildroot} -name .svn | xargs rm -rf 

%clean

%post
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%postun
%{_bindir}/test -x %{_bindir}/octave && %{_bindir}/octave -q -H --no-site-file --eval "pkg('rebuild');" || :

%files
%defattr(-,root,root)
%doc COPYING DESCRIPTION
%{_datadir}/octave/packages/%{pkgname}-%{version}



%changelog
* Sun Aug 21 2011 Lev Givon <lev@mandriva.org> 1.0.11-1mdv2012.0
+ Revision: 696039
- import octave-vrml


