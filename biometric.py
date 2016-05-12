# -*- coding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Enterprise Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://openerp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################


from openerp import fields,models


class biometric(models.Model):
    _name = 'biometric'
    _description = 'Biometrics'
    _rec_name = 'id'
#     def _check_fingers(self, cr, uid, ids, fingerprints=None, context=None):
#         print "_check_contacts: "+`fingerprints` + `ids`
#         objs = self.browse(cr, uid, ids, context=context)
#         for obj in objs:
#             if len(obj.fingerprints) < 2:
#                 return False
# 
#             # save name.. not sure where to do it :(
#             if not obj.name and obj.type_id and obj.type:
#                 n = False
#                 for o in self.pool.get('res.'+obj.type).browse(cr, uid, [obj.type_id]):
#                     n = o.name
#                 if n:
#                     self.write(cr, uid, ids, {'name':n})
# 
#         return True


    name = fields.Char('Name', size = 100) # person linked to
    type = fields.Char('Type', size = 50) # partner or user
    type_id = fields.Integer('ID link') # partner or user
    fingerprints =  fields.One2many('biometric.fingerprint', 'biometric_id','Fingerprints')
    last_scanned = fields.Date('Latest Confirmation', )
        ## fingerprint reader
        # 'fingerprint_data':fields.text('Fingerprint Data',),
    create_date = fields.Date('Date Created', readonly=True)
    create_uid = fields.Many2one('res.users', 'by User', readonly=True)
#     _constraints = [
#        (_check_fingers, 'Need at least 2 fingerprints registered', ['fingerprints']),
#     ]

# biometric()


class biometric_fingerprint(models.Model):
    _name = 'biometric.fingerprint'
    _description = 'Fingerprint'
    name = fields.Selection([
            ('r1','R1 - Right Thumb'),
            ('r2','R2 - Right Index'), 
            ('r2','R3 - Right Middle'), 
            ('r2','R4 - Right Ring'), 
            ('r2','R5 - Right Pinky'), 

            ('l1','L1 - Left Thumb'),
            ('l2','L2 - Left Index'), 
            ('l2','L3 - Left Middle'), 
            ('l2','L4 - Left Ring'), 
            ('l2','L5 - Left Pinky'), 

            ('O1','Other'),
            ], 'Finger', required=True)
    other = fields.Char('Other', help="eg. Left big toe", size=100)
    biometric_id = fields.Many2one('biometric', 'Biometric')
    fingerprint_data = fields.Text('Fingerprint',required=True)
    create_date = fields.Date('Date Registered', readonly=True)
    create_uid = fields.Many2one('res.users', 'by User', readonly=True)
    
# biometric_fingerprint()

# history of scans
class biometric_log(models.Model):
    _name = 'biometric.log'
    finger_id =fields.Many2one('biometric.fingerprint', 'Fingerprint') # link
    create_date = fields.Date('Date Scanned', readonly=True)
    create_uid = fields.Many2one('res.users', 'by User', readonly=True)
# biometric_log()
