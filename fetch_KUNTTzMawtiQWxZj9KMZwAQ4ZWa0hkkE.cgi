#!/usr/bin/bash -ex

source "$(dirname $0)/conf"

[ -n "${CONTENT_LENGTH}" ] && dd bs=${CONTENT_LENGTH} > /dev/null

echo ${CONTENT_LENGTH}
echo hgua

echo -e 'Content-Type: text/html\n\n'

cd "$contentsdir"

git pull
