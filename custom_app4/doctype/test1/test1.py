# Copyright (c) 2024, naman and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class test1(Document):
	def before_save(self):
		if self.first_name and self.last_name and self.check:
			self.full_name = self.first_name+" "+self.last_name