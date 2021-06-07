
Field Rename
...............
CRM LEAD

PROJECT FORMULIER
house_info                          => xaa_aa_house_info
goal_owner                          => xaa_aa_goal_owner
analysis_settlement                 => xaa_aa_analysis_settlement
faced_construction                  => xaa_aa_faced_construction
area                                => xaa_aa_area
floor_construction                  => xaa_aa_floor_construction
floor_construction_verd             => xaa_aa_floor_construction_verd
floor_construction_verd_2           => xaa_aa_floor_construction_verd_2
leads                               => xaa_aa_leads
dakbouw                             => xaa_aa_dakbouw
roof_covering                       => xaa_aa_roof_covering
foundation_construction_ids         => xaa_aa_foundation_construction_ids
inspection_foundation_depth         => xaa_aa_inspection_foundation_depth
location_pipping_ground             => xaa_aa_location_pipping_ground
possible_settings                   => xaa_aa_possible_settings
action_resident                     => xaa_aa_action_resident
action_total_wall                   => xaa_aa_action_total_wall
level_measurement_result            => xaa_aa_level_measurement_result
notes_calculation                   => xaa_aa_notes_calculation
aantal_schroefpalen                 => xaa_aa_aantal_schroefpalen
sondering_diepte                    => xaa_aa_sondering_diepte
gkosten_funderingsherstel           => xaa_aa_gkosten_funderingsherstel
gkosten_scheurherstel               => xaa_aa_gkosten_scheurherstel
schroefpaaldiameter                 => xaa_aa_schroefpaaldiameter
parkeren                            => xaa_aa_parkeren
toegang                             => xaa_aa_toegang
tuin                                => xaa_aa_tuin
bomen                               => xaa_aa_bomen
kraan                               => xaa_aa_kraan
grondwerk                           => xaa_aa_grondwerk
aanvullend                          => xaa_aa_aanvullend
image_1                             => xaa_aa_image_1
image_2                             => xaa_aa_image_2
image_3                             => xaa_aa_image_3
image_4                             => xaa_aa_image_4
image_5                             => xaa_aa_image_5
image_6                             => xaa_aa_image_6
image_7                             => xaa_aa_image_7
image_8                             => xaa_aa_image_8
plattegrond_img                     => xaa_aa_plattegrond_img
fundering_img                       => xaa_aa_fundering_img
blueprint_img                       => xaa_aa_blueprint_img
lot_img                             => xaa_aa_lot_img
extra_drawing_1_img                 => xaa_aa_extra_drawing_1_img
extra_drawing_2_img                 => xaa_aa_extra_drawing_2_img
note                                => xaa_aa_note


VIEW ID CHANGE
question_formulier_image             => project_formulier_image
first_question_form_template         => opportunity_formulier_template
second_question_form_template        => quote_formulier_template
third_question_form_template         => task_formulier_template
view_question_formulier_form         => view_project_formulier_form


Functionality of module:
........................
1. Add Formulier one option in question type field in crm.
2. if user select this formulier one option in lead and convert it into opportunity, then they will see all images and fields related to this formulier type on PF form view and online version.
3. PF show fields based on question type, there is many question type and many different fields.
4. Create many custom snippets for online quote and that snippets values filled dynamically if quote is linked with PF record, like image snippet get image from PF record and other fields value.
5. you can add custom snippet from quotation template or directly on online quote, both are working fine and show you latest values.