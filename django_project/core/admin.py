__author__ = 'Irwan Fathurrahman <irwan@kartoza.com>'
__date__ = '18/02/20'

from django.contrib.gis import admin as gis_admin


class OSMGeoAdminSecure(gis_admin.OSMGeoAdmin):
    """
    Admin of using OSMGeoAdmin with https
    """
    openlayers_url = 'https://openlayers.org/api/2.13/OpenLayers.js'
    wms_url = 'https://vmap0.tiles.osgeo.org/wms/vmap0'
