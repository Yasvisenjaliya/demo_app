app_name = "demo_app"
app_title = "it is a demo app"
app_publisher = "dcode"
app_description = "it is a demo app"
app_email = "administrator@sigzen.com"
app_license = "mit"

# Apps

# from demo_app.config.config import test_string, test_list, test_dict

# print(test_string)
# print(test_list)
# print(test_dict)


# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "demo_app",
# 		"logo": "/assets/demo_app/logo.png",
# 		"title": "it is a demo app",
# 		"route": "/demo_app",
# 		"has_permission": "demo_app.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/demo_app/css/demo_app.css"
app_include_js = "/assets/demo_app/js/demo_app.js"

# include js, css files in header of web template
# web_include_css = "/assets/demo_app/css/custom_style.css"
# web_include_js = "/assets/demo_app/js/demo_app.js"
# web_routes = [
#     {"from_route": "/custom_page", "to_route": "custom_page"}
# ]


# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "demo_app/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"Student Form": "public/js/student.js"}
# webform_include_css = {"Student Form": "public/css/student.css"}

# include js in page
# page_js = {"student-web-form" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"Student" : "public/js/demo_app.js"}
# doctype_list_js = {"Student" : "public/js/demo_app.js"}
# doctype_tree_js = {"Employee" : "public/js/demo_app.js"}
# doctype_calendar_js = {"Task" : "public/js/demo_app.js"}

doctype_list_js = {
    "Student": "public/js/student_list.js",
    "Customer": "public/js/customer_list.js"
}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "demo_app/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
	# "methods": "demo_app.utils.jinja_methods",
	# "filters": "demo_app.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "demo_app.install.before_install"
# after_install = "demo_app.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "demo_app.uninstall.before_uninstall"
# after_uninstall = "demo_app.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "demo_app.utils.before_app_install"
# after_app_install = "demo_app.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "demo_app.utils.before_app_uninstall"
# after_app_uninstall = "demo_app.utils.after_app_uninstall"


# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "demo_app.notifications.get_notification_config"

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

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }



# demo_app/hooks.py





# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }


# doc_events = {
#     "Server Side Scripting": {
#         "validate": "demo_app.programing_module.doctype.server_side_scripting.events.send_email_on_validate"
#     }
# }

# doc_events = {
#     "Customize Student Doc": {
#         "validate": "demo_app.programing_module.events.validate_student"
#     }
# }
# /home/yasvi/frappe-bench/apps/demo_app/demo_app/hooks.py
# doc_events = {
#     "Customer": {
#         "before_save": "demo_app.programing_module.override.customer_count"  
#     }
# }

# doc_events = {
#     "Customer": {
#         "on_update": "demo_app.customer_event.override_customer_on_update"
#     }
# }





# DocType event hooks
# doc_events = {
#     "Create Student Record": {
#         "on_update": "demo_app.programming_module.doctype.create_student_record.create_student_record.create_student_with_courses"
#     }
# }



# Scheduled Tasks
# ---------------

# scheduler_events = {

#     "cron": {
#         "* * * * *": [
#             "demo_app.tasks.cron"
#         ]
#     },
# 	"all": [
# 		"demo_app.tasks.all"
# 	],
# 	"daily": [
# 		"demo_app.tasks.daily"
# 	],
# 	"hourly": [
# 		"demo_app.tasks.hourly"
# 	],
# 	"weekly": [
# 		"demo_app.tasks.weekly"
# 	],
# 	"monthly": [
# 		"demo_app.tasks.monthly"
# 	],
# }


scheduler_events = {
    "daily": [
        "demo_app.scheduler.daily_sequence_check"
    ]
}

# Testing
# -------

# before_tests = "demo_app.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "demo_app.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_class = {
# 	# "Task": "demo_app.task.get_dashboard_data"
#     "Student": "demo_app.programing_module.override.DCODEStudent",
# }

after_migrate = "demo_app.programing_module.setup.add_custom_fields"





# Include JS file in the app
doctype_js = {
    "Customer": "public/js/customer_action_buttons.js"  
}



# exempt linked doctypes from being automatical
# ly cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["demo_app.utils.before_request"]
# after_request = ["demo_app.utils.after_request"]

# Job Events
# ----------
# before_job = ["demo_app.utils.before_job"]
# after_job = ["demo_app.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"demo_app.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

fixtures = [
    "Library Member",
]


# sounds = [
#     {
#         "name": "ping", 
#         "src": "/assets/demo_app/sounds/ping.mp3",  # Correct path
#         "volume": 0.2  # Optional volume setting
#     }
# ]


# demo_app/hooks.py

# override_email_send = "demo_app.email.send_custom_email"


# demo_app/hooks.py

# email_append_to = "demo_app.email.send_custom_email"

# demo_app/hooks.py

# override_email_send = "demo_app.email.send_custom_email"

# demo_app/hooks.py

# get_sender_details = "demo_app.email.get_sender_details"


app_include = [
    "demo_app.api.student.create_student_with_subjects"
]


api = {
    "methods": [
        {"method": "demo_app.api.customer.get_customers", "type": "GET"}
    ]
}

