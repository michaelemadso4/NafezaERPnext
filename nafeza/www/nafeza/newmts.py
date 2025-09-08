import frappe

@frappe.whitelist()
def get_shipment_files(shipment_request):
    doc = frappe.get_doc("shipment_requests", str(shipment_request),
    fields=["files"]
    )
    return doc

