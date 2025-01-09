// Copyright (c) 2025, dcode and contributors
// For license information, please see license.txt

frappe.query_reports["Server Side Scripting Script Report"] = {
	"filters": [
		{
			"fieldname": "name",
			"label": ("Server Side Scripting"),
			"fieldtype": "Link",
			"options": "Server Side Scripting"
		},
		{
			"fieldname": "dob",
			"label": ("DOB"),
			"fieldtype": "Date",
		},
		{
			"fieldname": "age",
			"label": ("Age"),
			"fieldtype": "Int",
		}

	]
};
