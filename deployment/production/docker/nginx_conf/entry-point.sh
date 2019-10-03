#!/bin/env sh

if [ -z "$TARGET" ]; then
	export TARGET=/etc/nginx/sites-available
fi

echo "TARGET=$TARGET"

if [ ! -z "$ALWAYS_INIT" ] || [ ! -e "$TARGET/.init-lock" ]; then
	echo "Config data initialization."
	mkdir -p $TARGET
	cp -rf /config_source/* $TARGET
	date > "$TARGET/.init-lock"
	echo "Config data initialized."
else
	echo "Skipping initialization."
fi

exec "$@"
