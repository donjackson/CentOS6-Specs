# CentOS6-Specs
Spec Files for custom-built CentOS/RHEL 6 RPMs

To build **libboost-1.59.0**:
$ `scl enable devtoolset-7 bash`
$ `rpmbuild -ba SPECS/libboost-1.59.0.spec`

To build **vowpal-wabbit-8.5.0**:
$ `rpm -ivh libboost-*`
$ `QA_RPATHS=$[ 0x0002 ] rpmbuild -ba SPECS/vowpal-wabbit-8.5.0.spec`
