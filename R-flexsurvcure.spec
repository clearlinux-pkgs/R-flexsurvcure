#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: R
# autospec version: v21
# autospec commit: e36a856
#
Name     : R-flexsurvcure
Version  : 1.3.3
Release  : 4
URL      : https://ftp.osuosl.org/pub/cran/src/contrib/flexsurvcure_1.3.3.tar.gz
Source0  : https://ftp.osuosl.org/pub/cran/src/contrib/flexsurvcure_1.3.3.tar.gz
Summary  : Flexible Parametric Cure Models
Group    : Development/Tools
License  : GPL-2.0+
Requires: R-flexsurv
BuildRequires : R-flexsurv
BuildRequires : buildreq-R
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
No detailed description available

%prep
%setup -q -n flexsurvcure

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1739816698

%install
export SOURCE_DATE_EPOCH=1739816698
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


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/flexsurvcure/DESCRIPTION
/usr/lib64/R/library/flexsurvcure/INDEX
/usr/lib64/R/library/flexsurvcure/Meta/Rd.rds
/usr/lib64/R/library/flexsurvcure/Meta/features.rds
/usr/lib64/R/library/flexsurvcure/Meta/hsearch.rds
/usr/lib64/R/library/flexsurvcure/Meta/links.rds
/usr/lib64/R/library/flexsurvcure/Meta/nsInfo.rds
/usr/lib64/R/library/flexsurvcure/Meta/package.rds
/usr/lib64/R/library/flexsurvcure/Meta/vignette.rds
/usr/lib64/R/library/flexsurvcure/NAMESPACE
/usr/lib64/R/library/flexsurvcure/NEWS.md
/usr/lib64/R/library/flexsurvcure/R/flexsurvcure
/usr/lib64/R/library/flexsurvcure/R/flexsurvcure.rdb
/usr/lib64/R/library/flexsurvcure/R/flexsurvcure.rdx
/usr/lib64/R/library/flexsurvcure/doc/flexsurvcure.R
/usr/lib64/R/library/flexsurvcure/doc/flexsurvcure.Rmd
/usr/lib64/R/library/flexsurvcure/doc/flexsurvcure.html
/usr/lib64/R/library/flexsurvcure/doc/index.html
/usr/lib64/R/library/flexsurvcure/help/AnIndex
/usr/lib64/R/library/flexsurvcure/help/aliases.rds
/usr/lib64/R/library/flexsurvcure/help/flexsurvcure.rdb
/usr/lib64/R/library/flexsurvcure/help/flexsurvcure.rdx
/usr/lib64/R/library/flexsurvcure/help/paths.rds
/usr/lib64/R/library/flexsurvcure/html/00Index.html
/usr/lib64/R/library/flexsurvcure/html/R.css
/usr/lib64/R/library/flexsurvcure/tests/testthat.R
/usr/lib64/R/library/flexsurvcure/tests/testthat/test_match_stata.R
/usr/lib64/R/library/flexsurvcure/tests/testthat/test_surv_funcs.R
/usr/lib64/R/library/flexsurvcure/tests/testthat/testthat-problems.rds
