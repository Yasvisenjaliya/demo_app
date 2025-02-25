frappe.ui.form.on('Create Student Record', {
    refresh: function (frm) {
        // Custom actions when the form is refreshed
        frm.add_custom_button(__('Save and Send'), function () {
            // Custom logic to send email or perform some other task
        });
    },
    validate: function (frm) {
        // Custom form validation logic
        if (!frm.doc.email) {
            frappe.msgprint(__('Please enter an email address.'));
            frappe.validated = false;
        }
    }
});
// demo_app / demo_app / programing_module / doctype / create_student_record / create_student_record.js