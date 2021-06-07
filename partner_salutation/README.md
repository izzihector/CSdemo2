RENAME FIELDS

RES PARTNER
firstname                   =>   xaa_aa_firstname
lastname                    =>   xaa_aa_lastname
informal_salutation         =>    xaa_aa_informal_salutation
formal_salutation           =>   xaa_aa_formal_salutation
formal_partner_salutation   =>  xaa_aa_formal_partner_salutation
informal_partner_salutation =>   xaa_aa_informal_partner_salutation


CRM LEAD
firstname                 => xaa_aa_firstname
lastname                  => xaa_aa_lastname
informal_salutation       => xaa_aa_informal_salutation
formal_salutation         => xaa_aa_formal_salutation
formal_salutation_result  => xaa_aa_formal_salutation_result
informal_salutation_result => xaa_aa_informal_salutation_result


SALE ORDER
sale_order_partner_result  => xaa_aa_sale_order_partner_result
salutation_type            => xaa_aa_salutation_type


functionality that we can add : 

When customer create from a lead at that time partner salutation and first name and last name must be add at new customer


Functionality OF this module:

=>  Based On First name , last name and partner salutation type you can generate Formal and Informal 
    Partner's Salutaion Result on Contacts and on CRM Lead.
=>  When Lead Convert to opportunity at that time Whatever Partners Details have like firstname,
    lastname, formal and informal salutation it will update on Contacts too.
=>  Also, Add partner salutaion On SO based on Partner.