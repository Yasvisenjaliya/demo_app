frappe.query_reports["Practice"] = {
	"filters": [
		{
			"fieldname": "subject",
			"label": __("Subject"),
			"fieldtype": "Link",
			"options": "Subject",
			"default": "",
			"mandatory": 1
		},
		{
			"fieldname": "student",
			"label": __("Student"),
			"fieldtype": "Link",
			"options": "Student",
			"default": "",
			"mandatory": 1
		}
	],
	"columns": [
		{
			"label": __("Student Name"),
			"fieldname": "name",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": __("First Name"),
			"fieldname": "first_name",
			"fieldtype": "Data",
			"width": 150
		},
		{
			"label": __("Email"),
			"fieldname": "email",
			"fieldtype": "Data",
			"width": 200
		},
		{
			"label": __("Grade"),
			"fieldname": "grade",
			"fieldtype": "Data",
			"width": 100
		}
	]
};
