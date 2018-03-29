# Support for documentation installation
# As the %%doc macro erases the target directory, namely
# $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}, manually installed
# documentation must be saved into a temporary dedicated directory.
%define _docdir %{_datadir}/doc/packages/boost-%{version}

%define most_libs libboost-atomic libboost-chrono libboost-date-time libboost-filesystem libboost-graph libboost-iostreams libboost-locale libboost-math libboost-program-options libboost-python libboost-random libboost-regex libboost-serialization libboost-signals libboost-system libboost-test libboost-thread libboost-timer libboost-wave

# Support for long double
%define disable_long_double 0
%ifarch %{arm}
  %define disable_long_double 1
%endif

# Configuration of MPI backends
%ifnarch %{ix86} x86_64
  # No MPICH support except on x86 and x86_64
  %bcond_with mpich
  %define _with_mpich 1
  %define build_mpi 1
  %define all_libs %{most_libs} libboost-mpich
%else
  %bcond_without mpich
  %define all_libs %{most_libs}
%endif

%ifarch s390 s390x
  # No OpenMPI support on zseries
  %bcond_with openmpi
  %define _with_openmpi 1
  %define build_mpi 1
  %define all_libs %{most_libs} libboost-openmpi
%else
  %bcond_without openmpi
  %define all_libs %{most_libs}
%endif

%define debug_package_requires %{all_libs}

Name: libboost
Summary: The free peer-reviewed portable C++ source libraries
Version: 1.59.0
Release: 1%{?dist}
License: Boost
URL: http://www.boost.org
Group: System Environment/Libraries
%define full_version %{name}-%{version}
%define file_version 1_59_0
Source0: boost_%{file_version}.tar.gz

# From the version 13 of Fedora, the Boost libraries are delivered
# with sonames equal to the Boost version (e.g., 1.41.0).  On older
# versions of Fedora (e.g., Fedora 12), the Boost libraries are
# delivered with another scheme for sonames (e.g., a soname of 5 for
# Fedora 12).  If for some reason you wish to set the sonamever
# yourself, you can do it here.
%define backward_sonamever 5
%if 0%{?rhel}
  %define sonamever %{version}
%else
  %if 0%{?fedora} >= 13
    %define sonamever %{version}
  %else
    %define sonamever %{backward_sonamever}
  %endif
%endif

# boost is an "umbrella" package that pulls in all other boost
# components, except for MPI sub-packages.  Those are "speacial", one
# doesn't necessarily need them and the more typical scenario, I
# think, will be that the developer wants to pick one MPI flavor.
Requires: libboost-atomic%{?_isa} = %{version}-%{release}
Requires: libboost-chrono%{?_isa} = %{version}-%{release}
Requires: libboost-date-time%{?_isa} = %{version}-%{release}
Requires: libboost-filesystem%{?_isa} = %{version}-%{release}
Requires: libboost-graph%{?_isa} = %{version}-%{release}
Requires: libboost-iostreams%{?_isa} = %{version}-%{release}
Requires: libboost-locale%{?_isa} = %{version}-%{release}
Requires: libboost-math%{?_isa} = %{version}-%{release}
Requires: libboost-program-options%{?_isa} = %{version}-%{release}
Requires: libboost-python%{?_isa} = %{version}-%{release}
Requires: libboost-random%{?_isa} = %{version}-%{release}
Requires: libboost-regex%{?_isa} = %{version}-%{release}
Requires: libboost-serialization%{?_isa} = %{version}-%{release}
Requires: libboost-signals%{?_isa} = %{version}-%{release}
Requires: libboost-system%{?_isa} = %{version}-%{release}
Requires: libboost-test%{?_isa} = %{version}-%{release}
Requires: libboost-thread%{?_isa} = %{version}-%{release}
Requires: libboost-timer%{?_isa} = %{version}-%{release}
Requires: libboost-wave%{?_isa} = %{version}-%{release}

BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: cmake
BuildRequires: libstdc++-devel
BuildRequires: bzip2-libs
BuildRequires: bzip2-devel
BuildRequires: zlib-devel
BuildRequires: python-devel
BuildRequires: libicu-devel
BuildRequires: chrpath
BuildRequires: dos2unix
BuildRequires: gcc-c++
BuildRequires: expat-devel
BuildRequires: docbook-dtds
BuildRequires: docbook-style-xsl
BuildRequires: doxygen
BuildRequires: libxslt
BuildRequires: texlive-latex

%bcond_with tests
%bcond_with docs_generated

%description
Boost provides free peer-reviewed portable C++ source libraries.  The
emphasis is on libraries which work well with the C++ Standard
Library, in the hopes of establishing "existing practice" for
extensions and providing reference implementations so that the Boost
libraries are suitable for eventual standardization. (Some of the
libraries have already been proposed for inclusion in the C++
Standards Committee's upcoming C++ Standard Library Technical Report.)

%package        -n libboost-atomic
Summary:        Runtime component of boost atomic library
Group:          System Environment/Libraries

%description    -n libboost-atomic
Runtime support for boost atomic library.


%package        -n libboost-chrono
Summary:        Runtime component of boost chrono library
Group:          System Environment/Libraries

%description    -n libboost-chrono
Runtime support for boost chrono library.


%package        -n libboost-container
Summary:        Runtime component of boost container library
Group:          System Environment/Libraries

%description    -n libboost-container
Runtime support for boost container library.


%package        -n libboost-context
Summary:        Runtime component of boost context library
Group:          System Environment/Libraries

%description    -n libboost-context
Runtime support for boost context library.


%package        -n libboost-coroutine
Summary:        Runtime component of boost coroutine library
Group:          System Environment/Libraries

%description    -n libboost-coroutine
Runtime support for boost coroutine library.


%package        -n libboost-date-time
Summary:        Runtime component of boost date-time library
Group:          System Environment/Libraries

%description    -n libboost-date-time
Runtime support for Boost Date Time, set of date-time libraries based
on generic programming concepts.


%package        -n libboost-doc
Summary:        HTML documentation for the Boost C++ Libraries
Group:          Documentation
%if 0%{?fedora} >= 10
BuildArch:      noarch
%endif

%description    -n libboost-doc
This package contains the documentation in the HTML format of the Boost C++
libraries. The documentation provides the same content as that on the Boost
web page (http://www.boost.org/doc/libs/1_59_0).


%package        -n libboost-filesystem
Summary:        Runtime component of boost filesystem library
Group:          System Environment/Libraries

%description    -n libboost-filesystem
Runtime support for the Boost Filesystem Library, which provides
portable facilities to query and manipulate paths, files, and
directories.


%package        -n libboost-graph
Summary:        Runtime component of boost graph library
Group:          System Environment/Libraries

%description    -n libboost-graph
Runtime support for the BGL graph library.  BGL interface and graph
components are generic, in the same sense as the the Standard Template
Library (STL).


%package        -n libboost-iostreams
Summary:        Runtime component of boost iostreams library
Group:          System Environment/Libraries

%description    -n libboost-iostreams
Runtime support for Boost.IOStreams, a framework for defining streams,
stream buffers and i/o filters.


%package        -n libboost-locale
Summary:        Runtime component of boost locale library
Group:          System Environment/Libraries

%description    -n libboost-locale
Runtime support for boost locale library.


%package        -n libboost-log
Summary:        Runtime component of boost log library
Group:          System Environment/Libraries

%description    -n libboost-log
Runtime support for boost log library.


%package        -n libboost-math
Summary:        Math functions for boost TR1 library
Group:          System Environment/Libraries

%description    -n libboost-math
Run-Time support for C99 and C++ TR1 C-style Functions from math
portion of Boost.TR1.


%package        -n libboost-program-options
Summary:        Runtime component of boost program_options library
Group:          System Environment/Libraries

%description    -n libboost-program-options
Runtime support of boost program options library, which allows program
developers to obtain (name, value) pairs from the user, via
conventional methods such as command line and configuration file.


%package        -n libboost-python
Summary:        Runtime component of boost python library
Group:          System Environment/Libraries

%description    -n libboost-python
The Boost Python Library is a framework for interfacing Python and
C++. It allows you to quickly and seamlessly expose C++ classes
functions and objects to Python, and vice versa, using no special
tools -- just your C++ compiler.  This package contains runtime
support for Boost Python Library.


%package        -n libboost-random
Summary:        Runtime component of boost random library
Group:          System Environment/Libraries

%description    -n libboost-random
Runtime support for boost random library.


%package        -n libboost-regex
Summary:        Runtime component of boost regular expression library
Group:          System Environment/Libraries

%description    -n libboost-regex
Runtime support for boost regular expression library.


%package        -n libboost-serialization
Summary:        Summary: Runtime component of boost serialization library
Group:          System Environment/Libraries

%description    -n libboost-serialization
Runtime support for serialization for persistence and marshaling.


%package        -n libboost-signals
Summary:        Runtime component of boost signals and slots library
Group:          System Environment/Libraries

%description    -n libboost-signals
Runtime support for managed signals & slots callback implementation.


%package        -n libboost-system
Summary:        Runtime component of boost system support library
Group:          System Environment/Libraries

%description    -n libboost-system
Runtime component of Boost operating system support library, including
the diagnostics support that will be part of the C++0x standard
library.


%package        -n libboost-test
Summary:        Runtime component of boost test library
Group:          System Environment/Libraries

%description    -n libboost-test
Runtime support for simple program testing, full unit testing, and for
program execution monitoring.


%package        -n libboost-thread
Summary:        Runtime component of boost thread library
Group:          System Environment/Libraries

%description    -n libboost-thread
Runtime component Boost.Thread library, which provides classes and
functions for managing multiple threads of execution, and for
synchronizing data between the threads or providing separate copies of
data specific to individual threads.


%package        -n libboost-timer
Summary:        Runtime component of boost timer library
Group:          System Environment/Libraries

%description    -n libboost-timer
Runtime support for boost timer library.


%package        -n libboost-wave
Summary:        Runtime component of boost C99/C++ preprocessing library
Group:          System Environment/Libraries

%description    -n libboost-wave
Runtime support for the Boost.Wave library, a Standards conformant,
and highly configurable implementation of the mandated C99/C++
preprocessor functionality.


%package        -n libboost-devel
Summary:        The Boost C++ headers and shared development libraries
Group:          Development/Libraries
Requires:       libboost%{?_isa} = %{version}-%{release}
Requires:       libstdc++-devel
Provides:       libboost-python-devel = %{version}-%{release}

%description    -n libboost-devel
Headers and shared object symlinks for the Boost C++ libraries.


%package        -n libboost-static
Summary:        The Boost C++ static development libraries
Group:          Development/Libraries
Requires:       libboost-devel%{?_isa} = %{version}-%{release}
Obsoletes:      libboost-static < %{version}-%{release}
Provides:       libboost-static = %{version}-%{release}

%description    -n libboost-static
Static Boost C++ libraries.


%if 0%{?_with_openmpi:1}

%package        -n libboost-openmpi
Summary:        Runtime component of Boost.MPI library
Group:          System Environment/Libraries
Requires:       openmpi%{?_isa}
BuildRequires:  openmpi-devel
Requires:       libboost-serialization%{?_isa} = %{version}-%{release}

%description    -n libboost-openmpi
Runtime support for Boost.MPI-OpenMPI, a library providing a clean C++
API over the OpenMPI implementation of MPI.


%package        -n libboost-openmpi-devel
Summary:        Shared library symlinks for Boost.MPI
Group:          System Environment/Libraries
Requires:       libboost-devel%{?_isa} = %{version}-%{release}
Requires:       libboost-openmpi%{?_isa} = %{version}-%{release}
Requires:       libboost-openmpi-python%{?_isa} = %{version}-%{release}
Requires:       libboost-graph-openmpi%{?_isa} = %{version}-%{release}

%description    -n libboost-openmpi-devel
Devel package for Boost.MPI-OpenMPI, a library providing a clean C++
API over the OpenMPI implementation of MPI.


%package        -n libboost-openmpi-python
Summary:        Python runtime component of Boost.MPI library
Group:          System Environment/Libraries
Requires:       libboost-openmpi%{?_isa} = %{version}-%{release}
Requires:       libboost-python%{?_isa} = %{version}-%{release}
Requires:       libboost-serialization%{?_isa} = %{version}-%{release}

%description    -n libboost-openmpi-python
Python support for Boost.MPI-OpenMPI, a library providing a clean C++
API over the OpenMPI implementation of MPI.


%package        -n libboost-graph-openmpi
Summary:        Runtime component of parallel boost graph library
Group:          System Environment/Libraries
Requires:       libboost-openmpi%{?_isa} = %{version}-%{release}
Requires:       libboost-serialization%{?_isa} = %{version}-%{release}

%description    -n libboost-graph-openmpi
Runtime support for the Parallel BGL graph library.  The interface and
graph components are generic, in the same sense as the the Standard
Template Library (STL).  This libraries in this package use OpenMPI
backend to do the parallel work.

%endif


%if 0%{?_with_mpich:1}

%package        -n libboost-mpich
Summary:        Runtime component of Boost.MPI library
Group:          System Environment/Libraries
Requires:       mpich%{?_isa}
BuildRequires:  mpich-devel
Requires:       libboost-serialization%{?_isa} = %{version}-%{release}
Obsoletes:      libboost-mpich2 < %{version}

%description    -n libboost-mpich
Runtime support for Boost.MPI-MPICH, a library providing a clean C++
API over the MPICH implementation of MPI.


%package        -n libboost-mpich-devel
Summary:        Shared library symlinks for Boost.MPI
Group:          System Environment/Libraries
Requires:       libboost-devel%{?_isa} = %{version}-%{release}
Requires:       libboost-mpich%{?_isa} = %{version}-%{release}
Requires:       libboost-mpich-python%{?_isa} = %{version}-%{release}
Requires:       libboost-graph-mpich%{?_isa} = %{version}-%{release}
Obsoletes:      libboost-mpich2-devel < %{version}

%description    -n libboost-mpich-devel
Devel package for Boost.MPI-MPICH, a library providing a clean C++
API over the MPICH implementation of MPI.


%package        -n libboost-mpich-python
Summary:        Python runtime component of Boost.MPI library
Group:          System Environment/Libraries
Requires:       libboost-mpich%{?_isa} = %{version}-%{release}
Requires:       libboost-python%{?_isa} = %{version}-%{release}
Requires:       libboost-serialization%{?_isa} = %{version}-%{release}
Obsoletes:      libboost-mpich2-python < %{version}

%description    -n libboost-mpich-python
Python support for Boost.MPI-MPICH, a library providing a clean C++
API over the MPICH implementation of MPI.


%package        -n libboost-graph-mpich
Summary:        Runtime component of parallel boost graph library
Group:          System Environment/Libraries
Requires:       libboost-mpich%{?_isa} = %{version}-%{release}
Requires:       libboost-serialization%{?_isa} = %{version}-%{release}
Obsoletes:      libboost-graph-mpich2 < %{version}

%description    -n libboost-graph-mpich
Runtime support for the Parallel BGL graph library.  The interface and
graph components are generic, in the same sense as the the Standard
Template Library (STL).  This libraries in this package use MPICH
backend to do the parallel work.

%endif


%prep
%setup -q -n boost_%{file_version}

%build
# Support for building tests.
%define boost_testflags -DBUILD_TESTS="NONE"
%if %{with tests}
  %define boost_testflags -DBUILD_TESTS="ALL"
%endif

export CXXFLAGS="-fno-strict-aliasing %{optflags}"

#Ensure that all scripts in the source are executable
find -type f ! \( -name \*.sh -o -name \*.py -o -name \*.pl \) -exec chmod -x {} +

#Clean up all generated .orig files
find . -name \*.orig -exec rm {} +

find . -type f -exec chmod u+w {} +

%if 0%{?build_mpi:1}
./bootstrap.sh --libdir=%{buildroot}%{_libdir} --includedir=%{buildroot}%{_includedir}
%else
./bootstrap.sh --libdir=%{buildroot}%{_libdir} --includedir=%{buildroot}%{_includedir} --without-libraries=mpi
%endif
./b2 -j4 -d0

%install
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/boost

./b2 install -j4

mkdir -p %{buildroot}%{_docdir}

pushd %{buildroot}%{_libdir}
blibs=$(find . -name \*.so.%{sonamever})
echo $blibs | xargs chrpath -d

for lib in ${blibs}; do
  BASE=$(basename ${lib} .so.%{version})
  SONAME_MT="$BASE-mt.so"
  ln -sf ${lib} $SONAME_MT
done
popd

#install the man pages
rm -rf doc/man/man3/boost::units::operator

for sec in 3 7 9; do
    install -d %buildroot/%{_mandir}/man${sec}
done

#install doc files
dos2unix libs/ptr_container/doc/tutorial_example.html \
	libs/parameter/doc/html/reference.html \
	libs/parameter/doc/html/index.html \
	libs/iostreams/doc/tree/tree.js \
	libs/graph/doc/lengauer_tarjan_dominator.htm \
find . -name \*.htm\* -o -name \*.gif -o -name \*.css -o -name \*.jpg -o -name \*.png -o -name \*.ico | \
	tar -cf - --files-from=- | tar -C %{buildroot}%{_docdir} -xf -
rm -rf %{buildroot}%{_docdir}/boost
ln -s /usr/include/boost %{buildroot}%{_docdir}
ln -s LICENSE_1_0.txt %{buildroot}%{_docdir}/LICENSE_1_0.txt
#only for documentation, doesn't need to be executable
find %{buildroot}%{_docdir} -name \*.py -exec chmod -x {} +
#symlink dupes

# MPI subpackages don't need the ldconfig magic.  They are hidden by
# default, in MPI backend-specific directory, and only show to the
# user after the relevant environment module has been loaded.

%post -n libboost-atomic -p /sbin/ldconfig
%postun -n libboost-atomic -p /sbin/ldconfig

%post -n libboost-chrono -p /sbin/ldconfig
%postun -n libboost-chrono -p /sbin/ldconfig

%post -n libboost-container -p /sbin/ldconfig
%postun -n libboost-container -p /sbin/ldconfig

%post -n libboost-context -p /sbin/ldconfig
%postun -n libboost-context -p /sbin/ldconfig

%post -n libboost-coroutine -p /sbin/ldconfig
%postun -n libboost-coroutine -p /sbin/ldconfig

%post -n libboost-date-time -p /sbin/ldconfig
%postun -n libboost-date-time -p /sbin/ldconfig

%post -n libboost-filesystem -p /sbin/ldconfig
%postun -n libboost-filesystem -p /sbin/ldconfig

%post -n libboost-graph -p /sbin/ldconfig
%postun -n libboost-graph -p /sbin/ldconfig

%post -n libboost-iostreams -p /sbin/ldconfig
%postun -n libboost-iostreams -p /sbin/ldconfig

%post -n libboost-locale -p /sbin/ldconfig
%postun -n libboost-locale -p /sbin/ldconfig

%post -n libboost-log -p /sbin/ldconfig
%postun -n libboost-log -p /sbin/ldconfig

%post -n libboost-math -p /sbin/ldconfig
%postun -n libboost-math -p /sbin/ldconfig

%post -n libboost-program-options -p /sbin/ldconfig
%postun -n libboost-program-options -p /sbin/ldconfig

%post -n libboost-python -p /sbin/ldconfig
%postun -n libboost-python -p /sbin/ldconfig

%post -n libboost-random -p /sbin/ldconfig
%postun -n libboost-random -p /sbin/ldconfig

%post -n libboost-regex -p /sbin/ldconfig
%postun -n libboost-regex -p /sbin/ldconfig

%post -n libboost-serialization -p /sbin/ldconfig
%postun -n libboost-serialization -p /sbin/ldconfig

%post -n libboost-signals -p /sbin/ldconfig
%postun -n libboost-signals -p /sbin/ldconfig

%post -n libboost-system -p /sbin/ldconfig
%postun -n libboost-system -p /sbin/ldconfig

%post -n libboost-test -p /sbin/ldconfig
%postun -n libboost-test -p /sbin/ldconfig

%post -n libboost-thread -p /sbin/ldconfig
%postun -n libboost-thread -p /sbin/ldconfig

%post -n libboost-timer -p /sbin/ldconfig
%postun -n libboost-timer -p /sbin/ldconfig

%post -n libboost-wave -p /sbin/ldconfig
%postun -n libboost-wave -p /sbin/ldconfig



%files

%files -n libboost-atomic
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_atomic*.so.%{sonamever}

%files -n libboost-chrono
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_chrono*.so.%{sonamever}

%files -n libboost-container
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_container*.so.%{sonamever}

%files -n libboost-context
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_context*.so.%{sonamever}

%files -n libboost-coroutine
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_coroutine*.so.%{sonamever}

%files -n libboost-date-time
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_date_time*.so.%{sonamever}

%files -n libboost-doc
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%doc %{_docdir}/*

%files -n libboost-filesystem
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_filesystem*.so.%{sonamever}

%files -n libboost-graph
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_graph*.so.%{sonamever}

%files -n libboost-iostreams
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_iostreams*.so.%{sonamever}

%files -n libboost-locale
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_locale*.so.%{sonamever}

%files -n libboost-log
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_log*.so.%{sonamever}

%files -n libboost-math
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_math*.so.%{sonamever}

%files -n libboost-program-options
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_program_options*.so.%{sonamever}

%files -n libboost-python
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_python*.so.%{sonamever}

%files -n libboost-random
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_random*.so.%{sonamever}

%files -n libboost-regex
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_regex*.so.%{sonamever}

%files -n libboost-serialization
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_*serialization*.so.%{sonamever}

%files -n libboost-signals
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_signals*.so.%{sonamever}

%files -n libboost-system
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_system*.so.%{sonamever}

%files -n libboost-test
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_prg_exec_monitor*.so.%{sonamever}
%{_libdir}/libboost_unit_test_framework*.so.%{sonamever}

%files -n libboost-thread
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_thread*.so.%{sonamever}

%files -n libboost-timer
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_timer*.so.%{sonamever}

%files -n libboost-wave
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/libboost_wave*.so.%{sonamever}

%files -n libboost-devel
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_includedir}/boost
%{_libdir}/*.so

%files -n libboost-static
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/*.a
%if 0%{?_with_mpich:1}
%{_libdir}/mpich/lib/*.a
%endif
%if 0%{?_with_openmpi:1}
%{_libdir}/openmpi/lib/*.a
%endif

# OpenMPI packages
%if 0%{?_with_openmpi:1}

%files -n libboost-openmpi
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/openmpi/lib/libboost_mpi.so.%{sonamever}
%{_libdir}/openmpi/lib/libboost_mpi-mt.so.%{sonamever}

%files -n libboost-openmpi-devel
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/openmpi/lib/libboost_*.so

%files -n libboost-openmpi-python
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/openmpi/lib/libboost_mpi_python*.so.%{sonamever}
%{python_sitearch}/openmpi/boost

%files -n libboost-graph-openmpi
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/openmpi/lib/libboost_graph_parallel.so.%{sonamever}
%{_libdir}/openmpi/lib/libboost_graph_parallel-mt.so.%{sonamever}

%endif

# MPICH packages
%if 0%{?_with_mpich:1}

%files -n libboost-mpich
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/mpich/lib/libboost_mpi.so.%{sonamever}
%{_libdir}/mpich/lib/libboost_mpi-mt.so.%{sonamever}

%files -n libboost-mpich-devel
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/mpich/lib/libboost_*.so

%files -n libboost-mpich-python
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/mpich/lib/libboost_mpi_python*.so.%{sonamever}
%{python_sitearch}/mpich/boost

%files -n libboost-graph-mpich
%defattr(-, root, root, -)
%doc LICENSE_1_0.txt
%{_libdir}/mpich/lib/libboost_graph_parallel.so.%{sonamever}
%{_libdir}/mpich/lib/libboost_graph_parallel-mt.so.%{sonamever}

%endif

%changelog
* Thu Mar 29 2018 Don Jackson <github:realdonjackson> 1.59.0
- libboost version 1.59.0.
