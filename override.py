import frappe
from erpnext.selling.doctype.sales_order.sales_order import SalesOrder as Original
class CustomSO(Original):
    def onload(self):
        frappe.msgprint("New Function overriden")
        super(CustomSO,self).onload()