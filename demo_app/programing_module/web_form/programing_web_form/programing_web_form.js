frappe.ready(function () {
	// bind events here
	// frappe.msgprint('Please fill all value')
	frappe.web_form.after_load = () => {
		frappe.web_form.on('enable', (field, value) => {
			frappe.msgprint('Hi User');
		})
		
	}


})