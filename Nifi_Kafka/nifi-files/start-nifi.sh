#!/bin/sh -e
cp ../../../home/docker/docker-share/nifi-social-media-nar-1.9.2.nar ./lib/nifi-social-media-nar-1.9.2.nar
cp ../../../home/docker/docker-share/hdfs-site.xml ./lib/hdfs-site.xml
cp ../../../home/docker/docker-share/core-site.xml ./lib/core-site.xml
../scripts/start.sh