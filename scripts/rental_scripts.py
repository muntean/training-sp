from xmlrpc import client
from datetime import datetime

url = 'https://bisstech-training-sp-dev-library-4944020.dev.odoo.com'
db = 'bisstech-training-sp-dev-library-4944020'
username = 'admin'
password = 'admin'

common = client.ServerProxy("{}/xmlrpc/2/common".format(url))
print(common.version())

uid = common.authenticate(db, username, password, {})
print(uid)

models = client.ServerProxy("{}/xmlrpc/2/object".format(url))

model_access = models.execute_kw(db, uid, password,
                                'library.rental', 'check_access_rights',
                                ['write'], {'raise_exception': False})
print(model_access)

contacts = models.execute_kw(db, uid, password,
                            'res.partner', 'search_read',
                            [[['is_company', '=', False]]], {'fields': ['name']})
print(contacts)

rental_fields = models.execute_kw(db, uid, password,
                                 'library.rental', 'fields_get',
                                 [], {'attributes': ['string', 'type', 'required']})
print(rental_fields)

rental_dates = models.execute_kw(db, uid, password,
                                  'library.rental', 'search_read',
                                  [], {'fields': ['write_date']})
print(rental_dates)

is_updated = False
for rental in rental_dates:
    date = datetime.strptime(rental['write_date'], "%Y-%m-%d %H:%M:%S")
    today = datetime.strptime(str(datetime.today()), "%Y-%m-%d %H:%M:%S.%f")
    if abs(date.month - today.month) > 2:
        update_rental = models.execute_kw(db, uid, password,
                                         'library.rental', 'write',
                                         [
                                             {
                                                 'customer_id': contacts[0]['id'],
                                             }
                                         ]
                                         )
        print(update_rental)
        is_updated = True
        
print(is_updated)