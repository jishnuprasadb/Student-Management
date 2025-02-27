# Copyright (c) 2025, Jishnu Prasad and Contributors
# See license.txt

# import frappe


import frappe
from frappe.tests.utils import FrappeTestCase

class TestStudentEnrollment(FrappeTestCase):

    def setUp(self):
        """Set up test data before running tests"""
        frappe.flags.args = frappe._dict()


    def test_missing_required_fields(self):
        """Test validation for missing required fields"""
        # Missing student_name
        enrollment1 = frappe.get_doc({
            "doctype": "Student Enrollment",
            "course": "Java",
            "email": "no_name@example.com",
            "enrollment_date":"2025-01-15"

        })
        with self.assertRaises(frappe.ValidationError) as context:
            enrollment1.before_submit()
        self.assertEqual(str(context.exception), "Student Name is required before submission.")

        # Missing course
        enrollment2 = frappe.get_doc({
            "doctype": "Student Enrollment",
            "student_name": "No Course Student",
            "email": "no_course@example.com",
            "enrollment_date":"2025-01-15"

        })
        with self.assertRaises(frappe.ValidationError) as context:
            enrollment2.before_submit()
        self.assertEqual(str(context.exception), "Course is required before submission.")

        # Missing email
        enrollment3 = frappe.get_doc({
            "doctype": "Student Enrollment",
            "student_name": "No Email Student",
            "course": "Java",
            "enrollment_date":"2025-01-15"

        })
        with self.assertRaises(frappe.ValidationError) as context:
            enrollment3.before_submit()
        self.assertEqual(str(context.exception), "Email is required before submission.")


    def test_duplicate_email(self):
        """Test that duplicate email is not allowed"""
        # Create the first student enrollment
        enrollment1 = frappe.get_doc({
            "doctype": "Student Enrollment",
            "student_name": "First Student",
            "course": "Java",
            "email": "duplicate@example.com",
            "enrollment_date":"2025-01-15"

        }).insert(ignore_permissions=True)

        # Try creating another enrollment with the same email
        enrollment2 = frappe.get_doc({
            "doctype": "Student Enrollment",
            "student_name": "Second Student",
            "course": "Java",
            "email": "duplicate@example.com",
            "enrollment_date":"2025-01-15"

        })
        
        # Attempt to insert and submit the duplicate record
        enrollment2.insert(ignore_permissions=True)
        
        with self.assertRaises(frappe.ValidationError) as context:
            enrollment2.submit()  # This should trigger before_submit()

        self.assertEqual(str(context.exception), "A student with this email already exists. Please use a unique email.")
