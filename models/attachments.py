from odoo import _, api, fields, models, SUPERUSER_ID
from odoo.exceptions import UserError, RedirectWarning, ValidationError
class Attachment(models.Model):
    _inherit = 'ir.attachment'

    