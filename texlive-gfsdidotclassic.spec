%global tl_name gfsdidotclassic
%global tl_revision 52778

Name:		texlive-%{tl_name}
Epoch:		1
Version:	001.001
Release:	%{tl_revision}.1
Summary:	The classic version of GFSDidot
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/greek/gfs/gfsdidotclassic
License:	ofl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsdidotclassic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsdidotclassic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
BuildRequires:	texlive-tlpkg
%texlive_base_requires
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The classic version of GFSDidot provided for Unicode TeX engines.

