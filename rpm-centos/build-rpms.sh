#!/bin/bash

yum -y install rpmdevtools yum-utils && \
rpmdev-setuptree && \
mv *.spec rpmbuild/SPECS/ && \
yum-builddep -y rpmbuild/SPECS/adoptopenjdk-repo.spec && \
spectool -g -R rpmbuild/SPECS/adoptopenjdk-repo.spec &&\
rpmbuild -ba rpmbuild/SPECS/adoptopenjdk-repo.spec
