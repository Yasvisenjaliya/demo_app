frappe.listview_settings['Student'] = {
    add_fields: ["status"], 
    get_indicator: function (doc) {
        if (doc.status === "Active") {
            return ["Active", "green", "status,=,Active"];
        } else if (doc.status === "Inactive") {
            return ["Inactive", "red", "status,=,Inactive"];
        } else {
            return ["Unknown", "gray", "status,=,Unknown"];
        }
    }
};
