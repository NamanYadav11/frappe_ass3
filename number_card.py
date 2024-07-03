import frappe
@frappe.whitelist()
def totalSalesOrder():
    return frappe.db.count("Sales Order",{'docstatus':1})