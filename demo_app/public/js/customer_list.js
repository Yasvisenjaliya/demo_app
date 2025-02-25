frappe.listview_settings['Customer'] = {
    onload: function (listview) {
        listview.page.add_inner_button(__('Custom Action'), function () {
            frappe.msgprint(__('Custom button clicked!'));
        });
    }
};
