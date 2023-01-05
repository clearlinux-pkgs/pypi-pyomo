#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-pyomo
Version  : 6.4.4
Release  : 10
URL      : https://files.pythonhosted.org/packages/f0/dd/9d2143b0ec2f7eb4bd7e84a4367c1667f765de8e8be03f128753158c7149/Pyomo-6.4.4.tar.gz
Source0  : https://files.pythonhosted.org/packages/f0/dd/9d2143b0ec2f7eb4bd7e84a4367c1667f765de8e8be03f128753158c7149/Pyomo-6.4.4.tar.gz
Summary  : Pyomo: Python Optimization Modeling Objects
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-pyomo-bin = %{version}-%{release}
Requires: pypi-pyomo-license = %{version}-%{release}
Requires: pypi-pyomo-python = %{version}-%{release}
Requires: pypi-pyomo-python3 = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : pypi(ply)

%description
## Pyomo Overview
        
        Pyomo is a Python-based open-source software package that supports a
        diverse set of optimization capabilities for formulating and analyzing
        optimization models. Pyomo can be used to define symbolic problems,
        create concrete problem instances, and solve these instances with
        standard solvers. Pyomo supports a wide range of problem types,

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
%setup -q -n Pyomo-6.4.4
cd %{_builddir}/Pyomo-6.4.4
pushd ..
cp -a Pyomo-6.4.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1670891726
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
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-pyomo
cp %{_builddir}/Pyomo-%{version}/LICENSE.md %{buildroot}/usr/share/package-licenses/pypi-pyomo/fb0d4c52dad6bba4d86046bff0f3eb2f58926fd2 || :
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
/usr/share/package-licenses/pypi-pyomo/fb0d4c52dad6bba4d86046bff0f3eb2f58926fd2

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
