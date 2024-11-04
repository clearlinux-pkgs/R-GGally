#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v4
# autospec commit: da8b975
#
Name     : R-GGally
Version  : 2.2.1
Release  : 60
URL      : https://cran.r-project.org/src/contrib/GGally_2.2.1.tar.gz
Source0  : https://cran.r-project.org/src/contrib/GGally_2.2.1.tar.gz
Summary  : Extension to 'ggplot2'
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-RColorBrewer
Requires: R-dplyr
Requires: R-ggplot2
Requires: R-ggstats
Requires: R-gtable
Requires: R-lifecycle
Requires: R-magrittr
Requires: R-plyr
Requires: R-progress
Requires: R-rlang
Requires: R-scales
Requires: R-tidyr
BuildRequires : R-RColorBrewer
BuildRequires : R-dplyr
BuildRequires : R-ggplot2
BuildRequires : R-ggstats
BuildRequires : R-gtable
BuildRequires : R-lifecycle
BuildRequires : R-magrittr
BuildRequires : R-network
BuildRequires : R-plyr
BuildRequires : R-progress
BuildRequires : R-rlang
BuildRequires : R-scales
BuildRequires : R-tidyr
BuildRequires : R-vdiffr
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
The R package 'ggplot2' is a plotting system based on the grammar of graphics.
    'GGally' extends 'ggplot2' by adding several functions
    to reduce the complexity of combining geometric objects with transformed data.
    Some of these functions include a pairwise plot matrix, a two group pairwise plot
    matrix, a parallel coordinates plot, a survival plot, and several functions to
    plot networks.

%prep
%setup -q -n GGally
pushd ..
cp -a GGally buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1707945509

%install
export SOURCE_DATE_EPOCH=1707945509
rm -rf %{buildroot}
LANG=C.UTF-8
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -flto -fno-semantic-interposition "
FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -flto -fno-semantic-interposition "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -flto -fno-semantic-interposition "
AR=gcc-ar
RANLIB=gcc-ranlib
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library
mkdir -p %{buildroot}-v3/usr/lib64/R/library
mkdir -p %{buildroot}-v4/usr/lib64/R/library
mkdir -p %{buildroot}-va/usr/lib64/R/library

mkdir -p ~/.R
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-v3/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize  -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v4 -mprefer-vector-width=512 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL --preclean  --install-tests --use-LTO --no-test-load --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}-v4/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper" > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=x86-64-v3 -mapxf -mavx10.1 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=x86-64-v3 -ftree-vectorize -mno-vzeroupper " >> ~/.R/Makevars
R CMD INSTALL  --install-tests --use-LTO --built-timestamp=${SOURCE_DATE_EPOCH} --data-compress=none --compress=none --build  -l %{buildroot}-va/usr/lib64/R/library .
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean  --use-LTO --install-tests --data-compress=none --compress=none --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library .
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc . || :

/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

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
/usr/lib64/R/library/GGally/NAMESPACE
/usr/lib64/R/library/GGally/NEWS.md
/usr/lib64/R/library/GGally/R/GGally
/usr/lib64/R/library/GGally/R/GGally.rdb
/usr/lib64/R/library/GGally/R/GGally.rdx
/usr/lib64/R/library/GGally/WORDLIST
/usr/lib64/R/library/GGally/data/Rdata.rdb
/usr/lib64/R/library/GGally/data/Rdata.rds
/usr/lib64/R/library/GGally/data/Rdata.rdx
/usr/lib64/R/library/GGally/help/AnIndex
/usr/lib64/R/library/GGally/help/GGally.rdb
/usr/lib64/R/library/GGally/help/GGally.rdx
/usr/lib64/R/library/GGally/help/aliases.rds
/usr/lib64/R/library/GGally/help/paths.rds
/usr/lib64/R/library/GGally/html/00Index.html
/usr/lib64/R/library/GGally/html/R.css
/usr/lib64/R/library/GGally/tests/spelling.R
/usr/lib64/R/library/GGally/tests/testthat.R
/usr/lib64/R/library/GGally/tests/testthat/data/airports.csv
/usr/lib64/R/library/GGally/tests/testthat/helper-options.R
/usr/lib64/R/library/GGally/tests/testthat/test-crosstalk.R
/usr/lib64/R/library/GGally/tests/testthat/test-deprecated.R
/usr/lib64/R/library/GGally/tests/testthat/test-gg-plots.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggally_colbar.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggally_cross.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggally_trends.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggbivariate.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggcoef.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggcorr.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggfacet.R
/usr/lib64/R/library/GGally/tests/testthat/test-gglegend.R
/usr/lib64/R/library/GGally/tests/testthat/test-gglyph.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggmatrix.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggmatrix_add.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggmatrix_getput.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggmatrix_location.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggnet.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggnet2.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggnetworkmap.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggnostic.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggparcoord.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggsave.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggscatmat.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggsurv.R
/usr/lib64/R/library/GGally/tests/testthat/test-ggtable.R
/usr/lib64/R/library/GGally/tests/testthat/test-utils.R
/usr/lib64/R/library/GGally/tests/testthat/test-vig_ggally.R
/usr/lib64/R/library/GGally/tests/testthat/test-wrap.R
/usr/lib64/R/library/GGally/tests/testthat/test-zzz_ggpairs.R
