%global octpkg vrml

Summary:	3D graphics using VRML
Name:		octave-vrml
Version:	1.0.13
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/vrml/
Source0:	https://downloads.sourceforge.net/octave/vrml-%{version}.tar.gz

BuildRequires:  octave-devel >= 2.9.7
BuildRequires:  octave-linear-algebra
BuildRequires:  octave-miscellaneous
BuildRequires:  octave-struct
BuildRequires:  octave-statistics

Requires:	octave(api) = %{octave_api}
Requires:  	octave-linear-algebra
Requires:  	octave-miscellaneous
Requires:  	octave-struct
Requires:  	octave-statistics

Requires(post): octave
Requires(postun): octave

BuildArch:	noarch

%description
3D graphics using VRML.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}

%build
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

