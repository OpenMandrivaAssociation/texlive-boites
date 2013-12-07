# revision 32235
# category Package
# catalog-ctan /macros/latex/contrib/boites
# catalog-date 2013-11-23 08:21:35 +0100
# catalog-license gpl
# catalog-version 1.1
Name:		texlive-boites
Epoch:		1
Version:	1.1
Release:	3
Summary:	Boxes that may break across pages
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/boites
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boites.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boites.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/boites.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines environments that allow page breaks inside framed boxes
whose edges may be variously fancy. The bundle includes a few
examples (shaded box, box with a wavy line on its side, etc).

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/boites/boites.sty
%{_texmfdistdir}/tex/latex/boites/boites_exemples.sty
%doc %{_texmfdistdir}/doc/latex/boites/Makefile
%doc %{_texmfdistdir}/doc/latex/boites/README
%doc %{_texmfdistdir}/doc/latex/boites/README.docu
%doc %{_texmfdistdir}/doc/latex/boites/boites.pdf
%doc %{_texmfdistdir}/doc/latex/boites/demo.pdf
%doc %{_texmfdistdir}/doc/latex/boites/demo.tex
%doc %{_texmfdistdir}/doc/latex/boites/ligne_qui_ondule_sur_la_gauche.eps
#- source
%doc %{_texmfdistdir}/source/latex/boites/boites.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
