import frappe
import logging

logger = logging.getLogger(__name__)

def get_context(context):
    context.allow_guest = True
    return context

@frappe.whitelist(allow_guest=True)
def get_shipment_files(shipment_request):
    logger.info(f"Request received: {frappe.request.method} {frappe.request.path}")
    doc = frappe.get_doc("shipment_requests", str(shipment_request),
    fields=["files"]
    )
    return doc


@frappe.whitelist(allow_guest=True)
def get_shipment_requests(aci_number):
    logger.info(f"Request received: {frappe.request.method} {frappe.request.path}")
     # جلب كل البيانات من الـ doctype
    shipment_requests = frappe.get_all(
        'shipment_requests',  # اسم الـ Doctype بالضبط
        filters={'aci_number': aci_number},
        fields=["shipment_number",
  "shipmentname",
  "address",
  "mobile_number",
  "egyptian",
  "national_id_passport_number",
  "factory_number",
  "national_id_expiry_date",
  "country",
  "type_of_registration",
  "registration_number",
  "registration_expiry_date",
  "sub_type",
  "ledger",
  "date_46",
  "declared_value",
  "applicant",
  "mobile_number_for_communication",
  "email",
  "applicants_title_format",
  "statement_presenter",
  "statement_presenters_role",
  "affiliated_to",
  "tariff_application_date",
  "previous_importer",
  "joint_inspection_date",
  "truck_release_date",
  "shipment_link_type",
  "shipping_date",
  "compatible_customs_system",
  "current_customs_system",
  "tariff_sector",
  "submission_system",
  "previous_customs_system",
  "customs_complex",
  "registration_customs",
  "goods_arrival_customs",
  "final_release_customs",
  "goods_delivery_location",
  "warehouse_transport_storage",
  "for_entity",
  "inspection_description",
  "client_attendance_date_for_inspection",
  "number_of_transfer_parties",
  "insertion_location",
  "first_save_date",
  "saved_by",
  "last_save_date",
  "aci_request_date",
  "aci_issue_date",
  "submission_date",
  "status",
  "declaration_stage",
  "postal_parcel_indicator",
  "operator_registered_in_e_invoice_system",
  "operator_registered_in_white_list",
  "exit_indicator_for_included_goods_without_containers",
  "completion_of_endorsement",
  "full_fee_payment_in_phase_one",
  "disbursement_visa",
  "article_104c_commitment",
  "request_exit_transport",
  "inspection_and_examination_rate",
  "specialized_committees",
  "request_type3",
  "sufficiency_of_submitted_documents",
  "is_the_incoming_message_stock",
  "is_the_incoming_message_under_suspicion",
  "is_the_message_in_a_wooden_box_thickness_gt_6mm",
  "guided_goods_for_free_zone",
  "goods_for_free_zone",
  "is_the_incoming_message_used_or_waste",
  "policy_number",
  "policy_date",
  "road_number",
  "linked_to_main_policy",
  "port_of_loading",
  "port_of_arrival",
  "final_destination",
  "arrival_date",
  "departure_date_from_exporting_country",
  "shipment_destination_type",
  "last_location",
  "shipping_agent",
  "transport_name",
  "beneficiary_name",
  "number_of_waiver_requests",
  "shipment_number2",
  "sub_number",
  "shipment_date",
  "invoice_number",
  "invoice_date",
  "contract_type_according_to_principal",
  "contract_date",
  "preliminary_invoice_number",
  "preliminary_invoice_date",
  "purchase_order_or_contract_number",
  "purchase_order_or_contract_date",
  "original_invoice_value",
  "currency",
  "central_bank_rate_indicator",
  "customs_exchange_rate",
  "central_bank_exchange_rate",
  "local_invoice_value",
  "number_of_invoice_items",
  "address_invoice",
  "exporter_type",
  "foreign_supplier_nationality",
  "aci_checked",
  "inquiry_date",
  "shipment_description",
  "last_modified_date",
  "payment_method",
  "bank_handling_the_transfer",
  "payment_type",
  "due_date"
  ]  # غير الحقول حسب اللي عندك
    )
    if shipment_requests:
        return shipment_requests[0]  # بما إنه Unique، هيرجع عنصر واحد
    else:
        return {}  # لو مفيش سجل مطابق



