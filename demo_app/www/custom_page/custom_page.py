import frappe
from frappe.website.website_generator import WebsiteGenerator

class CustomPage(WebsiteGenerator):
    def get_context(self, context):
        context.title = "Custom Page Title"
        context.custom_message = "This is a custom message displayed on the page."
        return context
