import base64
from .models import *
from odoo import api

def pre_init_hook(cr):
    from odoo import registry
    db_registry = registry(cr.dbname)
    env = api.Environment(cr, 1, {})
    for attachment in env['ir.attachment'].with_context(active_test=False).search([]):
        datas = base64.b64decode(attachment.datas)
        env.cr.execute("update ir_attachment set store_fname = null, db_datas = %s where id =%s", (datas, attachment.id))
    
