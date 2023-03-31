Name:		texlive-gfsdidotclassic
Version:	52778
Release:	2
Summary:	The classic version of GFSDidot
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gfsdidotclassic
License:	ofl
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsdidotclassic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gfsdidotclassic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The classic version of GFSDidot provided for Unicode TeX
engines.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/fonts/opentype/public/gfsdidotclassic
%doc %{_texmfdistdir}/doc/fonts/gfsdidotclassic

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
