Solvari Api
---------------

Solvari Docs <a href="https://pro.solvari.nl/api/customer-docs/index.html">URL</a> 

Solvari send http request, params filled in form data
----------------------
Ex:
gender: Male
first_name: madan
last_name": thakur
street: ABC
house_nr: 123456
zip_code: 67890
city: gandhinagar
location[lat]: 23
phone: 1234567890
email: madan@madan.com.com
spoken_by_solvari:True
message_by_solvari:solvari message
competitors:xyz
description:solari lead
additional_data[question]:whats your name
additional_data[answer]:Madan
products[id]:1
products[title]:solvari product
secret:
---------------------------------------------------

json data sample send by  solvari api
------------------------------------------
{"city": "Nieuwegein", "first_name": "Test", "last_name": "Jansen", "description": "Optional description added by lead", "message_by_solvari": "Special message by Solvari", "house_nr": "9", "products[0][title]": "Zonnepanelen installeren", "gender": "M", "created_at": "2020-05-08 12:48:15", "location[lat]": "52.0285223", "email": "info@solvari.nl", "products[0][id]": "1040", "phone": "+31 (0)85 - 600 1000", "street": "Zadelstede", "spoken_by_solvari": "0", "competitors": "2", "country": "NL", "location[lng]": "5.0741231", "id": "15000000", "zip_code": "3431 JZ"}
