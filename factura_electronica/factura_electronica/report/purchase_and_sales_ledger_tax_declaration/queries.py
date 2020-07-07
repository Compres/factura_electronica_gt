# Copyright (c) 2020, Si Hay Sistema and contributors
# For license information, please see license.txt

from __future__ import unicode_literals

import datetime

import frappe
from frappe import _
from frappe.utils import cstr, flt
import json


MONTHS_MAP = {
    "January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "Jun": 6,
    "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12
}


def get_purchases_invoice(filters):
    """
    Obtiene datos de la base de datos de Facturas de compras

    Args:
        filters (dict): Filtros front end

    Returns:
        list: Lista diccionarios
    """

    month = MONTHS_MAP.get(filters.month)

    purchase_invoices = frappe.db.sql(
        f"""SELECT DISTINCT name AS documento, 'C' AS compras_ventas, naming_series AS serie_doc, posting_date AS fecha_doc,
            facelec_nit_fproveedor AS nit_cliente_proveedor, supplier AS nombre_cliente_proveedor, company,
            supplier_address AS invoice_address, net_total, facelec_p_gt_tax_fuel AS total_fuel, facelec_p_gt_tax_goods AS total_goods,
            facelec_p_gt_tax_services AS total_services, facelec_p_total_iva AS iva, grand_total AS total_valor_doc,
            shipping_address AS company_address_invoice, docstatus, taxes_and_charges
            FROM `tabPurchase Invoice`
            WHERE YEAR(posting_date)='{filters.year}' AND MONTH(posting_date)='{month}' AND (docstatus=1 OR docstatus=2)
            AND company='{filters.company}';
        """, as_dict=True
    )

    # with open('items_purchase_invoice.json', 'w') as f:
    #     f.write(json.dumps(items, indent=2))

    return purchase_invoices


def get_sales_invoice(filters):
    """
    Obtiene datos de la base de datos de Facturas de venta

    Args:
        filters (dict): Filtros front end

    Returns:
        list: Lista diccionarios
    """

    month = MONTHS_MAP.get(filters.month)

    sales_invoices = frappe.db.sql(
        f"""SELECT DISTINCT name AS documento, 'V' AS compras_ventas, naming_series AS serie_doc, posting_date AS fecha_doc,
            nit_face_customer AS nit_cliente_proveedor, customer AS nombre_cliente_proveedor, company,
            customer_address AS invoice_address, net_total, shs_total_iva_fac AS iva, company_address AS company_address_invoice,
            docstatus, taxes_and_charges
            FROM `tabSales Invoice`
            WHERE YEAR(posting_date)='{filters.year}' AND MONTH(posting_date)='{month}' AND (docstatus=1 OR docstatus=2)
            AND company='{filters.company}';
        """, as_dict=True
    )

    with open('sales_invoices.json', 'w') as f:
        f.write(json.dumps(sales_invoices, default=str, indent=2))

    return sales_invoices


def get_items_purchase_invoice(invoice_name):

    items = frappe.db.sql(
        f"""SELECT DISTINCT parent, net_amount, amount, facelec_p_is_good AS is_good,
            facelec_p_is_service AS is_service, facelec_p_is_fuel AS is_fuel,
            facelec_p_sales_tax_for_this_row AS tax_for_item, facelec_p_gt_tax_net_fuel_amt AS net_fuel,
            facelec_p_gt_tax_net_goods_amt AS net_good, facelec_p_gt_tax_net_services_amt AS net_service
            FROM `tabPurchase Invoice Item` WHERE parent = '{invoice_name}'
        """, as_dict=True
    )

    # with open('items_purchase.json', 'w') as f:
    #     f.write(json.dumps(items, default=str, indent=2))

    return items


def get_items_sales_invoice(invoice_name):

    # facelec_gt_tax_net_goods_amt AS net_good, facelec_gt_tax_net_services_amt AS net_service

    items = frappe.db.sql(
        f"""SELECT DISTINCT parent, net_amount, amount, facelec_is_good AS is_good,
            facelec_is_service AS is_service, factelecis_fuel AS is_fuel,
            facelec_sales_tax_for_this_row AS tax_for_item, facelec_gt_tax_net_fuel_amt AS net_fuel,
            facelec_gt_tax_net_goods_amt AS net_good, facelec_gt_tax_net_services_amt AS net_service
            FROM `tabSales Invoice Item` WHERE parent = '{invoice_name}'
        """, as_dict=True
    )

    return items
