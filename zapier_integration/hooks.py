# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "zapier_integration"
app_title = "Zapier Integration"
app_publisher = "Bai Web and Mobile Lab"
app_description = "A Frappe Integration to Zapier"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "iraltomera@bai.ph"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/zapier_integration/css/zapier_integration.css"
# app_include_js = "/assets/zapier_integration/js/zapier_integration.js"

# include js, css files in header of web template
# web_include_css = "/assets/zapier_integration/css/zapier_integration.css"
# web_include_js = "/assets/zapier_integration/js/zapier_integration.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "zapier_integration.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "zapier_integration.install.before_install"
# after_install = "zapier_integration.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "zapier_integration.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"zapier_integration.tasks.all"
# 	],
# 	"daily": [
# 		"zapier_integration.tasks.daily"
# 	],
# 	"hourly": [
# 		"zapier_integration.tasks.hourly"
# 	],
# 	"weekly": [
# 		"zapier_integration.tasks.weekly"
# 	]
# 	"monthly": [
# 		"zapier_integration.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "zapier_integration.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "zapier_integration.event.get_events"
# }

