%define octpkg vrml

Summary:	3D graphics using VRML
Name:		octave-%{octpkg}
Version:	1.0.13
Release:	1
Source0:	http://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
License:	GPLv3+ and GFDL
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/
BuildArch:	noarch

BuildRequires:	octave-devel >= 2.9.7

Requires:	octave(api) = %{octave_api}
Requires:	octave-linear-algebra
Requires:	octave-miscellaneous
Requires:	octave-struct
Requires:	octave-statistics

Requires(post): octave
Requires(postun): octave

%description
3D graphics using VRML.

This package is part of community Octave-Forge collection.

%prep
%setup -qcT

%build
%octave_pkg_build -T

%install
%octave_pkg_install

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

%files
%dir %{octpkgdir}
%{octpkgdir}/*
%doc %{octpkg}/NEWS
%doc %{octpkg}/COPYING