@frappe.whitelist(allow_guest=True)
def get_shipment_shipment_details(aci_number):
    shipment = frappe.get_all(
        'shipment_requests',
        filters={'aci_number': aci_number},
        fields=['name']
    )

    if not shipment:
        return {"shipment_details": [], "parcels_required_for_inspection": [],"item_data":[],"invoice_items":[],"invoice_expenses":[],"acid_items_without_invoice":[]}

    shipment_name = shipment[0].name
    doc = frappe.get_doc('shipment_requests', shipment_name)

    # جدول الشحنات
    shipment_details = []
    for i, row in enumerate(doc.shipment_details, start=1):
        shipment_details.append({
            "idx": i,
            "shipment_type": row.shipment_type or "",
            "shipment_destination_type": row.shipment_destination_type or "",
            "general_description_of_goods": row.general_description_of_goods or "",
            "freezing_status": row.freezing_status or "",
            "container_code": row.container_code or "",
            "number_of_packages": row.number_of_packages or "",
            "package_unit": row.package_unit or "",
            "gross_weight": row.gross_weight or "",
            "weight_unit": row.weight_unit or "",
            "shipping_line": row.shipping_line or "",
            "status": row.status or "",
            "discharge_date": row.discharge_date or "",
            "required_for_xray_inspection": row.required_for_xray_inspection or "",
            "xray_inspection_result": row.xray_inspection_result or ""
        })

    # جدول الطرود المطلوبة للفحص
    parcels_required_for_inspection = []
    for i, row in enumerate(doc.parcels_required_for_inspection, start=1):
        parcels_required_for_inspection.append({
            "idx": i,
            "container_code": row.container_code or "",
            "customs_seal_for_containers": row.customs_seal_for_containers or "",
            "gross_weight": row.gross_weight or "",
            "weight_unit": row.weight_unit or "",
            "number_of_packages": row.number_of_packages or "",
            "package_unit": row.package_unit or "",
            "discharge_date": row.discharge_date or "",
            "required_by_customs": "✔" if row.required_by_customs else "",
            "required_by_inspection": "✔" if row.required_by_inspection else "",
            "required_by_safety_authority": "✔" if row.required_by_safety_authority else "",
            "required_for_xray_inspection": "✔" if row.required_for_xray_inspection else "",
            "xray_inspection_result": row.xray_inspection_result or "",
            "general_description_of_goods": row.general_description_of_goods or ""
        })
    item_data = []
    for i, row in enumerate(doc.item_data, start=1):
       item_data.append({
            "idx": i,
            "item_serial_number": row.item_serial_number or "",
            "item_number": row.item_number or "",
            "item_number_at_exporter_or_other_systems": row.item_number_at_exporter_or_other_systems or "",
            "detailed_item_description": row.detailed_item_description or "",
            "tariff_code": row.tariff_code or "",
            "country_of_origin": row.country_of_origin or "",
            "purpose_of_use": row.purpose_of_use or "",
            "tariff_code_according_to_exporter": row.tariff_code_according_to_exporter or "",
            "tariff_code_according_to_aci": row.tariff_code_according_to_aci or "",
            "invoice_item_serial": row.invoice_item_serial or "",
            "item_according_to_appraiser": row.item_according_to_appraiser or "",
            "quantity": row.quantity or "",
            "quantity_unit": row.quantity_unit or "",
            "weight": row.weight or "",
            "weight_unit": row.weight_unit or "",
            "engine_number_indicator": row.engine_number_indicator or "",
            "inspection_visa": row.inspection_visa or "",
            "shortage_or_surplus_quantity": row.shortage_or_surplus_quantity or "",
            "goeic_result": row.goeic_result or "",
            "nfsa_result": row.nfsa_result or "",
            "ntra_result": row.ntra_result or "",
        })
    invoice_items = []
    for i, row in enumerate(doc.invoice_items, start=1):
            invoice_items.append({
                "idx": i,
                "customs_item_serial": row.customs_item_serial or "",
                "customs_edit_or_add": row.customs_edit_or_add or "",
                "tariff_code": row.tariff_code or "",
                "tariff_description": row.tariff_description or "",
                "gross_weight": row.gross_weight or "",
                "net_weight": row.net_weight or "",
                "weight_unit": row.weight_unit or "",
                "customs_quantity": row.customs_quantity or "",
                "customs_quantity_unit": row.customs_quantity_unit or "",
                "statistical_quantity": row.statistical_quantity or "",
                "statistical_quantity_unit": row.statistical_quantity_unit or "",
                "invoice_item_price": row.invoice_item_price or "",
                "invoice_currency": row.invoice_currency or "",
                "item_description": row.item_description or "",
                "country_of_origin": row.country_of_origin or "",
                "is_item_modified": row.is_item_modified or "",
                "inspector_description": row.inspector_description or "",
                "inspection_visa": row.inspection_visa or "",
                "shortage_or_surplus_quantity": row.shortage_or_surplus_quantity or "",
            })
        
    invoice_expenses = []
    for i, row in enumerate(doc.invoice_expenses, start=1):
            invoice_expenses.append({
                "idx": i,
                "expense_type": row.expense_type or "",
                "value_or_percentage": row.value_or_percentage or "",
                "percentage": row.percentage or "",
                "expense_value": row.expense_value or "",
                "expense_currency": row.expense_currency or "",
                "exchange_rate": row.exchange_rate or "",
                "local_value": row.local_value or "",
            })
    acid_items_without_invoice = []
    for i, row in enumerate(doc.acid_items_without_invoice, start=1):
        acid_items_without_invoice.append({
            "idx": i,
            "tariff_code": row.tariff_code or "",
            "country_of_origin": row.country_of_origin or "",
            "purpose_of_use": row.purpose_of_use or "",
            "exporter_code": row.exporter_code or "",
            "exporter_name": row.exporter_name or "",
            "quantity": row.quantity or "",
            "quantity_unit": row.quantity_unit or "",
            "value_in_foreign_currency": row.value_in_foreign_currency or "",
            "currency": row.currency or "",
            "value_in_local_currency": row.value_in_local_currency or "",
        })
       
    return {
        "shipment_details": shipment_details,
        "parcels_required_for_inspection": parcels_required_for_inspection,
        "item_data":item_data,
        "invoice_items":invoice_items,
        "invoice_expenses":invoice_expenses,
        "acid_items_without_invoice":acid_items_without_invoice
    }

