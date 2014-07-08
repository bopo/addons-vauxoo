#!/usr/bin/python
# -*- encoding: utf-8 -*-
###########################################################################
#    Module Writen to OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Vauxoo (<http://vauxoo.com>).
#    All Rights Reserved
###############Credits######################################################
#    Coded by: Juan Carlos Funes(juan@vauxoo.com)
#############################################################################
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
################################################################################

{
    "name" : "Creacion de Attachment en la Factura Electronica para Mexico (CFD,CFDI,CBB)",
    "version" : "1.0",
    "author" : "Vauxoo",
    "category" : "Localization/Mexico",
    "description" : """This module creates attachment for Invoice(CFD,CFDI,CBB)
    """,
    "website" : "http://www.vauxoo.com/",
    "license" : "AGPL-3",
    "depends" : ["account", "mail", "email_template",
                "l10n_mx_facturae_seq",
                "l10n_mx_facturae_report",
                "email_template_multicompany",
                "l10n_mx_facturae_groups",
                "account_cancel",
                "l10n_mx_facturae_lib",
                "l10n_facturae_groups_multipac_vauxoo"
        ],
    "demo" : [],
    "data" : [
        "security/l10n_mx_ir_attachment_facturae_security.xml",
        "security/ir.model.access.csv",
        "security/l10n_mx_facturae_multipac_security_ir_rules.xml",
        "ir_attachment_facturae_view.xml",
        "l10n_mx_facturae_workflow.xml",
        "l10n_mx_facturae_mail_server_data.xml",
        "res_config.xml",
        "test/update_type-to-pac.yml",
        "data/l10n_mx_facturae_email_data.xml",
    ],
    "installable" : True,
    "active" : False,
}
