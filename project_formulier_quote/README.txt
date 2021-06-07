ob_website_calender_booking
===========================
add button in mail template for open calender on website

quote_calculation
=================
quote_calculation module not used in this module, but it's usefull for formulier_type_2 and formulier_type_3 module

Field Rename
QUESTION FORMULIER
need_discount                       xaa_aa_need_discount
discount_product                    xaa_aa_discount_product
need_schouw                         xaa_aa_need_schouw
discount_qty                        xaa_aa_discount_qty
quote_template_id                   xaa_aa_quote_template_id
cost_price_total                    xaa_aa_cost_price_total

HOUSE INFO
house_type                          xaa_aa_house_type
house_image                         xaa_aa_house_image
is_iso                              xaa_aa_is_iso
is_pv                               xaa_aa_is_pv

ROOF INFO
roof_type                           xaa_aa_roof_type
roof_image                          xaa_aa_roof_image

PRODUCT USER
name                                xaa_aa_name

PRODUCT BRAND
name                                xaa_aa_name

SOLAR TYPE
name                                xaa_aa_name

PRODUCT TEMPLATE
priority                           xaa_aa_priority
product_type                       xaa_aa_product_type
min_product_range                  xaa_aa_min_product_range
max_product_range                  xaa_aa_max_product_range
wq_min_range                       xaa_aa_wq_min_range
wq_max_range                       xaa_aa_wq_max_range
solar_type                         xaa_aa_solar_type
product_brand                      xaa_aa_product_brand
is_solar_panel_product             xaa_aa_is_solar_panel_product
show_product_ec_user               xaa_aa_show_product_user
product_portal_user                xaa_aa_product_portal_user
wq_header_1                        xaa_aa_wq_header_1
wq_header_2                        xaa_aa_wq_header_2
wq_line1                           xaa_aa_wq_line1
wq_line2                           xaa_aa_wq_line2
wq_line3                           xaa_aa_wq_line3
wq_line4                           xaa_aa_wq_line4
wq_image                           xaa_aa_wq_image

RES USER
show_score                         xaa_aa_show_score

SALE ORDER TEMPLATE
task_product_id                    xaa_aa_task_product_id

SALE ORDER
cost_price_total                   xaa_aa_cost_price_total


CONTROLLER
/formulier/quote/<int:question_frm_id>/<string:pf_access>    => /formulier/quote/<int:xaa_aa_formulier_id>/<string:xaa_aa_pf_access>

VIEW ID CHANGE
question_formulier_view_inh        => view_project_formulier_form_inh
customer_quote_question_formulier  => customer_quotation_question_template

Functionality
..............
1. Add new url and website page for create quote for customer.
2. create new mail template for open online PF and make lost PF(lead). so customer can lost lead directly from received mail.
3. This module is helpfull for formulier type 2 and formulier type 3 module, here add new URL for website quote, so customer can create quote from that page.
4. add models, house info and roof info, this will usefull for formulier_type_2 and formulier_type_3 module.
5. this module provide all configuration of PF website quote. like add new fields on product.
6. hide header/footer on PF website quote. and also add all common required things related to formulier_type_2 and formulier_type_3 module.
7. use 'Montserrat' font on PF website quote.
8. use progress bar on submit online pf quote.
