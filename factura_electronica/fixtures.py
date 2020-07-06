# -*- coding: utf-8 -*-
#  Si Hay Sistema and Contributors 2020
from __future__ import unicode_literals
from . import __version__ as app_version

"""
en-US: Make sure all fields that are coming from another branch and the new fields you require are added to the fixtures
list.
es-GT: Asegurate que todos los fixtures que vengan de otra rama y los
nuevos fixtures que estes creando se agreguen al listado fixtures.

"""

def fill_fixtures():
    # We declare fixtures as an empty list.
    fixtures_fillup = []

    # Add the corresponding fields to the fixture objects
    # if the object does not exist, simply create it and copy accordingly.

    custom_field = {
        "dt": "Custom Field", "filters": [
            [
                "name", "in", [
                    "Purchase Invoice-supplier_invoice_prefix",
                    "Contact-valid_identifications",
                    "Contact-identifications",
                    "Quotation-facelec_qt_nit",
                    "Otros Impuestos Factura Electronica-cost_center",
                    "UOM-faceleccodigo_unidad_de_medida",
                    "Sales Taxes and Charges Template-facelec_default_excise_tax",
                    "Supplier-facelec_nit_proveedor",
                    "Purchase Invoice-facelec_nit_fproveedor",
                    "Purchase Taxes and Charges Template-facelect_default_when_excise_taxes_present",
                    "Sales Taxes and Charges-tax_name",
                    "Purchase Order-facelec_po_nit",
                    "Supplier Quotation-shs_spq_nit",
                    "Purchase Invoice-es_factura_especial",
                    "Sales Invoice-appointment",
                    "Sales Taxes and Charges-taxable_unit_code",
                    "Purchase Receipt-facelec_nit_prproveedor",
                    "Sales Order-shs_so_nit",
                    "Delivery Note-shs_dn_nit",
                    "Sales Invoice-es_nota_de_debito",
                    "Item-facelec_three_digit_uom",
                    "Sales Invoice-facelec_factura_asociada",
                    "Customer-nit_face_customer",
                    "Sales Invoice-serie_original_del_documento",
                    "Company-nit_face_company",
                    "Sales Invoice-shs_numero_resolucion",
                    "Address-tax_category",
                    "Journal Entry-tipo_poliza",
                    "Quotation Item-facelec_qt_three_digit_uom_code",
                    "Sales Invoice Item-facelec_three_digit_uom_code",
                    "Delivery Note Item-shs_three_digit_uom_code",
                    "Sales Order Item-shs_so_three_digit_uom_code",
                    "Purchase Order Item-facelec_po_three_digit_uom_code",
                    "Purchase Invoice Item-facelec_p_purchase_three_digit",
                    "Sales Invoice-cae_factura_electronica",
                    "Sales Invoice-nit_face_customer",
                    "Sales Invoice-cae_nota_de_credito",
                    "Purchase Receipt Item-facelec_pr_purchase_three_digit",
                    "Supplier Quotation Item-shs_spq_three_digit_uom_code",
                    "Sales Invoice-cae_nota_de_debito",
                    "Sales Invoice-numero_autorizacion_fel",
                    "Purchase Invoice Item-shs_amount_for_back_calc",
                    "Sales Invoice Item-shs_amount_for_back_calc",
                    "Delivery Note Item-shs_amount_for_back_calc",
                    "Purchase Receipt Item-shs_amount_for_back_calc",
                    "Supplier Quotation-guatemala_tax",
                    "Supplier Quotation-shs_spq_gt_tax_fuel",
                    "Supplier Quotation-guatemala_spq_tax_or_good",
                    "Supplier Quotation-shs_spq_gt_tax_goods",
                    "Supplier Quotation-guatemala_spq_good_or_service",
                    "Supplier Quotation-shs_spq_gt_tax_services",
                    "Supplier Quotation Item-excise_tax_calculation",
                    "Quotation-shs_qt_otros_impuestos",
                    "Supplier Quotation-shs_spq_total_iva",
                    "Supplier Quotation Item-shs_spq_tax_rate_per_uom",
                    "Quotation-shs_tax_quotation",
                    "Supplier Quotation Item-shs_spq_tax_rate_per_uom_account",
                    "Quotation-shs_qt_total_otros_imp_incl",
                    "Supplier Quotation Item-shs_spq_other_tax_amount",
                    "Supplier Quotation Item-shs_spq_break",
                    "Quotation-guatemala_tax",
                    "Quotation-facelec_qt_gt_tax_fuel",
                    "Supplier Quotation Item-shs_spq_amount_minus_excise_tax",
                    "Delivery Note Item-shs_dn_excise_tax_calculation_section",
                    "Sales Invoice Item-section_break_55",
                    "Quotation-guatemala_qt_tax_or_good",
                    "Supplier Quotation Item-shs_spq_sales_tax_for_this_row",
                    "Delivery Note Item-shs_dn_tax_rate_per_uom",
                    "Supplier-guatemala_tax_category",
                    "Sales Order Item-excise_tax_calculation_shs",
                    "Quotation-facelec_qt_gt_tax_goods",
                    "Sales Invoice Item-facelec_tax_rate_per_uom",
                    "Supplier Quotation Item-type_of_expense_for_tax_purposes",
                    "Delivery Note Item-shs_dn_other_tax_amount",
                    "Quotation-guatemala_qt_good_or_service",
                    "Sales Invoice Item-facelec_tax_rate_per_uom_account",
                    "Supplier Quotation Item-shs_spq_gt_tax_net_fuel_amt",
                    "Delivery Note Item-shs_dn_tax_rate_per_uom_account",
                    "Sales Order Item-shs_so_tax_rate_per_uom",
                    "Quotation-facelec_qt_gt_tax_services",
                    "Supplier Quotation Item-shs_spq_gt_tax_net_goods_amt",
                    "Sales Invoice Item-facelec_other_tax_amount",
                    "Delivery Note Item-col_break_dn",
                    "Sales Order Item-shs_so_other_tax_amount",
                    "Quotation-facelec_qt_total_iva",
                    "Sales Invoice Item-col_break_6",
                    "Supplier Quotation Item-shs_spq_gt_tax_net_services_amt",
                    "Sales Order Item-shs_so_tax_rate_per_uom_account",
                    "Delivery Note Item-shs_dn_amount_minus_excise_tax",
                    "Supplier Quotation Item-tax_type_column_break",
                    "Sales Invoice Item-facelec_amount_minus_excise_tax",
                    "Delivery Note Item-shs_dn_sales_tax_for_this_row",
                    "Sales Order Item-col_break_so_shs",
                    "Purchase Receipt-guatemala_tax_pr",
                    "Purchase Invoice Item-section_break_p1",
                    "Sales Invoice Item-facelec_sales_tax_for_this_row",
                    "Supplier Quotation Item-shs_spq_is_fuel",
                    "Delivery Note Item-type_of_expense_for_tax_purposes_dn",
                    "Sales Order Item-shs_so_amount_minus_excise_tax",
                    "Purchase Receipt-facelec_pr_gt_tax_fuel",
                    "Sales Order-guatemala_tax",
                    "Purchase Invoice Item-facelec_p_tax_rate_per_uom",
                    "Sales Invoice Item-type_of_expense_for_tax_purposes",
                    "Supplier Quotation Item-shs_spq_is_good",
                    "Delivery Note Item-shs_dn_gt_tax_net_fuel_amt",
                    "Sales Order Item-shs_so_sales_tax_for_this_row",
                    "Purchase Receipt-guatemala_tax_or_good_pr",
                    "Sales Order-shs_gt_tax_fuel",
                    "Purchase Invoice Item-facelec_p_other_tax_amount",
                    "Sales Invoice Item-facelec_gt_tax_net_goods_amt",
                    "Supplier Quotation Item-shs_spq_is_service",
                    "Delivery Note Item-shs_dn_gt_tax_net_goods_amt",
                    "Sales Order Item-type_of_expense_for_tax_purposes_so",
                    "Supplier Quotation Item-other_tax_amount",
                    "Purchase Receipt-facelec_pr_gt_tax_goods",
                    "Sales Order-shs_so_tax_or_good",
                    "Purchase Invoice Item-facelec_p_tax_rate_per_uom_account",
                    "Sales Invoice Item-facelec_gt_tax_net_services_amt",
                    "Delivery Note Item-shs_dn_gt_tax_net_services_amt",
                    "Sales Order Item-shs_so_gt_tax_net_fuel_amt",
                    "Purchase Receipt-guatemala_good_or_service_pr",
                    "Sales Order-shs_so_gt_tax_goods",
                    "Purchase Invoice Item-col_break_p1",
                    "Sales Invoice Item-facelec_gt_tax_net_fuel_amt",
                    "Delivery Note Item-tax_type_column_break",
                    "Sales Order Item-shs_so_gt_tax_net_goods_amt",
                    "Purchase Receipt-facelec_pr_gt_tax_services",
                    "Sales Order-shs_so_good_or_service",
                    "Purchase Invoice Item-facelec_p_amount_minus_excise_tax",
                    "Purchase Receipt Item-excise_tax_calculation_pr",
                    "Sales Invoice Item-tax_type_column_break",
                    "Delivery Note Item-shs_dn_is_fuel",
                    "Sales Order Item-shs_so_gt_tax_net_services_amt",
                    "Purchase Order-guatemala_tax",
                    "Purchase Receipt-facelec_pr_total_iva",
                    "Sales Order-shs_so_gt_tax_services",
                    "Quotation Item-excise_tax_calculation_section",
                    "Purchase Invoice Item-facelec_p_sales_tax_for_this_row",
                    "Purchase Receipt Item-facelec_pr_tax_rate_per_uom",
                    "Sales Invoice Item-facelec_is_service",
                    "Delivery Note Item-shs_dn_is_good",
                    "Sales Order Item-tax_type_column_break_so",
                    "Purchase Order-facelec_po_gt_tax_fuel",
                    "Sales Order-shs_so_total_iva",
                    "Purchase Invoice Item-ptype_of_expense_for_tax_purposes",
                    "Purchase Receipt Item-facelec_pr_other_tax_amount",
                    "Sales Invoice Item-facelec_is_good",
                    "Delivery Note Item-shs_dn_is_service",
                    "Sales Order Item-shs_so_is_fuel",
                    "Quotation Item-facelec_qt_tax_rate_per_uom",
                    "Purchase Order-guatemala_po_tax_or_good",
                    "Delivery Note-guatemala_tax_shs",
                    "Purchase Invoice Item-facelec_p_gt_tax_net_fuel_amt",
                    "Purchase Receipt Item-facelec_pr_tax_rate_per_uom_account",
                    "Sales Invoice Item-factelecis_fuel",
                    "Sales Order Item-shs_so_is_good",
                    "Quotation Item-facelec_qt_other_tax_amount",
                    "Purchase Order-facelec_po_gt_tax_goods",
                    "Delivery Note-shs_dn_gt_tax_fuel",
                    "Purchase Invoice Item-facelec_p_gt_tax_net_goods_amt",
                    "Purchase Receipt Item-col_pr",
                    "Sales Order Item-shs_so_is_service",
                    "Quotation Item-facelec_qt_tax_rate_per_uom_account",
                    "Purchase Order-guatemala_po_good_or_service",
                    "Delivery Note-guatemala_dn_tax_or_good",
                    "Purchase Invoice Item-facelec_p_gt_tax_net_services_amt",
                    "Purchase Receipt Item-facelec_pr_amount_minus_excise_tax",
                    "Quotation Item-col_break_qt",
                    "Purchase Order-facelec_po_gt_tax_services",
                    "Delivery Note-shs_dn_gt_tax_goods",
                    "Purchase Invoice Item-tax_type_column_break",
                    "Purchase Receipt Item-facelec_pr_sales_tax_for_this_row",
                    "Quotation Item-facelec_qt_amount_minus_excise_tax",
                    "Purchase Order-facelec_po_total_iva",
                    "Delivery Note-guatemala_dn_good_or_service",
                    "Sales Invoice-shs_total_iva_fac",
                    "Purchase Invoice Item-facelec_p_is_fuel",
                    "Purchase Receipt Item-prtype_of_expense_for_tax_purposes",
                    "Quotation Item-facelec_qt_sales_tax_for_this_row",
                    "Delivery Note-shs_dn_gt_tax_services",
                    "Purchase Invoice Item-facelec_p_is_good",
                    "Purchase Receipt Item-facelec_pr_gt_tax_net_fuel_amt",
                    "Quotation Item-type_of_expense_for_tax_purposes_qt",
                    "Delivery Note-shs_dn_total_iva",
                    "Purchase Invoice Item-facelec_p_is_service",
                    "Purchase Receipt Item-facelec_pr_gt_tax_net_goods_amt",
                    "Quotation Item-facelec_qt_gt_tax_net_fuel_amt",
                    "Purchase Receipt Item-facelec_pr_gt_tax_net_services_amt",
                    "Quotation Item-facelec_qt_gt_tax_net_goods_amt",
                    "Purchase Invoice-guatemala_tax",
                    "Purchase Receipt Item-tax_type_column_break_pr",
                    "Quotation Item-facelec_qt_gt_tax_net_services_amt",
                    "Purchase Invoice-facelec_p_gt_tax_fuel",
                    "Purchase Receipt Item-facelec_pr_is_fuel",
                    "Quotation Item-tax_type_column_break",
                    "Purchase Invoice-guatemala_tax_or_good",
                    "Purchase Receipt Item-facelec_pr_is_good",
                    "Quotation Item-facelec_qt_is_fuel",
                    "Purchase Invoice-facelec_p_gt_tax_goods",
                    "Purchase Receipt Item-facelec_pr_is_service",
                    "Quotation Item-facelec_qt_is_good",
                    "Purchase Invoice-guatemala_good_or_service",
                    "Quotation Item-facelec_qt_is_service",
                    "Purchase Invoice-facelec_p_gt_tax_services",
                    "Purchase Invoice-facelec_p_total_iva",
                    "Purchase Invoice-otros_impuestos_incluidos_en_precio",
                    "Purchase Invoice-shs_pi_otros_impuestos",
                    "Purchase Order Item-excise_tax_calculation_section",
                    "Purchase Invoice-shs_pi_total_otros_imp_incl",
                    "Purchase Order Item-facelec_po_tax_rate_per_uom",
                    "Purchase Invoice-otros_impuestos",
                    "Purchase Order Item-facelec_po_other_tax_amount",
                    "Purchase Invoice-other_tax_facelec",
                    "Purchase Order Item-facelec_po_tax_rate_per_uom_account",
                    "Purchase Order Item-col_brk_po",
                    "Sales Invoice-otros_impuestos_incluidos_en_precio",
                    "Purchase Order Item-facelec_po_amount_minus_excise_tax",
                    "Sales Invoice-shs_otros_impuestos",
                    "Purchase Order Item-facelec_po_sales_tax_for_this_row",
                    "Sales Invoice-shs_total_otros_imp_incl",
                    "Purchase Order Item-potype_of_expense_for_tax_purposes",
                    "Sales Invoice-tax_facelec",
                    "Purchase Order Item-facelec_po_gt_tax_net_fuel_amt",
                    "Sales Invoice-other_tax_facelec",
                    "Purchase Order Item-facelec_po_gt_tax_net_goods_amt",
                    "Purchase Order Item-facelec_po_gt_tax_net_services_amt",
                    "Purchase Order Item-tax_type_column_break",
                    "Purchase Order Item-facelec_po_is_fuel",
                    "Company-tax_witholding_ranges_section",
                    "Purchase Order Item-facelec_po_is_good",
                    "Company-tax_witholding_ranges",
                    "Purchase Order Item-facelec_po_is_service",
                    "Company-tax_category",
                    "Item-excise_taxes",
                    "Item-facelec_tax_rate_per_uom",
                    "Item-facelec_tax_rate_per_uom_purchase_account",
                    "Item-facelec_tax_rate_per_uom_selling_account",
                    "Item-facelec_uom_tax_included_in_price",
                    "Item-tax_per_category",
                    "Item-facelec_is_fuel",
                    "Item-facelec_is_good",
                    "Item-facelec_is_service",
                    "Purchase Invoice-purchase_ledger_page_number",
                    "Sales Invoice-sales_ledger_page_number",
                    "Customer-facelec_tax_category",
                    "Customer-facelec_section_taxes",
                    "Supplier-facelec_tax_category",
                    "Supplier-facelec_section_taxes",
                    "Sales Taxes and Charges Template-facelec_is_exempt",
                    "Item-facelec_is_exempt"
                    "Purchase Taxes and Charges Template-facelec_is_exempt",
                    "Sales Invoice-facelec_export_record",
                    "Sales Invoice-facelec_export_doc"
                ]
            ]
        ]
    }

    translation = {
        "dt": "Translation", "filters": [
            [
                "source_name", "in", [
                    "Public Writ",
                    "VAT Exemption Record",
                    "Consumable Acquisition Record",
                    "Unique Customs Declaration",
                    "SAT Form",
                    "Tax Category Group",
                    "Retention Confirmation Number",
                    "Sales Ledger Page Number",
                    "Purchase Ledger Page Number",
                    "Invoice Total",
                    "Invoice Date",
                    "Tax ID",
                    "Invoice Number",
                    "Date of Retention",
                    "Income Tax Retentions",
                    "VAT Retentions",
                    "VAT and Income Tax Retention Report",
                    "Es Factura Especial",
                    "Is Special Invoice"
                ]
            ]
        ]
    }


    # NEW FUNCTIONALITY FOR EXPORTING
    fixtures_fillup.append(custom_field)
    fixtures_fillup.append(translation)
    fixtures_fillup.append('Tax Category')
    fixtures_fillup.append('Identification Document Type')

    return fixtures_fillup

# fixtures = fill_fixtures()
