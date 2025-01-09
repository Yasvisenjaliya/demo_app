// Copyright (c) 2025, dcode and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Student Marks", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on('Student Marks', {
    validate: function (frm) {
        let hasNegativeMarks = false;

        frm.doc.marks_table.forEach(row => {
            if (row.marks < 0) {
                hasNegativeMarks = true;
                frappe.msgprint({
                    title: __('Validation Error'),
                    indicator: 'red',
                    message: __('Marks cannot be negative in row {0}', [row.idx])
                });
            }
        });

        if (hasNegativeMarks) {
            frappe.validated = false;
        }
    }
});
