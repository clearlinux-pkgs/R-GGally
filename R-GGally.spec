#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-GGally
Version  : 1.5.0
Release  : 29
URL      : https://cran.r-project.org/src/contrib/GGally_1.5.0.tar.gz
Source0  : https://cran.r-project.org/src/contrib/GGally_1.5.0.tar.gz
Summary  : Extension to 'ggplot2'
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RColorBrewer
Requires: R-ggplot2
Requires: R-gtable
Requires: R-plyr
Requires: R-progress
Requires: R-reshape
Requires: R-rlang
BuildRequires : R-RColorBrewer
BuildRequires : R-ggplot2
BuildRequires : R-gtable
BuildRequires : R-plyr
BuildRequires : R-progress
BuildRequires : R-reshape
BuildRequires : R-rlang
BuildRequires : buildreq-R

%description
The R package 'ggplot2' is a plotting system based on the grammar of graphics.
    'GGally' extends 'ggplot2' by adding several functions
    to reduce the complexity of combining geometric objects with transformed data.
    Some of these functions include a pairwise plot matrix, a two group pairwise plot
    matrix, a parallel coordinates plot, a survival plot, and several functions to
    plot networks.

%prep
%setup -q -c -n GGally
cd %{_builddir}/GGally

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1589762058

%install
export SOURCE_DATE_EPOCH=1589762058
rm -rf %{buildroot}
export LANG=C.UTF-8
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$FFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library GGally
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library GGally
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library GGally
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc GGally || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/GGally/DESCRIPTION
/usr/lib64/R/library/GGally/INDEX
/usr/lib64/R/library/GGally/Meta/Rd.rds
/usr/lib64/R/library/GGally/Meta/data.rds
/usr/lib64/R/library/GGally/Meta/features.rds
/usr/lib64/R/library/GGally/Meta/hsearch.rds
/usr/lib64/R/library/GGally/Meta/links.rds
/usr/lib64/R/library/GGally/Meta/nsInfo.rds
/usr/lib64/R/library/GGally/Meta/package.rds
/usr/lib64/R/library/GGally/Meta/vignette.rds
/usr/lib64/R/library/GGally/NAMESPACE
/usr/lib64/R/library/GGally/NEWS.md
/usr/lib64/R/library/GGally/R/GGally
/usr/lib64/R/library/GGally/R/GGally.rdb
/usr/lib64/R/library/GGally/R/GGally.rdx
/usr/lib64/R/library/GGally/data/Rdata.rdb
/usr/lib64/R/library/GGally/data/Rdata.rds
/usr/lib64/R/library/GGally/data/Rdata.rdx
/usr/lib64/R/library/GGally/doc/docs.Rmd
/usr/lib64/R/library/GGally/doc/docs.html
/usr/lib64/R/library/GGally/doc/ggcoef.html
/usr/lib64/R/library/GGally/doc/ggduo.html
/usr/lib64/R/library/GGally/doc/gglyph.html
/usr/lib64/R/library/GGally/doc/ggmatrix.html
/usr/lib64/R/library/GGally/doc/ggnetworkmap.html
/usr/lib64/R/library/GGally/doc/ggpairs.html
/usr/lib64/R/library/GGally/doc/ggscatmat.html
/usr/lib64/R/library/GGally/doc/ggsurv.html
/usr/lib64/R/library/GGally/doc/index.html
/usr/lib64/R/library/GGally/doc/rd.Rmd
/usr/lib64/R/library/GGally/doc/rd.html
/usr/lib64/R/library/GGally/help/AnIndex
/usr/lib64/R/library/GGally/help/GGally.rdb
/usr/lib64/R/library/GGally/help/GGally.rdx
/usr/lib64/R/library/GGally/help/aliases.rds
/usr/lib64/R/library/GGally/help/paths.rds
/usr/lib64/R/library/GGally/html/00Index.html
/usr/lib64/R/library/GGally/html/R.css
/usr/lib64/R/library/GGally/tests/testthat.R
/usr/lib64/R/library/GGally/tests/testthat/data/airports.csv
/usr/lib64/R/library/GGally/tests/testthat/test-crosstalk.R
/usr/lib64/R/library/GGally/tests/testthat/test-gg-plots.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggcoef.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggcorr.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggfacet.R
/usr/lib64/R/library/GGally/tests/testthat/test-gglegend.R
/usr/lib64/R/library/GGally/tests/testthat/test-gglyph.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggmatrix.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggmatrix_add.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggmatrix_getput.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggnet.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggnet2.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggnetworkmap.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggnostic.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggparcoord.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggsave.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggscatmat.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggsurv.R
/usr/lib64/R/library/GGally/tests/testthat/test-utils.R
/usr/lib64/R/library/GGally/tests/testthat/test-wrap.R
/usr/lib64/R/library/GGally/tests/testthat/test-zzz_ggpairs.R
