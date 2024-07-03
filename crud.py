import frappe
@frappe.whitelist()
def get_user():
    data=frappe.get_all('User', fields=['*'])
    return data
@frappe.whitelist()
def create_user():
    try:
        data=frappe.local.form_dict
        if frappe.db.exists('User', data.email):
            frappe.throw("User already exist")
        data=frappe.get_doc({
            'doctype':'User',
            **data
        })
        data.insert()
        frappe.db.commit()
        return data
    except Exception as e:
        raise frappe.error_log(500,"Error creating user: {e}")
@frappe.whitelist()
def update_user():
    try:
        data=frappe.local.form_dict
        if data.name:
            file=frappe.get_doc('User',data.name)
            file.update(data)
            file.save()
            frappe.db.commit()
            return file
        else:
            raise frappe.error_log(404,"Name not found")
    except Exception as e:
        raise frappe.error_log(500,"Error updating user: {e}")
@frappe.whitelist()
def delete_user():
    try:
        data=frappe.local.form_dict
        if data.name:
            frappe.delete_doc('User', data.name)
            frappe.db.commit()
            return "File deleted"
        else:
            raise frappe.error_log(404,"Name not found")
    except Exception as e:
        raise frappe.error_log(500,"Error deleting user: {e}")