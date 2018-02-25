#!/bin/bash

echo "Use this to tag a version on your local"
echo "machine, push the tag upstream and then"
echo "deploy it to the remote"
echo "e.g."
echo "$0 1.2.3"
VERSION=$1
echo "Last tag on your local system is:"
git tag | grep -v version | sort --version-sort | tail -1
echo "New tag to be added to your local repo and pushed upstream:"
echo $VERSION
read -p "Are you sure you want to continue? " -n 1 -r
echo    # (optional) move to a new line
if [[ $REPLY =~ ^[Yy]$ ]]
then
    VERSION=$1
    # Get the latest backups and media from production
    make dbbackup
    make mediasync
    # Sync the latest backups and media to staging from production
    rsync -L  backups/latest.dmp staging.kartoza.com:/home/web/staging.kartoza.com/deployment/backups/
    rsync -r -v media/ staging.kartoza.com:/home/web/staging.kartoza.com/deployment/media
    # Tag the release and push to main repo
    # .version is used by Raven/Sentry
    echo $VERSION > ../django_project/.version
    git reset HEAD *
    git add ../django_project/.version
    git commit -m "bump to version ${VERSION}"
    git tag $VERSION
    git push --tags upstream develop
    # Check it out on the server
    # No migrations are run - you should do that manually for now
    ssh kartoza4 "cd /home/web/kartoza.com/deployment && git fetch --tags && git checkout $VERSION && make build && make kill && make web && make migrate && make collectstatic && make reload"
else
    echo "Tag and deploy to staging aborted."
fi