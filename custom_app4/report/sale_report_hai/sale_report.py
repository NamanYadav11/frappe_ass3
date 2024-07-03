import frappe
def execute(filters=None):
    columns, data = [], []
    # Define columns
    columns = [
        {"label": "Customer Name", "fieldname": "customer_name", "fieldtype": "Data", "width": 150},
        {"label": "Sales Order", "fieldname": "sales_order", "fieldtype": "Link", "options": "Sales Order", "width": 150},
        {"label": "Delivery Date", "fieldname": "delivery_date", "fieldtype": "Date", "width": 120},
        {"label": "Item Code", "fieldname": "item_code", "fieldtype": "Link", "options": "Item", "width": 120},
        {"label": "Item Name", "fieldname": "item_name", "fieldtype": "Data", "width": 150},
        {"label": "Item Qty", "fieldname": "item_qty", "fieldtype": "Float", "width": 100},
    ]
    # Fetch data
    data = frappe.db.sql('''
        SELECT
            so.customer_name, so.name as sales_order, soi.delivery_date,
            soi.item_code, soi.item_name, soi.qty as item_qty
        FROM
            `tabSales Order` so
        INNER JOIN
            `tabSales Order Item` soi ON soi.parent = so.name
        WHERE
            so.docstatus = 1
        ''', as_dict=True)
    return columns, data