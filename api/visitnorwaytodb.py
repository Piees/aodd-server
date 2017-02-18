# -*- coding: utf-8 -*-
from models import Categories, Product, db
from visitnorwaydata import visitnorway, categories

for x in categories:
    cat = Categories()
    cat.id = x['id']
    cat.name = x['name']
    db.session.add(cat)
    db.session.commit()

for x in visitnorway:
    if x['geoLocation'] != None:
        cat = Categories.query.filter_by(
            name=x['categories'][0]['name']).first()
        prod = Product()
        prod.id = x['id']
        prod.name = x['name']
        prod.lat = x['geoLocation']['latitude']
        prod.long = x['geoLocation']['longitude']
        prod.image = None
        prod.alternativeText = None
        if x['image'] != None:
            prod.image = x['image']['url']
            prod.alternativeText = x['image']['alternativeText']
        prod.categories = cat
        db.session.add(prod)
        db.session.commit()
