#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-nltk
Version  : 3.7
Release  : 3
URL      : https://files.pythonhosted.org/packages/b4/e0/840a250e5f85c480389c44d4058c7888b0c9f5f5333b353c77782a8a8e23/nltk-3.7.zip
Source0  : https://files.pythonhosted.org/packages/b4/e0/840a250e5f85c480389c44d4058c7888b0c9f5f5333b353c77782a8a8e23/nltk-3.7.zip
Summary  : Natural Language Toolkit
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-nltk-bin = %{version}-%{release}
Requires: pypi-nltk-license = %{version}-%{release}
Requires: pypi-nltk-python = %{version}-%{release}
Requires: pypi-nltk-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(click)
BuildRequires : pypi(joblib)
BuildRequires : pypi(py)
BuildRequires : pypi(regex)
BuildRequires : pypi(tqdm)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
natural language processing.  NLTK requires Python 3.7, 3.8, 3.9 or 3.10.

%package bin
Summary: bin components for the pypi-nltk package.
Group: Binaries
Requires: pypi-nltk-license = %{version}-%{release}

%description bin
bin components for the pypi-nltk package.


%package license
Summary: license components for the pypi-nltk package.
Group: Default

%description license
license components for the pypi-nltk package.


%package python
Summary: python components for the pypi-nltk package.
Group: Default
Requires: pypi-nltk-python3 = %{version}-%{release}

%description python
python components for the pypi-nltk package.


%package python3
Summary: python3 components for the pypi-nltk package.
Group: Default
Requires: python3-core
Provides: pypi(nltk)
Requires: pypi(click)
Requires: pypi(joblib)
Requires: pypi(regex)
Requires: pypi(tqdm)

%description python3
python3 components for the pypi-nltk package.


%prep
%setup -q -n nltk-3.7
cd %{_builddir}/nltk-3.7
pushd ..
cp -a nltk-3.7 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656391247
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-nltk
cp %{_builddir}/nltk-3.7/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-nltk/47b573e3824cd5e02a1a3ae99e2735b49e0256e4
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/nltk

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-nltk/47b573e3824cd5e02a1a3ae99e2735b49e0256e4

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
