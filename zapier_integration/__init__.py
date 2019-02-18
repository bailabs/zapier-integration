# Copyright (c) 2019, Bai Web and Mobile Lab and Contributors
# MIT License. See LICENSE
from __future__ import unicode_literals

import frappe

import json

__version__ = '1.0.0'


@frappe.whitelist()
def action(**form_dict):
    doctype = frappe.request.path.split('/api/method/zapier_integration.action/')[1]

    data = json.loads(form_dict['data'])
    data.update({'doctype': doctype})

    response = {}

    try:
        data = frappe.get_doc(data).insert().as_dict()
        response = {'data': data['name']}
    except frappe.DuplicateEntryError as e:
        frappe.local.response.http_status_code = 409
        frappe.log_error(frappe.get_traceback())

    return response
