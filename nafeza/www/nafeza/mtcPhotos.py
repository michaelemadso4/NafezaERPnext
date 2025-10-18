import frappe

def get_context(context):
    context.allow_guest = True
    return context

@frappe.whitelist()
def get_shipment_files(shipment_request):
    doc = frappe.get_doc("shipment_requests", str(shipment_request),
    fields=["files"]
    )
    return doc

@frappe.whitelist(allow_guest=True)
def getShipment_data(shipment_request):
    doc = frappe.get_doc("shipment_requests", str(shipment_request),)

    return doc
