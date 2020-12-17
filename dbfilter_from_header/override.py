# © 2013  Therp BV
# © 2014  ACSONE SA/NV
# Copyright 2018 Quartile Limited
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

import logging
import re
<<<<<<< HEAD
=======

>>>>>>> upstream/13.0
from odoo import http
from odoo.tools import config

db_filter_org = http.db_filter


def db_filter(dbs, httprequest=None):
    dbs = db_filter_org(dbs, httprequest)
    httprequest = httprequest or http.request.httprequest
<<<<<<< HEAD
    db_filter_hdr = httprequest.environ.get('HTTP_X_ODOO_DBFILTER')
=======
    db_filter_hdr = httprequest.environ.get("HTTP_X_ODOO_DBFILTER")
>>>>>>> upstream/13.0
    if db_filter_hdr:
        dbs = [db for db in dbs if re.match(db_filter_hdr, db)]
    return dbs


<<<<<<< HEAD
if config.get('proxy_mode') and \
   'dbfilter_from_header' in config.get('server_wide_modules'):
    _logger = logging.getLogger(__name__)
    _logger.info('monkey patching http.db_filter')
=======
if config.get("proxy_mode") and "dbfilter_from_header" in config.get(
    "server_wide_modules"
):
    _logger = logging.getLogger(__name__)
    _logger.info("monkey patching http.db_filter")
>>>>>>> upstream/13.0
    http.db_filter = db_filter
