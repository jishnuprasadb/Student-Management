# Copyright (c) 2025, Jishnu Prasad and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class StudentEnrollment(Document):
	def before_submit(self):
		if not self.student_name:
			frappe.throw("Student Name is required before submission.")

		if not self.course:
			frappe.throw("Course is required before submission.")

		if not self.email:
			frappe.throw("Email is required before submission.")

		#Check for duplicate email in the system
		#Additional check
		if frappe.db.exists("Student Enrollment", {"email": self.email, "name": ("!=", self.name)}):
			frappe.throw("A student with this email already exists. Please use a unique email.")