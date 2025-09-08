import frappe

def get_context(context):

    context.allow_guest = True
    return context

@frappe.whitelist()  # مهم علشان تقدر تناديها من js
def get_shipment_requests():
    data = frappe.get_all(
        "shipment_requests",
        fields=[
            "preliminary_number",
            "aci_number",
            "egyptian_importer",
            "foreign_exporter",
            "exporting_country",
            "country_icon",
            "request_type",
            "request_date",
            "shipment_type"
        ]
    )

    # تحويل الـ datetime/date إلى string
    for row in data:
        if row.get("request_date"):
            row["request_date"] = str(row["request_date"])

    return data