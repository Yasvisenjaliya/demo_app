// /home/yasvi/frappe-bench/apps/demo_app/demo_app/public/js/customer_action_buttons.js
frappe.ui.form.on('Customer', {
    onload: function (frm) {
        
        setTimeout(() => {
            $('.btn[aria-expanded="false"][data-toggle="dropdown"]').each(function () {
                if ($(this).text().trim() === __("Actions")) {
                    $(this).hide();
                }
            });
        });
    }
});
