FROM busybox

VOLUME ["/config_source"]
ADD sites-available /config_source
ADD entry-point.sh /entry-point.sh

ENTRYPOINT ["/entry-point.sh"]
