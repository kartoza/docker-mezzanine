#!/bin/bash

echo "Use this to tag a version on your local"
echo "machine, push the tag upstream and then"
echo "deploy it to the remote"
echo "e.g."
echo "$0 version-1.2.3"
VERSION=$1
make dbbackup
make mediasync
git tag $VERSION
git push --tags upstream 
ssh mezzanine "cd /home/timlinux/mezzanine.kartoza.com/deployment && git fetch --tags && git checkout $VERSION && make build && make kill && make web && make migrate && make collectstatic && make reload"
