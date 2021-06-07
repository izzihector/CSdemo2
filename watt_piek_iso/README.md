RENAME FIELDS

PRODUCT TEMPLATE
ec_watt_piek          => xaa_aa_watt_piek
ec_iso                => xaa_aa_iso


SALE ORDER
ec_order_watt_piek    => xaa_aa_order_watt_piek
ec_order_iso          => xaa_aa_order_iso


SALE ORDER LINE
ec_watt_piek          => xaa_aa_watt_piek
ec_iso                => xaa_aa_iso
total_ec_watt_piek    => xaa_aa_total_watt_piek
total_ec_iso          => xaa_aa_total_iso


SALE REPORT
ec_order_watt_piek    => xaa_aa_order_watt_piek
ec_order_iso          => xaa_aa_order_iso


Functionality of this Module.

-> This Module allows you to set Watt Piek and ISO Value on Product template and later
   Used in Sale order and sale Report.
-> Calculate Watt Piek and ISO Values on SO Based on Sale order Line's Product's
   Watt Piek and ISO Values and it's quantity
-> Also Shows Watt Piek and ISO On Sales Report