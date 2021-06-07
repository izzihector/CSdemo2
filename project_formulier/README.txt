quote_print module:
...................
1 field is use from quote print module to this module
Field name: website_desc_footer
Method name: def fill_drawing_images()
Note: please check above method in all other related module of 'quotation_images_feedback'


1) change report tag

MODULE RENAME
quotation_images_feedback  => project_formulier
Field Rename
...............
CRM LEAD

question_frm_id                => xaa_aa_formulier_id
customer_type                  => xaa_aa_formulier_type
soort                          => xaa_aa_soort

RES USERS

customer_type                   xaa_aa_formulier_type
template_id                     xaa_aa_template_id
lead_category                   xaa_aa_lead_category
lead_lead_source                xaa_aa_lead_lead_source
redirect_pf_url                 xaa_aa_redirect_pf_url
show_cost_price                 xaa_aa_show_cost_price (remove from user)

New Model (formulier.customer.type)
name                            xaa_aa_name
technical_name                  xaa_aa_technical_name

SALE ORDER LINE
question_frm_id                => xaa_aa_formulier_id

SALE ORDER
question_frm_id                => xaa_aa_formulier_id
soort                          => xaa_aa_soort

SALE ORDER TEMPLATE
template_video_ids             => xaa_aa_template_video_ids

ORDER VIDEO
order_template_id              => xaa_aa_order_template_id

PROJECT TASK
question_frm_id                => xaa_aa_formulier_id

QUESTION FORMULIER
name                           => xaa_aa_name
active                         => active
lead_id                        => xaa_aa_lead_id
image                          => xaa_aa_image
partner_id                     => xaa_aa_partner_id
question_type                  => xaa_aa_formulier_type
state                          => xaa_aa_state
street                         => xaa_aa_street
street2                        => xaa_aa_street2
zip                            => xaa_aa_zip
city                           => xaa_aa_city
state_id                       => xaa_aa_state_id
country_id                     => xaa_aa_country_id
phone                          => xaa_aa_phone
mobile                         => xaa_aa_mobile
trademark_id                   => xaa_aa_trademark_id
time                           => xaa_aa_time
user_id                        => xaa_aa_user_id
pf_access                      => xaa_aa_pf_access
image_ids                      => xaa_aa_image_ids
sale_number                    => xaa_aa_sale_number
order_ids                      => xaa_aa_order_ids
lead_number                    => xaa_aa_lead_number
lead_ids                       => xaa_aa_lead_ids
task_number                    => xaa_aa_task_number
task_ids                       => xaa_aa_task_ids
date_opportunity               => xaa_aa_date_opportunity
date_report                    => xaa_aa_date_report
video_ids                      => xaa_aa_video_ids
document_ids                   => xaa_aa_document_ids

ORDER IMAGE
name                           => xaa_aa_name
image                          => xaa_aa_image
file_type                      => xaa_aa_file_type
is_task                        => xaa_aa_is_task
question_frm_id                => xaa_aa_formulier_id

ORDER IMAGE
name                           => xaa_aa_name
video                          => xaa_aa_video
file_type                      => xaa_aa_file_type
is_task                        => xaa_aa_is_task
question_frm_id                   => xaa_aa_formulier_id

ORDER DOCUMENT
name                           => xaa_aa_name
file                           => xaa_aa_file
file_type                      => xaa_aa_file_type
question_frm_id                => xaa_aa_formulier_id

CONTROLLER
/question/form/image/upload      => /formulier/form/image/upload
/question/form/video/upload      => /formulier/form/video/upload
/question/form/document/upload   => /formulier/form/document/upload
/question/formulier/submit/<int:question_frm_id>/<string:model_name> =>
    /project/formulier/submit/<int:xaa_aa_formulier_id>/<string:model_name>

VIEWS
id => first_question_form_template   => opportunity_formulier_template
id => second_question_form_template  => quote_formulier_template
id => third_question_form_template   => task_formulier_template
id => question_formulier_image       => project_formulier_image
id => question_formulier_extra_image => project_formulier_extra_image
id => question_formulier_video       => project_formulier_video
id => question_formulier_document    => project_formulier_document
id => question_formulier_task_extra_image => project_formulier_task_extra_image
id => question_formulier_task_video => project_formulier_task_video
id => question_formulier_task_document => project_formulier_task_document
id => third_question_formulier_image => task_project_formulier_image
id => question_formulier_profile => project_formulier_profile
id => question_formulier_template => main_formulier_template
id => action_question_formulier_form => action_project_formulier_form
id => view_question_formulier_form   => view_project_formulier_form

MENU
question_formulier_menu_root => project_formulier_menu_root
question_formulier_menu      => project_formulier_menu


Functionality
main goal is get information from customer related to lead, quotation.
1. Formulier record is created when lead is converted into opportunity.
2. Add PF tab in opportunity, Task, Sale Order and also add create project formulier button in opportunity.
3. Add buttons on opportunity for open online PF and form view of PF.
4. Many fields filled from opportunity into PF record. like partner, address, mobile etc.
5. Add project formulier tab on user form (many configuration), this values are useful for online pf operation.
6. For the open online PF, user require PF ID and Access token
7. Back to edit and Back to opportunity link add on online PF for redirect on that.
8. Upload many images on online pf(From Extra Images Tab), Also user can delete it.
9. Upload many videos on online pf(From Videos Tab), Also user can delete it.
10. Upload many Documents on online pf(From Documents Tab), Also user can delete it.
11) Add many tabs on online PF and some are show based on some condition, like first phase is for opportunity data, and that phase only show when PF have 'opportunity' stage, there is total 3 phase, and 6 stages on PF, first stage is for get some details from customer, so ask some basic question on online pf, third phase is show when PF have created quotation and task.
12) Online pf reload on click 'save' button.
13) Streetview image add in 'overview' image field
14) User can fill onlin form all fields, different type of fields.
15) Add smart button on PF form view for show linked opportunity, sale order and task.
16) Login user related PF records show in my account in website, user can open own PF record from my account.
17) Dynamic value concept apply for online quote, user can get any field value on online quotation, (Quotation, opportunity, PF) => syntax => $(formulier:object.xxa_aa_name)
18) Image fields updated from online PF.
19) Add new tabs in edit media dialogue box on online quote page and show all images, documents and videos from linked PF records,  user also can select image from edit media dialogue box and put it in online quote.