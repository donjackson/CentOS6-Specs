%define uname     vowpal_wabbit
%define version   8.5.0
%define release   1
%define major     0
%define libname   lib%{name}%{major}
%define develname lib%{name}-devel

Name:           vowpal-wabbit
Version:        %{version}
Release:        %{release}%{?dist}
Summary:        A fast and efficient machine learning system
License:        BSD
Group:          Sciences/Mathematics
Url:            http://hunch.net/~vw/
Source0:        http://github.com/JohnLangford/%{uname}/archive/%{version}/%{uname}-%{version}.tar.gz
BuildRequires:  gcc-c++
BuildRequires:  libboost-devel
BuildRequires:  zlib-devel

%description
The Vowpal Wabbit (VW) project is a fast out-of-core learning system sponsored
by Microsoft Research and (previously) Yahoo! Research.

Vowpal Wabbit is notable as an efficient scalable implementation of online
machine learning and support for a number of machine learning reductions,
importance weighting, and a selection of different loss functions and
optimization algorithms.

%package -n     %{libname}
Summary:        Main library for Vowpal Wabbit
Group:          System/Libraries
Provides:       %{name} = %{version}-%{release}

%description -n %{libname}
This package contains the library needed to run programs dynamically
linked with vowpal-wabbit.

%package -n     %{develname}
Summary:        Headers for developing programs that will use Vowpal Wabbit
Group:          Development/C
Requires:       %{name} = %{version}
Requires:       %{libname} = %{version}
Provides:       %{name}-devel = %{version}-%{release}

%description -n %{develname}
This package contains the headers that programmers will need to develop
applications which will use Vowpal Wabbit.

%prep
%setup -q -n %{uname}-%{version}

%build
./autogen.sh
./configure
make clean
make

%install
make \
    DESTDIR=$RPM_BUILD_ROOT \
install

# install the utl scripts
mkdir -p %{buildroot}%{_bindir}/
mkdir -p %{buildroot}%{_libdir}/
mkdir -p %{buildroot}%{_includedir}/vowpalwabbit/
mkdir -p %{buildroot}%{_datadir}/vowpalwabbit
install -m 0755 utl/logistic %{buildroot}%{_bindir}/
install -m 0755 utl/vw-convergence %{buildroot}%{_bindir}/
install -m 0755 utl/vw-csv2bin %{buildroot}%{_bindir}/
install -m 0755 utl/vw-hypersearch %{buildroot}%{_bindir}/
install -m 0755 utl/vw-regr %{buildroot}%{_bindir}/
install -m 0755 utl/vw-top-errors %{buildroot}%{_bindir}/
install -m 0755 utl/vw-varinfo %{buildroot}%{_bindir}/
install -m 0755 utl/vw2csv %{buildroot}%{_bindir}/
install -m 0644 utl/vw-validate.html %{buildroot}%{_datadir}/vowpalwabbit/

# install the binaries
install -m 0755 %{buildroot}/usr/local/bin/active_interactor %{buildroot}%{_bindir}/
install -m 0755 %{buildroot}/usr/local/bin/ezexample_predict %{buildroot}%{_bindir}/
install -m 0755 %{buildroot}/usr/local/bin/ezexample_train %{buildroot}%{_bindir}/
install -m 0755 %{buildroot}/usr/local/bin/library_example %{buildroot}%{_bindir}/
install -m 0755 %{buildroot}/usr/local/bin/spanning_tree %{buildroot}%{_bindir}/
install -m 0755 %{buildroot}/usr/local/bin/vw %{buildroot}%{_bindir}/

# install the libraries
install -m 0755 %{buildroot}/usr/local/lib/liballreduce.so.* %{buildroot}%{_libdir}/
install -m 0755 %{buildroot}/usr/local/lib/libvw.so.* %{buildroot}%{_libdir}/
install -m 0755 %{buildroot}/usr/local/lib/libvw_c_wrapper.so.* %{buildroot}%{_libdir}/

# install the devel files
mkdir -p %{buildroot}%{_libdir}/pkgconfig
install -m 0755 %{buildroot}/usr/local/include/vowpalwabbit/*.h %{buildroot}%{_includedir}/vowpalwabbit/
install -m 0755 %{buildroot}/usr/local/lib/pkgconfig/* %{buildroot}%{_libdir}/pkgconfig/

# remove libtool files
find %{buildroot} -name '*.la' -delete

%files
%doc README LICENSE AUTHORS
%{_bindir}/active_interactor
%{_bindir}/ezexample_predict
%{_bindir}/ezexample_train
%{_bindir}/library_example
%{_bindir}/logistic
%{_bindir}/spanning_tree
%{_bindir}/vw
%{_bindir}/vw-convergence
%{_bindir}/vw-csv2bin
%{_bindir}/vw-hypersearch
%{_bindir}/vw-regr
%{_bindir}/vw-top-errors
%{_bindir}/vw-varinfo
%{_bindir}/vw2csv
%dir %{_datadir}/vowpalwabbit
%{_datadir}/vowpalwabbit/vw-validate.html

#%files -n %{libname}
%{_libdir}/liballreduce.so.%{major}*
%{_libdir}/libvw.so.%{major}*
%{_libdir}/libvw_c_wrapper.so.%{major}*

#%files -n %{develname}
%dir %{_includedir}/vowpalwabbit
%{_includedir}/vowpalwabbit/*.h
%{_libdir}/*.so.%{major}*
%{_libdir}/pkgconfig/libvw.pc
%{_libdir}/pkgconfig/libvw_c_wrapper.pc


%changelog
* Thu Mar 29 2018 Don Jackson <github:realdonjackson> 8.5.0
- vowpal-wabbit version 8.5.0.
- build against libboost-1.59.0.
