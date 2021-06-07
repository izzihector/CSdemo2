RENAME FIELDS
=====================================================


CRM LEAD
sale_order_id                  =>      xaa_aa_sale_order_id

SALE ORDER
xaa_aa_formulier_type          =>      xaa_aa_formulier_type


Functionality of this Module.
=====================================================
==> This module create opportunity On quotation form if opportunity is not set on quotation.
==> Some of the features are :
==> When you Send quotation at that time if opportunity is not created, then it will
    create opportunity and move it to send quote stage.
==> When you confirm Quotation at that time it also set opportunity to won.
==> And if quotation cancel then it will set opportunity to lost.