#!/bin/bash
MYDATE=`date +%d-%B-%Y`
MONTH=$(date +%B)
YEAR=$(date +%Y)
cd /home/web/mezzanine.kartoza.com/deployment
MYBASEDIR=`pwd`/backups
MYBACKUPDIR=${MYBASEDIR}/${YEAR}/${MONTH}
mkdir -p ${MYBACKUPDIR}

cd ${MYBACKUPDIR}
docker exec -ti mezzanine-db /bin/bash -c "PGPASSWORD=docker pg_dump -Fc -f /tmp/latest.dmp -h localhost -U docker gis"
docker cp mezzanine-db:/tmp/latest.dmp PG_mezzanine-${MYDATE}.dmp

cd -
rm backups/latest.dmp

cd backups
ln -s ${MYBACKUPDIR}/PG_mezzanine-${MYDATE}.dmp latest.dmp

cd ..
