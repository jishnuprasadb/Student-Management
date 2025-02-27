// Copyright (c) 2025, Jishnu Prasad and contributors
// For license information, please see license.txt

frappe.ui.form.on("Student Enrollment", {
    validate: function(frm) {
        // validate email
        if (frm.doc.email && !validate_email(frm.doc.email)) {
            frappe.msgprint(__('Please enter a valid email address.'));
            frappe.validated = false;
        }
        // validate enrollment date
        if (frm.doc.enrollment_date && frappe.datetime.get_today() < frm.doc.enrollment_date) {
            frappe.msgprint(__('Enrollment Date cannot be a future date.'));
            frappe.validated = false;
        }   
    }
});


function validate_email(email) {
    var email_regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return email_regex.test(email);
}
