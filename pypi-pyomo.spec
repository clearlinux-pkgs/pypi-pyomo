#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: distutils3
#
Name     : pypi-pyomo
Version  : 6.6.2
Release  : 14
URL      : https://files.pythonhosted.org/packages/9b/73/0c11bb78ef7db2bf04424a4a7511c1f0a63777d7120f98a6f1d9e59e9dc7/Pyomo-6.6.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/9b/73/0c11bb78ef7db2bf04424a4a7511c1f0a63777d7120f98a6f1d9e59e9dc7/Pyomo-6.6.2.tar.gz
Summary  : Pyomo: Python Optimization Modeling Objects
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pyomo-bin = %{version}-%{release}
Requires: pypi-pyomo-license = %{version}-%{release}
Requires: pypi-pyomo-python = %{version}-%{release}
Requires: pypi-pyomo-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(ply)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
[![Github Actions Status](https://github.com/Pyomo/pyomo/workflows/GitHub%20CI/badge.svg?event=push)](https://github.com/Pyomo/pyomo/actions?query=event%3Apush+workflow%3A%22GitHub+CI%22)
[![Jenkins Status](https://github.com/Pyomo/jenkins-status/blob/main/pyomo_main.svg)](https://pyomo-jenkins.sandia.gov/)
[![codecov](https://codecov.io/gh/Pyomo/pyomo/branch/main/graph/badge.svg)](https://codecov.io/gh/Pyomo/pyomo)
[![Documentation Status](https://readthedocs.org/projects/pyomo/badge/?version=latest)](http://pyomo.readthedocs.org/en/latest/)
[![Build services](https://github.com/Pyomo/jenkins-status/blob/main/pyomo_services.svg)](https://pyomo-jenkins.sandia.gov/)
[![GitHub contributors](https://img.shields.io/github/contributors/pyomo/pyomo.svg)](https://github.com/pyomo/pyomo/graphs/contributors)
[![Merged PRs](https://img.shields.io/github/issues-pr-closed-raw/pyomo/pyomo.svg?label=merged+PRs)](https://github.com/pyomo/pyomo/pulls?q=is:pr+is:merged)

%package bin
Summary: bin components for the pypi-pyomo package.
Group: Binaries
Requires: pypi-pyomo-license = %{version}-%{release}

%description bin
bin components for the pypi-pyomo package.


%package license
Summary: license components for the pypi-pyomo package.
Group: Default

%description license
license components for the pypi-pyomo package.


%package python
Summary: python components for the pypi-pyomo package.
Group: Default
Requires: pypi-pyomo-python3 = %{version}-%{release}

%description python
python components for the pypi-pyomo package.


%package python3
Summary: python3 components for the pypi-pyomo package.
Group: Default
Requires: python3-core
Provides: pypi(pyomo)
Requires: pypi(ply)

%description python3
python3 components for the pypi-pyomo package.


%prep
%setup -q -n Pyomo-6.6.2
cd %{_builddir}/Pyomo-6.6.2
pushd ..
cp -a Pyomo-6.6.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1693253455
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyomo
cp %{_builddir}/Pyomo-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-pyomo/c1c4d16ea67d2566b9cd10cb5141738f421c6c83 || :
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
/usr/bin/pyomo

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-pyomo/c1c4d16ea67d2566b9cd10cb5141738f421c6c83

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
