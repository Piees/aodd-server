# -*- coding: utf-8 -*-
import json

visitcategories = json.loads(
    '''[{"id":"40","name":"Tourist","code":"tourist","subcategories":[{"id":null,"name":null,"code":"tourist--whats-on","subcategories":[{"id":"31","name":"Annual","code":"tourist--whats-on--annual","subcategories":[]},{"id":"13","name":"Art & Design Exhibitions","code":"tourist--whats-on--art+%26+design+exhibitions","subcategories":[]},{"id":"32","name":"Children & Family","code":"tourist--whats-on--children+%26+family","subcategories":[]},{"id":"3","name":"Classical Concerts & Festivals","code":"tourist--whats-on--classical+concerts+%26+festivals","subcategories":[]},{"id":"1","name":"Concerts & Festivals","code":"tourist--whats-on--concerts+%26+festivals","subcategories":[]},{"id":"11","name":"Congress & Conventions","code":"tourist--whats-on--congress+%26+conventions","subcategories":[]},{"id":"30","name":"Cultural","code":"tourist--whats-on--cultural","subcategories":[]},{"id":"25","name":"Dance","code":"tourist--whats-on--dance","subcategories":[]},{"id":"6","name":"Festivals","code":"tourist--whats-on--festivals","subcategories":[]},{"id":"17","name":"Food & Drink","code":"tourist--whats-on--food+%26+drink","subcategories":[]},{"id":"18","name":"Guided Tours","code":"tourist--whats-on--guided+tours","subcategories":[]},{"id":"7","name":"Jazz & Blues Concerts & Festivals","code":"tourist--whats-on--jazz+%26+blues+concerts+%26+festivals","subcategories":[]},{"id":"26","name":"Movies","code":"tourist--whats-on--movies","subcategories":[]},{"id":"9","name":"Pop & Rock Concerts & Festivals","code":"tourist--whats-on--pop+%26+rock+concerts+%26+festivals","subcategories":[]},{"id":"28","name":"Shows","code":"tourist--whats-on--shows","subcategories":[]},{"id":"21","name":"Sports","code":"tourist--whats-on--sports","subcategories":[]},{"id":"29","name":"Theatre","code":"tourist--whats-on--theatre","subcategories":[]},{"id":"24","name":"Winter Sports","code":"tourist--whats-on--winter+sports","subcategories":[]}]},{"id":null,"name":null,"code":"tourist--what-to-do","subcategories":[{"id":"19","name":"Getting Here & Around","code":"tourist--what-to-do--getting+here+%26+around","subcategories":[{"id":"110","name":"Air Travel","code":"tourist--what-to-do--getting+here+%26+around--air+travel","subcategories":[]},{"id":"111","name":"Buses","code":"tourist--what-to-do--getting+here+%26+around--buses","subcategories":[]},{"id":"112","name":"Car Rental","code":"tourist--what-to-do--getting+here+%26+around--car+rental","subcategories":[]},{"id":"113","name":"Cruise","code":"tourist--what-to-do--getting+here+%26+around--cruise","subcategories":[]},{"id":"114","name":"Ferries & Boats","code":"tourist--what-to-do--getting+here+%26+around--ferries+%26+boats","subcategories":[]},{"id":"115","name":"Taxi","code":"tourist--what-to-do--getting+here+%26+around--taxi","subcategories":[]},{"id":"116","name":"Tour Operators","code":"tourist--what-to-do--getting+here+%26+around--tour+operators","subcategories":[]},{"id":"117","name":"Train","code":"tourist--what-to-do--getting+here+%26+around--train","subcategories":[]},{"id":"235","name":"Driving Suggestions","code":"tourist--what-to-do--getting+here+%26+around--driving+suggestions","subcategories":[]}]},{"id":"115","name":"The Great Outdoors","code":"tourist--what-to-do--the+great+outdoors","subcategories":[{"id":"140","name":"Action & Adventure","code":"tourist--what-to-do--the+great+outdoors--action+%26+adventure","subcategories":[]},{"id":"141","name":"Climbing","code":"tourist--what-to-do--the+great+outdoors--climbing","subcategories":[]},{"id":"142","name":"Diving","code":"tourist--what-to-do--the+great+outdoors--diving","subcategories":[]},{"id":"143","name":"Glacier walking","code":"tourist--what-to-do--the+great+outdoors--glacier+walking","subcategories":[]},{"id":"144","name":"Grotting","code":"tourist--what-to-do--the+great+outdoors--grotting","subcategories":[]},{"id":"145","name":"Hanggliding & Paragliding","code":"tourist--what-to-do--the+great+outdoors--hanggliding+%26+paragliding","subcategories":[]},{"id":"146","name":"Kiting","code":"tourist--what-to-do--the+great+outdoors--kiting","subcategories":[]},{"id":"147","name":"Motor sports","code":"tourist--what-to-do--the+great+outdoors--motor+sports","subcategories":[]},{"id":"148","name":"Parachuting","code":"tourist--what-to-do--the+great+outdoors--parachuting","subcategories":[]},{"id":"149","name":"Rafting","code":"tourist--what-to-do--the+great+outdoors--rafting","subcategories":[]},{"id":"150","name":"Snowscooter","code":"tourist--what-to-do--the+great+outdoors--snowscooter","subcategories":[]},{"id":"151","name":"Biking","code":"tourist--what-to-do--the+great+outdoors--biking","subcategories":[]},{"id":"152","name":"Canoeing & Kayaking","code":"tourist--what-to-do--the+great+outdoors--canoeing+%26+kayaking","subcategories":[]},{"id":"153","name":"Fishing","code":"tourist--what-to-do--the+great+outdoors--fishing","subcategories":[]},{"id":"154","name":"Hiking","code":"tourist--what-to-do--the+great+outdoors--hiking","subcategories":[]},{"id":"155","name":"Hunting","code":"tourist--what-to-do--the+great+outdoors--hunting","subcategories":[]},{"id":"156","name":"Riding & Sledging","code":"tourist--what-to-do--the+great+outdoors--riding+%26+sledging","subcategories":[]},{"id":"157","name":"Sailing & Boat Activities","code":"tourist--what-to-do--the+great+outdoors--sailing+%26+boat+activities","subcategories":[]},{"id":"158","name":"Skiing","code":"tourist--what-to-do--the+great+outdoors--skiing","subcategories":[]},{"id":"159","name":"Winter Without Skis","code":"tourist--what-to-do--the+great+outdoors--winter+without+skis","subcategories":[]},{"id":"195","name":"Wildlife & Safaris","code":"tourist--what-to-do--the+great+outdoors--wildlife+%26+safaris","subcategories":[]},{"id":"221","name":"Golfing","code":"tourist--what-to-do--the+great+outdoors--golfing","subcategories":[]},{"id":"222","name":"Summer Activities","code":"tourist--what-to-do--the+great+outdoors--summer+activities","subcategories":[]},{"id":"230","name":"National Parks","code":"tourist--what-to-do--the+great+outdoors--national+parks","subcategories":[]},{"id":"231","name":"Tour Suggestions","code":"tourist--what-to-do--the+great+outdoors--tour+suggestions","subcategories":[]}]},{"id":"110","name":"Attraction & Culture","code":"tourist--what-to-do--attraction+%26+culture","subcategories":[{"id":"160","name":"Buildings & Monuments","code":"tourist--what-to-do--attraction+%26+culture--buildings+%26+monuments","subcategories":[]},{"id":"161","name":"Cultural Heritage","code":"tourist--what-to-do--attraction+%26+culture--cultural+heritage","subcategories":[]},{"id":"162","name":"Museums & Galleries","code":"tourist--what-to-do--attraction+%26+culture--museums+%26+galleries","subcategories":[]},{"id":"163","name":"Nature Attractions","code":"tourist--what-to-do--attraction+%26+culture--nature+attractions","subcategories":[]},{"id":"164","name":"Sami Culture","code":"tourist--what-to-do--attraction+%26+culture--sami+culture","subcategories":[]},{"id":"210","name":"Northern Lights","code":"tourist--what-to-do--attraction+%26+culture--northern+lights","subcategories":[]},{"id":"212","name":"Vikings","code":"tourist--what-to-do--attraction+%26+culture--vikings","subcategories":[]},{"id":"213","name":"Midnight Sun","code":"tourist--what-to-do--attraction+%26+culture--midnight+sun","subcategories":[]}]},{"id":"111","name":"Family Fun","code":"tourist--what-to-do--family+fun","subcategories":[{"id":"166","name":"Bathing","code":"tourist--what-to-do--family+fun--bathing","subcategories":[]},{"id":"167","name":"Family Activities","code":"tourist--what-to-do--family+fun--family+activities","subcategories":[]},{"id":"168","name":"Farm Activities","code":"tourist--what-to-do--family+fun--farm+activities","subcategories":[]},{"id":"169","name":"Games","code":"tourist--what-to-do--family+fun--games","subcategories":[]},{"id":"170","name":"Theme Parks","code":"tourist--what-to-do--family+fun--theme+parks","subcategories":[]},{"id":"209","name":"Beaches","code":"tourist--what-to-do--family+fun--beaches","subcategories":[]},{"id":"214","name":"Ball Games","code":"tourist--what-to-do--family+fun--ball+games","subcategories":[]}]},{"id":"114","name":"Taste Norway","code":"tourist--what-to-do--taste+norway","subcategories":[{"id":"171","name":"Cafés & Diner","code":"tourist--what-to-do--taste+norway--caf%c3%a9s+%26+diner","subcategories":[]},{"id":"172","name":"Food Traditions","code":"tourist--what-to-do--taste+norway--food+traditions","subcategories":[]},{"id":"174","name":"Nightclubs","code":"tourist--what-to-do--taste+norway--nightclubs","subcategories":[]},{"id":"175","name":"Pubs & Bars","code":"tourist--what-to-do--taste+norway--pubs+%26+bars","subcategories":[]},{"id":"176","name":"Restaurants","code":"tourist--what-to-do--taste+norway--restaurants","subcategories":[]},{"id":"220","name":"Seafood Restaurants","code":"tourist--what-to-do--taste+norway--seafood+restaurants","subcategories":[]},{"id":"229","name":"Norwegian Foodprints","code":"tourist--what-to-do--taste+norway--norwegian+foodprints","subcategories":[]}]},{"id":"113","name":"Shopping","code":"tourist--what-to-do--shopping","subcategories":[{"id":"182","name":"Gifts & Souvenirs","code":"tourist--what-to-do--shopping--gifts+%26+souvenirs","subcategories":[]},{"id":"183","name":"Grocery","code":"tourist--what-to-do--shopping--grocery","subcategories":[]},{"id":"184","name":"Home & Garden","code":"tourist--what-to-do--shopping--home+%26+garden","subcategories":[]},{"id":"185","name":"Services","code":"tourist--what-to-do--shopping--services","subcategories":[]},{"id":"186","name":"Shopping Center","code":"tourist--what-to-do--shopping--shopping+center","subcategories":[]},{"id":"187","name":"Shops","code":"tourist--what-to-do--shopping--shops","subcategories":[]},{"id":"188","name":"Sports & Outdoors","code":"tourist--what-to-do--shopping--sports+%26+outdoors","subcategories":[]},{"id":"216","name":"Clothing","code":"tourist--what-to-do--shopping--clothing","subcategories":[]}]},{"id":"117","name":"Recreation & Sports","code":"tourist--what-to-do--recreation+%26+sports","subcategories":[{"id":"217","name":"Ball Games","code":"tourist--what-to-do--recreation+%26+sports--ball+games","subcategories":[]},{"id":"218","name":"Fitness Centers","code":"tourist--what-to-do--recreation+%26+sports--fitness+centers","subcategories":[]},{"id":"219","name":"Other sports","code":"tourist--what-to-do--recreation+%26+sports--other+sports","subcategories":[]},{"id":"236","name":"Spa","code":"tourist--what-to-do--recreation+%26+sports--spa","subcategories":[]},{"id":"237","name":"Motor Sports","code":"tourist--what-to-do--recreation+%26+sports--motor+sports","subcategories":[]},{"id":"238","name":"Golfing","code":"tourist--what-to-do--recreation+%26+sports--golfing","subcategories":[]}]},{"id":"118","name":"Tours & Sightseeing","code":"tourist--what-to-do--tours+%26+sightseeing","subcategories":[{"id":"223","name":"Fjord & Coastal Cruise","code":"tourist--what-to-do--tours+%26+sightseeing--fjord+%26+coastal+cruise","subcategories":[]},{"id":"224","name":"Guided Tours","code":"tourist--what-to-do--tours+%26+sightseeing--guided+tours","subcategories":[]},{"id":"225","name":"Round Trips","code":"tourist--what-to-do--tours+%26+sightseeing--round+trips","subcategories":[]},{"id":"226","name":"Sightseeing","code":"tourist--what-to-do--tours+%26+sightseeing--sightseeing","subcategories":[]},{"id":"227","name":"Tour Suggestions","code":"tourist--what-to-do--tours+%26+sightseeing--tour+suggestions","subcategories":[]}]}]},{"id":null,"name":null,"code":"tourist--where-to-stay","subcategories":[{"id":"197","name":"Apartments","code":"tourist--where-to-stay--apartments","subcategories":[]},{"id":"198","name":"Camping","code":"tourist--where-to-stay--camping","subcategories":[]},{"id":"199","name":"Cottages & Holiday Houses","code":"tourist--where-to-stay--cottages+%26+holiday+houses","subcategories":[]},{"id":"200","name":"Farm Holidays","code":"tourist--where-to-stay--farm+holidays","subcategories":[]},{"id":"201","name":"Fishermen\u0027s Cabin","code":"tourist--where-to-stay--fishermen\u0027s+cabin","subcategories":[]},{"id":"202","name":"Guest Marinas","code":"tourist--where-to-stay--guest+marinas","subcategories":[]},{"id":"203","name":"Health & Spa Hotel","code":"tourist--where-to-stay--health+%26+spa+hotel","subcategories":[]},{"id":"204","name":"Hostels & Guesthouses","code":"tourist--where-to-stay--hostels+%26+guesthouses","subcategories":[]},{"id":"205","name":"Hotels","code":"tourist--where-to-stay--hotels","subcategories":[]},{"id":"206","name":"Lighthouse","code":"tourist--where-to-stay--lighthouse","subcategories":[]},{"id":"207","name":"Motels","code":"tourist--where-to-stay--motels","subcategories":[]},{"id":"208","name":"Private Rooms to Rent","code":"tourist--where-to-stay--private+rooms+to+rent","subcategories":[]},{"id":"211","name":"Ski Resort","code":"tourist--where-to-stay--ski+resort","subcategories":[]},{"id":"215","name":"Spa","code":"tourist--where-to-stay--spa","subcategories":[]}]}]}]'''
)[0]

visitnorway = json.loads('''[{
    "id": "7651",
    "name": "Ådneram Cabin",
    "geoLocation": {
        "latitude": 59.01785,
        "longitude": 6.93066,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=354&p=758&t=1",
        "alternativeText": "Ådneram Turisthytte",
        "copyright": "Ådneram Turisthytte"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "23",
        "name": "Hotels & More",
        "code": null
    }],
    "owner": "Lister Reiseliv",
    "ownerId": null,
    "address": "Undergangen v/Rogaland Teater",
    "contact": {
        "address": "Undergangen v/Rogaland Teater",
        "email": "informasjon@stavanger-turistforening.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 51840200",
        "streetAddress": null,
        "postalCode": "4001",
        "city": "Sirdal",
        "web": "http://www.stavanger-turistforening.no",
        "bookingUrl": "",
        "county": {
            "code": 11,
            "name": "ROGALAND"
        },
        "municipality": {
            "code": 1103,
            "name": "STAVANGER"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "173057",
    "name": "Access Oslo",
    "geoLocation": {
        "latitude": 60.20106,
        "longitude": 11.07486,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=10&p=2787512&t=1",
        "alternativeText": "Access Oslo",
        "copyright": "Access Oslo"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "19",
        "name": "Getting Here & Around",
        "code": null
    }],
    "owner": "Akershus Reiselivsråd",
    "ownerId": null,
    "address": "GA - terminalen Oslo Lufthavn, Gardermoen Vest",
    "contact": {
        "address": "GA - terminalen Oslo Lufthavn, Gardermoen Vest",
        "email": "ops@accessoslo.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 91222999",
        "streetAddress": null,
        "postalCode": "2060",
        "city": "Ullensaker",
        "web": "http://www.accessoslo.no",
        "bookingUrl": "",
        "county": {
            "code": 2,
            "name": "AKERSHUS"
        },
        "municipality": {
            "code": 235,
            "name": "ULLENSAKER"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "9451",
    "name": "Across Spitsbergen Ski Expedition-Hurtigruten Svalbard",
    "geoLocation": {
        "latitude": 78.2209,
        "longitude": 15.64603,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=384&p=399&t=1",
        "alternativeText": "Skitur",
        "copyright": "Skitur"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "115",
        "name": "The Great Outdoors",
        "code": null
    }],
    "owner": "Svalbard Reiseliv AS",
    "ownerId": null,
    "address": "Polarsenteret",
    "contact": {
        "address": "Polarsenteret",
        "email": "info@hurtigrutensvalbard.com",
        "fax": null,
        "mobile": null,
        "phone": " +47 79026100",
        "streetAddress": null,
        "postalCode": "9170",
        "city": "Spitsbergen",
        "web": "www.hurtigrutensvalbard.com",
        "bookingUrl": "",
        "county": {
            "code": 21,
            "name": "SVALBARD"
        },
        "municipality": {
            "code": 2111,
            "name": "SPITSBERGEN"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "175491",
    "name": "Active Leisure",
    "geoLocation": {
        "latitude": 59.08213,
        "longitude": 10.4213,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=4&p=6089&t=1",
        "alternativeText": "Aktiv fritid - ut på tur",
        "copyright": "Aktiv fritid - ut på tur"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "111",
        "name": "Family Fun",
        "code": null
    }],
    "owner": "Visit Sandefjord",
    "ownerId": null,
    "address": "Sjøbodsand",
    "contact": {
        "address": "Sjøbodsand",
        "email": "post@a-fritid.no",
        "fax": null,
        "mobile": null,
        "phone": "",
        "streetAddress": null,
        "postalCode": "3145",
        "city": "Tjøme",
        "web": "www.a-fritid.no",
        "bookingUrl": "",
        "county": {
            "code": 7,
            "name": "VESTFOLD"
        },
        "municipality": {
            "code": 723,
            "name": "TJØME"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "126851",
    "name":
    "4 Days – VIP Sailing From Tromsø to Hammerfest - Arctic Cruise in Norway",
    "geoLocation": {
        "latitude": 69.6509754127,
        "longitude": 18.9602413545,
        "elevation": 0
    },
    "image": {
        "url": "http://images.citybreak.com/image.aspx?ImageId=3177956",
        "alternativeText": "4 Days – VIP Sailing From Tromsø to Hammerfest",
        "copyright": "4 Days – VIP Sailing From Tromsø to Hammerfest"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "118",
        "name": "Tours & Sightseeing",
        "code": null
    }],
    "owner": "Visit Tromsø-Region",
    "ownerId": null,
    "address": "Brinkvegen 41",
    "contact": {
        "address": "Brinkvegen 41",
        "email": "kal@acinorway.com",
        "fax": null,
        "mobile": null,
        "phone": " +47 90549997",
        "streetAddress": null,
        "postalCode": "9012",
        "city": "Tromsø",
        "web": "http://www.acinorway.com",
        "bookingUrl": "",
        "county": {
            "code": 19,
            "name": "TROMS"
        },
        "municipality": {
            "code": 1902,
            "name": "TROMSØ"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "177431",
    "name": "Aim Challenge",
    "geoLocation": {
        "latitude": 60.862802208,
        "longitude": 8.5224938392,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=500&p=6771&t=1",
        "alternativeText": "Aim Challenge",
        "copyright": "Aim Challenge"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "117",
        "name": "Recreation & Sports",
        "code": null
    }],
    "owner": "Hemsedal Turistkontor",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "info@aimchallenge.com",
        "fax": null,
        "mobile": null,
        "phone": "",
        "streetAddress": null,
        "postalCode": "3560",
        "city": "Hemsedal",
        "web": "www.hemsedal.com",
        "bookingUrl": "",
        "county": {
            "code": 6,
            "name": "BUSKERUD"
        },
        "municipality": {
            "code": 618,
            "name": "HEMSEDAL"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "12354",
    "name": "Akers Have Apartments",
    "geoLocation": {
        "latitude": 59.918189195,
        "longitude": 10.761576447,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=23&p=13334&t=1",
        "alternativeText": "Akers Have 1",
        "copyright": "Akers Have 1"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "23",
        "name": "Hotels & More",
        "code": null
    }],
    "owner": "VisitOSLO as",
    "ownerId": null,
    "address": "Heimdalsgata 1 A",
    "contact": {
        "address": "Heimdalsgata 1 A",
        "email": "post@akershave.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 23891044",
        "streetAddress": null,
        "postalCode": "0560",
        "city": "Oslo",
        "web": "www.akershave.no",
        "bookingUrl": "",
        "county": {
            "code": 3,
            "name": "OSLO"
        },
        "municipality": {
            "code": 301,
            "name": "OSLO"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "182624",
    "name":
    "24-hour Aurora Expedition in the Beautiful Lyngen Alps – Green Gold of Norway",
    "geoLocation": {
        "latitude": 69.649219,
        "longitude": 18.962274,
        "elevation": 0
    },
    "image": {
        "url": "http://images.citybreak.com/image.aspx?ImageId=3218734",
        "alternativeText": "",
        "copyright": ""
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "110",
        "name": "Attraction & Culture",
        "code": null
    }],
    "owner": "",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "francisco@greengoldofnorway.com",
        "fax": null,
        "mobile": null,
        "phone": "",
        "streetAddress": null,
        "postalCode": null,
        "city": "9008",
        "web": "www.greengoldofnorway.com",
        "bookingUrl": "",
        "county": {
            "code": 0,
            "name": null
        },
        "municipality": {
            "code": 0,
            "name": null
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "11661",
    "name": "Aaraastunet",
    "geoLocation": {
        "latitude": 59.989,
        "longitude": 10.97714,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=10&p=2719413&t=1",
        "alternativeText": "Aaraastunet  - dekket bord",
        "copyright": "Aaraastunet  - dekket bord"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "20",
        "name": "Meeting Venues",
        "code": null
    }],
    "owner": "Akershus Reiselivsråd",
    "ownerId": null,
    "address": "Årosveien 307",
    "contact": {
        "address": "Årosveien 307",
        "email": "aaraastunet@gmail.com",
        "fax": null,
        "mobile": null,
        "phone": " +47 46922214",
        "streetAddress": null,
        "postalCode": "1480",
        "city": "Nittedal",
        "web": "http:// www.aaraasgard.no",
        "bookingUrl": "",
        "county": {
            "code": 2,
            "name": "AKERSHUS"
        },
        "municipality": {
            "code": 233,
            "name": "NITTEDAL"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "4717",
    "name": "Aarnes kafeteria",
    "geoLocation": {
        "latitude": 59.36696,
        "longitude": 9.18008,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=78&p=2725&t=1",
        "alternativeText": "Aarnes Kafeteria",
        "copyright": "Aarnes Kafeteria"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "114",
        "name": "Taste Norway",
        "code": null
    }],
    "owner": "Reisemål Bø AS",
    "ownerId": null,
    "address": "Strannavegen 302",
    "contact": {
        "address": "Strannavegen 302",
        "email": "post@aarneskafeteria.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 35955733",
        "streetAddress": null,
        "postalCode": "3810",
        "city": "Sauherad",
        "web": "http://www.aarnesgruppen.no",
        "bookingUrl": "",
        "county": {
            "code": 8,
            "name": "TELEMARK"
        },
        "municipality": {
            "code": 822,
            "name": "SAUHERAD"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": {
        "tripAdvisorId": 3388524,
        "tripAdvisorUrl":
        "https://www.tripadvisor.com/Restaurant_Review-g3206469-d3388524-Reviews-m34784-Aarnes_Kafeteria-Gvarv_Sauherad_Municipality_Telemark_Eastern_Norway.html",
        "name": "Aarnes Kafeteria",
        "avgRating": 4.5,
        "reviewCount": 17,
        "geoId": 3206469,
        "type": "restaurant",
        "vnExternIds": null
    },
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "91364",
    "name": "Abelvær Gård",
    "geoLocation": {
        "latitude": 64.73146,
        "longitude": 11.18355,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=393&p=991&t=1",
        "alternativeText":
        "Abelvær Gård (farm) in Nærøy along the scenic road Kystriksv",
        "copyright":
        "Abelvær Gård (farm) in Nærøy along the scenic road Kystriksv"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "23",
        "name": "Hotels & More",
        "code": null
    }],
    "owner": "Ergo-Tec (norwaysafari.no)",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "post@abelvaer.com",
        "fax": null,
        "mobile": null,
        "phone": " +47 92414496",
        "streetAddress": null,
        "postalCode": "7950",
        "city": "Nærøy",
        "web": "http://abelvaer.com",
        "bookingUrl": "",
        "county": {
            "code": 17,
            "name": "NORD-TRØNDELAG"
        },
        "municipality": {
            "code": 1751,
            "name": "NÆRØY"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "188617",
    "name": "4.The Pilgrim’s Route Mastemyr-Oslo",
    "geoLocation": {
        "latitude": 59.80656,
        "longitude": 10.79112,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=10&p=2756011&t=1",
        "alternativeText": "Pilegrimsleden Follo",
        "copyright": "Pilegrimsleden Follo"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "115",
        "name": "The Great Outdoors",
        "code": null
    }],
    "owner": "Akershus Reiselivsråd",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "info@akershus.com",
        "fax": null,
        "mobile": null,
        "phone": "",
        "streetAddress": null,
        "postalCode": "1410",
        "city": "Oppegård",
        "web": "www.akershus.com",
        "bookingUrl": "",
        "county": {
            "code": 2,
            "name": "AKERSHUS"
        },
        "municipality": {
            "code": 217,
            "name": "OPPEGÅRD"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "8511",
    "name":
    "7 days\u0027 photo and bird watching safari with Fjord Cruise Adventure",
    "geoLocation": {
        "latitude": 62.47223,
        "longitude": 6.14948,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=65&p=7967&t=1",
        "alternativeText": "Points North Charters",
        "copyright": "Points North Charters"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "110",
        "name": "Attraction & Culture",
        "code": null
    }],
    "owner": "Geirangerfjord - Ålesund & Sunnmøre",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "info@pointsnorthcharters.com",
        "fax": null,
        "mobile": null,
        "phone": " +47 90792834",
        "streetAddress": null,
        "postalCode": "6002",
        "city": "Ålesund",
        "web": "http://www.pointsnorthcharters.com",
        "bookingUrl": "",
        "county": {
            "code": 15,
            "name": "MØRE OG ROMSDAL"
        },
        "municipality": {
            "code": 1504,
            "name": "ÅLESUND"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "353",
    "name": "Akerselva river",
    "geoLocation": {
        "latitude": 59.931355547,
        "longitude": 10.757739543,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=23&p=6794&t=1",
        "alternativeText": "Akerselva - Fabrikkpikene",
        "copyright": "Akerselva - Fabrikkpikene"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "110",
        "name": "Attraction & Culture",
        "code": null
    }],
    "owner": "VisitOSLO as",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "",
        "fax": null,
        "mobile": null,
        "phone": "",
        "streetAddress": null,
        "postalCode": null,
        "city": "Oslo",
        "web":
        "www.oslo.kommune.no/getfile.php/Innhold/Natur,%20kultur%20og%20fritid/Tur-%20og%20friluftsliv/Turkart%20og%20-guider/Turguide%20Akerselva.pdf",
        "bookingUrl": "",
        "county": {
            "code": 0,
            "name": null
        },
        "municipality": {
            "code": 0,
            "name": null
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": {
        "tripAdvisorId": 3478798,
        "tripAdvisorUrl":
        "https://www.tripadvisor.com/Attraction_Review-g190479-d3478798-Reviews-m34784-Akerselva_River-Oslo_Eastern_Norway.html",
        "name": "Akerselva River",
        "avgRating": 4.5,
        "reviewCount": 156,
        "geoId": 190479,
        "type": "attraction",
        "vnExternIds": null
    },
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "10077",
    "name": "Åkrådalen Seter",
    "geoLocation": {
        "latitude": 61.953615086,
        "longitude": 11.52215132,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=44&p=5913&t=1",
        "alternativeText": "Åkrådalen seter",
        "copyright": "Åkrådalen seter"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "23",
        "name": "Hotels & More",
        "code": null
    }],
    "owner": "Destinasjon Røros",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "m-kveen@online.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 99012131",
        "streetAddress": null,
        "postalCode": "2485",
        "city": "Rendalen",
        "web": "www.akradalen.no",
        "bookingUrl": "",
        "county": {
            "code": 4,
            "name": "HEDMARK"
        },
        "municipality": {
            "code": 432,
            "name": "RENDALEN"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "86364",
    "name": "Agder Natural History Museum and Botanical Garden",
    "geoLocation": {
        "latitude": 58.1588,
        "longitude": 8.00371,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=390&p=432&t=1",
        "alternativeText": "Agder Naturmuseum og Botaniske Hage",
        "copyright": "Agder Naturmuseum og Botaniske Hage"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "110",
        "name": "Attraction & Culture",
        "code": null
    }],
    "owner": "Visit Kristiansand",
    "ownerId": null,
    "address": "Gimlevn. 23",
    "contact": {
        "address": "Gimlevn. 23",
        "email": "ekspedisjonen.naturmuseet@kristiansand.kommune.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 38058620",
        "streetAddress": null,
        "postalCode": "4630",
        "city": "Kristiansand",
        "web": "www.uia.no/eksterne-nettsider/naturmuseum",
        "bookingUrl": "",
        "county": {
            "code": 10,
            "name": "VEST-AGDER"
        },
        "municipality": {
            "code": 1001,
            "name": "KRISTIANSAND"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": {
        "tripAdvisorId": 319169,
        "tripAdvisorUrl":
        "https://www.tripadvisor.com/Attraction_Review-g190492-d319169-Reviews-m34784-Agder_Natural_History_Museum_and_Botanical_Garden-Kristiansand_Vest_Agder_S.html",
        "name": "Agder Natural History Museum and Botanical Garden",
        "avgRating": 4.0,
        "reviewCount": 23,
        "geoId": 190492,
        "type": "attraction",
        "vnExternIds": null
    },
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "177174",
    "name": "Aglen camping AS",
    "geoLocation": {
        "latitude": 64.633775916,
        "longitude": 11.066011047,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=288&p=757&t=1",
        "alternativeText": "Aglen",
        "copyright": "Aglen"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "23",
        "name": "Hotels & More",
        "code": null
    }],
    "owner": "Visit Namdalen",
    "ownerId": null,
    "address": "Aglen",
    "contact": {
        "address": "Aglen",
        "email": "booking@aglencamping.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 47973911",
        "streetAddress": null,
        "postalCode": "7819",
        "city": "Namsos",
        "web": "www.aglencamping.no/",
        "bookingUrl": "",
        "county": {
            "code": 17,
            "name": "NORD-TRØNDELAG"
        },
        "municipality": {
            "code": 1703,
            "name": "NAMSOS"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "2571",
    "name": "All-year Christmas Shop",
    "geoLocation": {
        "latitude": 60.39682,
        "longitude": 5.32397,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=1&p=36676&t=1",
        "alternativeText": "Julehuset",
        "copyright": "Julehuset"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "113",
        "name": "Shopping",
        "code": null
    }],
    "owner": "Bergen Reiselivslag",
    "ownerId": null,
    "address": "Holmedalsgården 1",
    "contact": {
        "address": "Holmedalsgården 1",
        "email": "bergen@aviken.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 55215100",
        "streetAddress": null,
        "postalCode": "5003",
        "city": "Bergen",
        "web": "http://www.gifts.no",
        "bookingUrl": "",
        "county": {
            "code": 12,
            "name": "HORDALAND"
        },
        "municipality": {
            "code": 1201,
            "name": "BERGEN"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "177561",
    "name": "Alnes Panorama Venue",
    "geoLocation": {
        "latitude": 62.48684,
        "longitude": 5.97319,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=65&p=9146&t=1",
        "alternativeText": "Alnes Panorama",
        "copyright": "Alnes Panorama"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "20",
        "name": "Meeting Venues",
        "code": null
    }],
    "owner": "Geirangerfjord - Ålesund & Sunnmøre",
    "ownerId": null,
    "address": "Alnes",
    "contact": {
        "address": "Alnes",
        "email": "mail@alnespanorama.com",
        "fax": null,
        "mobile": null,
        "phone": "",
        "streetAddress": null,
        "postalCode": "6055",
        "city": "Giske",
        "web": "http://www.alnespanorama.com",
        "bookingUrl": "",
        "county": {
            "code": 15,
            "name": "MØRE OG ROMSDAL"
        },
        "municipality": {
            "code": 1532,
            "name": "GISKE"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "86827",
    "name": "Amfi Kanebogen",
    "geoLocation": {
        "latitude": 68.77944,
        "longitude": 16.56567,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=397&p=1290&t=1",
        "alternativeText": "Flyfoto",
        "copyright": "Flyfoto"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "113",
        "name": "Shopping",
        "code": null
    }],
    "owner": "Destination Harstad",
    "ownerId": null,
    "address": "Skilleveien 5Kanebogen",
    "contact": {
        "address": "Skilleveien 5Kanebogen",
        "email": "kanebogen@amfi.no",
        "fax": null,
        "mobile": null,
        "phone": "",
        "streetAddress": null,
        "postalCode": "9411",
        "city": "Harstad",
        "web": "http://www.amfi.no",
        "bookingUrl": "",
        "county": {
            "code": 19,
            "name": "TROMS"
        },
        "municipality": {
            "code": 1903,
            "name": "HARSTAD"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "4397",
    "name": "Ålesund Airport Vigra",
    "geoLocation": {
        "latitude": 62.56045,
        "longitude": 6.11252,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=65&p=1743&t=1",
        "alternativeText": "Avinor",
        "copyright": "Avinor"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "19",
        "name": "Getting Here & Around",
        "code": null
    }],
    "owner": "Geirangerfjord - Ålesund & Sunnmøre",
    "ownerId": null,
    "address": "Ålesund Lufthavn Vigra",
    "contact": {
        "address": "Ålesund Lufthavn Vigra",
        "email": "tor.haande@avinor.no",
        "fax": null,
        "mobile": null,
        "phone": "",
        "streetAddress": null,
        "postalCode": "6040",
        "city": "Giske",
        "web": "http://www.avinor.no/lufthavn/alesund",
        "bookingUrl": "",
        "county": {
            "code": 15,
            "name": "MØRE OG ROMSDAL"
        },
        "municipality": {
            "code": 1532,
            "name": "GISKE"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "91984",
    "name": "Along the Trondheim lane",
    "geoLocation": {
        "latitude": 63.520388722,
        "longitude": 9.1118928997,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=95&p=1953&t=1",
        "alternativeText": "DS Hitra",
        "copyright": "DS Hitra"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "110",
        "name": "Attraction & Culture",
        "code": null
    }],
    "owner": "KystNorge AS",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "post@kystmuseet.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 72444010",
        "streetAddress": null,
        "postalCode": "7246",
        "city": "Hitra",
        "web": "www.kystmuseet.no",
        "bookingUrl": "",
        "county": {
            "code": 16,
            "name": "SØR-TRØNDELAG"
        },
        "municipality": {
            "code": 1617,
            "name": "HITRA"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "9774",
    "name": "Alpin Apartments Sørlia",
    "geoLocation": {
        "latitude": 61.23449,
        "longitude": 10.45647,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=277&p=8443&t=1",
        "alternativeText": "Alpin Apartments Sørlia",
        "copyright": "Alpin Apartments Sørlia"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "23",
        "name": "Hotels & More",
        "code": null
    }],
    "owner": "Visit Lillehammer",
    "ownerId": null,
    "address": "Sørlia 130",
    "contact": {
        "address": "Sørlia 130",
        "email": "post@hafjellresort.com",
        "fax": null,
        "mobile": null,
        "phone": " +47 61285550",
        "streetAddress": null,
        "postalCode": "2636",
        "city": "Øyer",
        "web":
        "http://www2.hafjellresort.no/no/overnatting/a62040/alpin-apartments-s%C3%B8rlia/detaljer",
        "bookingUrl": "",
        "county": {
            "code": 5,
            "name": "OPPLAND"
        },
        "municipality": {
            "code": 521,
            "name": "ØYER"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "5657",
    "name": "Ål Stave Church Museum",
    "geoLocation": {
        "latitude": 60.6281,
        "longitude": 8.55318,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=343&p=8053&t=1",
        "alternativeText": "Portalen",
        "copyright": "Portalen"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "110",
        "name": "Attraction & Culture",
        "code": null
    }],
    "owner": "Hallingdal Reiseliv",
    "ownerId": null,
    "address": "Gartnarvegen 5",
    "contact": {
        "address": "Gartnarvegen 5",
        "email": "post@alturistinfo.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 32081060",
        "streetAddress": null,
        "postalCode": "3570",
        "city": "Ål",
        "web": "http://www.al.no",
        "bookingUrl": "",
        "county": {
            "code": 6,
            "name": "BUSKERUD"
        },
        "municipality": {
            "code": 619,
            "name": "ÅL"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "126101",
    "name": "Albmi adventures",
    "geoLocation": {
        "latitude": 67.2784087826,
        "longitude": 14.4030761719,
        "elevation": 0
    },
    "image": {
        "url": "http://images.citybreak.com/image.aspx?ImageId=2834210",
        "alternativeText": "adventureweekend11.jpg",
        "copyright": "adventureweekend11.jpg"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "115",
        "name": "The Great Outdoors",
        "code": null
    }],
    "owner": "Visit Bodö",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "booking@albmi.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 94053795",
        "streetAddress": null,
        "postalCode": null,
        "city": "",
        "web": "http://www.albmi.com",
        "bookingUrl": "",
        "county": {
            "code": 0,
            "name": null
        },
        "municipality": {
            "code": 0,
            "name": null
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "173084",
    "name": "Ål Kulturhus",
    "geoLocation": null,
    "image": {
        "url": "http://media.tellus.no/images/?d=343&p=408&t=1",
        "alternativeText": "Veslesalen",
        "copyright": "Veslesalen"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": true,
    "categories": [{
        "id": "23",
        "name": "Hotels & More",
        "code": null
    }],
    "owner": "Hallingdal Reiseliv",
    "ownerId": null,
    "address": "Myren 40, Sundre",
    "contact": {
        "address": "Myren 40, Sundre",
        "email": "aal.kulturhus@hallingnett.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 32085100",
        "streetAddress": null,
        "postalCode": "3570",
        "city": "Ål",
        "web": "http://www.aal.kulturhus.no",
        "bookingUrl": "",
        "county": {
            "code": 6,
            "name": "BUSKERUD"
        },
        "municipality": {
            "code": 619,
            "name": "ÅL"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "1141",
    "name": "Apotekern Kafe",
    "geoLocation": {
        "latitude": 62.47107,
        "longitude": 6.15078,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=65&p=211&t=1",
        "alternativeText": "The Art Nouveau Centre",
        "copyright": "The Art Nouveau Centre"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "114",
        "name": "Taste Norway",
        "code": null
    }],
    "owner": "Geirangerfjord - Ålesund & Sunnmøre",
    "ownerId": null,
    "address": "Apotekergt. 16",
    "contact": {
        "address": "Apotekergt. 16",
        "email": "nina@jugendstilsenteret.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 70104978",
        "streetAddress": null,
        "postalCode": "6004",
        "city": "Ålesund",
        "web": "www.jugendstilsenteret.no",
        "bookingUrl": "",
        "county": {
            "code": 15,
            "name": "MØRE OG ROMSDAL"
        },
        "municipality": {
            "code": 1504,
            "name": "ÅLESUND"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "126644",
    "name": "Aquaculture Centre – Visit a Norwegian Salmon Farm",
    "geoLocation": {
        "latitude": 68.6018143521,
        "longitude": 15.3817935921,
        "elevation": 0
    },
    "image": {
        "url": "http://images.citybreak.com/image.aspx?ImageId=2914352",
        "alternativeText": "akvakultur1.jpeg",
        "copyright": "akvakultur1.jpeg"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "110",
        "name": "Attraction & Culture",
        "code": null
    }],
    "owner": "Vesterålen Reiseliv",
    "ownerId": null,
    "address": "Gårdsøyveien 32",
    "contact": {
        "address": "Gårdsøyveien 32",
        "email": "post@akvakulturivesteralen.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 95881822",
        "streetAddress": null,
        "postalCode": "8406",
        "city": "Sortland",
        "web": "http://www.akvakulturivesteralen.no",
        "bookingUrl": "",
        "county": {
            "code": 18,
            "name": "NORDLAND"
        },
        "municipality": {
            "code": 1870,
            "name": "SORTLAND"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "126604",
    "name": "Arctic autumn on wheels - Huset på Yttersiden",
    "geoLocation": {
        "latitude": 68.6541451219,
        "longitude": 14.6369022725,
        "elevation": 0
    },
    "image": {
        "url": "http://images.citybreak.com/image.aspx?ImageId=2924127",
        "alternativeText": "ringstadsykkel1.jpg",
        "copyright": "ringstadsykkel1.jpg"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "115",
        "name": "The Great Outdoors",
        "code": null
    }],
    "owner": "Vesterålen Reiseliv",
    "ownerId": null,
    "address": "Ringstad",
    "contact": {
        "address": "Ringstad",
        "email": "karina@yttersiden.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 76137480",
        "streetAddress": null,
        "postalCode": "8475",
        "city": "Bø i Vesterålen",
        "web": "http://www.yttersiden.no",
        "bookingUrl": "",
        "county": {
            "code": 18,
            "name": "NORDLAND"
        },
        "municipality": {
            "code": 1867,
            "name": "BØ (N.)"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "189157",
    "name": "Angling in Bygland",
    "geoLocation": {
        "latitude": 58.82435,
        "longitude": 7.78628,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=108&p=503697&t=1",
        "alternativeText": "Trouts from Otra",
        "copyright": "Trouts from Otra"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "115",
        "name": "The Great Outdoors",
        "code": null
    }],
    "owner": "Setesdal",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "post@glashytta.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 37934040",
        "streetAddress": null,
        "postalCode": null,
        "city": "Bygland",
        "web": "www.bygland.kommune.no",
        "bookingUrl": "",
        "county": {
            "code": 0,
            "name": null
        },
        "municipality": {
            "code": 0,
            "name": null
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "11827",
    "name": "Angvik Gamle Handelssted",
    "geoLocation": {
        "latitude": 62.89209,
        "longitude": 8.09006,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=64&p=4891&t=1",
        "alternativeText": "Angvik gamle handelssted",
        "copyright": "Angvik gamle handelssted"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "114",
        "name": "Taste Norway",
        "code": null
    }],
    "owner": "VisitNordvest",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "post@angvik-hotel.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 71291300",
        "streetAddress": null,
        "postalCode": "6636",
        "city": "Gjemnes",
        "web": "www.angvik-hotell.no",
        "bookingUrl": "",
        "county": {
            "code": 15,
            "name": "MØRE OG ROMSDAL"
        },
        "municipality": {
            "code": 1557,
            "name": "GJEMNES"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "190881",
    "name": "Åndalsnes-Trollstigen-Geiranger (one way)",
    "geoLocation": {
        "latitude": 62.56745,
        "longitude": 7.68995,
        "elevation": 0
    },
    "image": null,
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "118",
        "name": "Tours & Sightseeing",
        "code": null
    }],
    "owner": "Geirangerfjord - Ålesund & Sunnmøre",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "info@visitalesund.com",
        "fax": null,
        "mobile": null,
        "phone": " +47 70163430",
        "streetAddress": null,
        "postalCode": "6003",
        "city": "Ålesund",
        "web": "www.visitalesund.com",
        "bookingUrl": "",
        "county": {
            "code": 15,
            "name": "MØRE OG ROMSDAL"
        },
        "municipality": {
            "code": 1504,
            "name": "ÅLESUND"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "8564",
    "name": "Åmfoss Bridge",
    "geoLocation": {
        "latitude": 58.76942,
        "longitude": 8.48407,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=12&p=6282&t=1",
        "alternativeText": "Åmfoss bru",
        "copyright": "Åmfoss bru"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "110",
        "name": "Attraction & Culture",
        "code": null
    }],
    "owner": "Arendal Turistkontor",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "postmottak@amli.kommune.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 37185264",
        "streetAddress": null,
        "postalCode": "4865",
        "city": "Åmli",
        "web": "http://www.amli.kommune.no",
        "bookingUrl": "",
        "county": {
            "code": 9,
            "name": "AUST-AGDER"
        },
        "municipality": {
            "code": 929,
            "name": "ÅMLI"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "11904",
    "name": "Åmotdalshytta mountain lodge",
    "geoLocation": {
        "latitude": 62.35921,
        "longitude": 9.19749,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=64&p=10410&t=1",
        "alternativeText": "Åmotdalshytta Sommer",
        "copyright": "Åmotdalshytta Sommer"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "23",
        "name": "Hotels & More",
        "code": null
    }],
    "owner": "VisitNordvest",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "turist@knt.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 71676937",
        "streetAddress": null,
        "postalCode": null,
        "city": "Kristiansund",
        "web": "www.kntur.no",
        "bookingUrl": "",
        "county": {
            "code": 0,
            "name": null
        },
        "municipality": {
            "code": 0,
            "name": null
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "11544",
    "name": "Apartment in Vestlia",
    "geoLocation": {
        "latitude": 8.21814,
        "longitude": 60.5229,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=341&p=2329&t=1",
        "alternativeText": "Utleiehus på Geilo",
        "copyright": "Utleiehus på Geilo"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "23",
        "name": "Hotels & More",
        "code": null
    }],
    "owner": "Visit Geilo AS",
    "ownerId": null,
    "address": "Gamle Skurdalsvegen 231",
    "contact": {
        "address": "Gamle Skurdalsvegen 231",
        "email": "post@geilo.no",
        "fax": null,
        "mobile": null,
        "phone": "",
        "streetAddress": null,
        "postalCode": "3580",
        "city": "Hol",
        "web": "https://www.airbnb.no/rooms/386628?alsm=1&s=gNYE",
        "bookingUrl": "",
        "county": {
            "code": 6,
            "name": "BUSKERUD"
        },
        "municipality": {
            "code": 620,
            "name": "HOL"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "142417",
    "name": "Apartments at Moen Båtbyggeri",
    "geoLocation": {
        "latitude": 58.72556,
        "longitude": 9.07623,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=362&p=4675&t=1",
        "alternativeText": "K. Christensens båtbyggeri",
        "copyright": "K. Christensens båtbyggeri"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "23",
        "name": "Hotels & More",
        "code": null
    }],
    "owner": "Risør Turistinformasjon",
    "ownerId": null,
    "address": "Hammeråker",
    "contact": {
        "address": "Hammeråker",
        "email": "tharald@hobbyas.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 37023289",
        "streetAddress": null,
        "postalCode": "4950",
        "city": "Risør",
        "web": "http://www.batbyggeri.no",
        "bookingUrl": "",
        "county": {
            "code": 9,
            "name": "AUST-AGDER"
        },
        "municipality": {
            "code": 901,
            "name": "RISØR"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "8797",
    "name": "Around lake Bergsjøen Ål in Hallingdal",
    "geoLocation": {
        "latitude": 60.71616,
        "longitude": 8.28797,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=343&p=5610&t=1",
        "alternativeText": "Bergsjøen rundt",
        "copyright": "Bergsjøen rundt"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "115",
        "name": "The Great Outdoors",
        "code": null
    }],
    "owner": "Hallingdal Reiseliv",
    "ownerId": null,
    "address": "Bergsjøområdet",
    "contact": {
        "address": "Bergsjøområdet",
        "email": "post@alturistinfo.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 32081060",
        "streetAddress": null,
        "postalCode": "3570",
        "city": "Ål",
        "web": "www.al.no",
        "bookingUrl": "",
        "county": {
            "code": 6,
            "name": "BUSKERUD"
        },
        "municipality": {
            "code": 619,
            "name": "ÅL"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "186314",
    "name": "Alveland Shop & Café",
    "geoLocation": {
        "latitude": 69.1068035,
        "longitude": 15.9623401,
        "elevation": 0
    },
    "image": {
        "url": "http://images.citybreak.com/image.aspx?ImageId=4246459",
        "alternativeText": "",
        "copyright": ""
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "114",
        "name": "Taste Norway",
        "code": null
    }],
    "owner": "Vesterålen Reiseliv",
    "ownerId": null,
    "address": "Bankveien",
    "contact": {
        "address": "Bankveien",
        "email": "post@alveland.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 76146149",
        "streetAddress": null,
        "postalCode": "8485",
        "city": "Dverberg",
        "web": "http://alveland.no/",
        "bookingUrl": "",
        "county": {
            "code": 18,
            "name": "NORDLAND"
        },
        "municipality": {
            "code": 1871,
            "name": "ANDØY"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "1697",
    "name": "Amanda Shopping Centre - the regions largest mall",
    "geoLocation": {
        "latitude": 59.39489,
        "longitude": 5.33156,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=83&p=1004885&t=1",
        "alternativeText": "Amanda Storsenter",
        "copyright": "Amanda Storsenter"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "113",
        "name": "Shopping",
        "code": null
    }],
    "owner": "Destinasjon Haugesund & Haugalandet",
    "ownerId": null,
    "address": "Longhammarveien 27",
    "contact": {
        "address": "Longhammarveien 27",
        "email": "amanda@steenstrom.com",
        "fax": null,
        "mobile": null,
        "phone": " +47 52719700",
        "streetAddress": null,
        "postalCode": "5536",
        "city": "Haugesund",
        "web": "http://www.amandastorsenter.no",
        "bookingUrl": "",
        "county": {
            "code": 11,
            "name": "ROGALAND"
        },
        "municipality": {
            "code": 1106,
            "name": "HAUGESUND"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "11647",
    "name": "Arctic Mountain Pilgrim",
    "geoLocation": {
        "latitude": 63.399018,
        "longitude": 10.372298,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=27&p=4671&t=1",
        "alternativeText": "Forrolhogna",
        "copyright": "Forrolhogna"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "115",
        "name": "The Great Outdoors",
        "code": null
    }],
    "owner": "Visit Trondheim  AS",
    "ownerId": null,
    "address": "Skjermveien 51B",
    "contact": {
        "address": "Skjermveien 51B",
        "email": "hcbrimi@gmail.com",
        "fax": null,
        "mobile": null,
        "phone": "",
        "streetAddress": null,
        "postalCode": "7023",
        "city": "Trondheim",
        "web": "www.tempusfugittravel.com",
        "bookingUrl": "",
        "county": {
            "code": 16,
            "name": "SØR-TRØNDELAG"
        },
        "municipality": {
            "code": 1601,
            "name": "TRONDHEIM"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "126271",
    "name": "Arctic sea fishing",
    "geoLocation": {
        "latitude": 69.6948399,
        "longitude": 29.3781932,
        "elevation": 0
    },
    "image": {
        "url": "http://images.citybreak.com/image.aspx?ImageId=2959636",
        "alternativeText": "images[1]",
        "copyright": "images[1]"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "115",
        "name": "The Great Outdoors",
        "code": null
    }],
    "owner": "Book Finnmark",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "info@neidenfjellstue.com",
        "fax": null,
        "mobile": null,
        "phone": " +47 78996141",
        "streetAddress": null,
        "postalCode": "9930",
        "city": "Neiden",
        "web": "http://www.neidenfjellstue.com",
        "bookingUrl": "",
        "county": {
            "code": 20,
            "name": "FINNMARK"
        },
        "municipality": {
            "code": 2030,
            "name": "SØR-VARANGER"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "3701",
    "name": "Arena Overøye - alpint",
    "geoLocation": {
        "latitude": 62.41892,
        "longitude": 7.21991,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=65&p=1602&t=1",
        "alternativeText": "Map",
        "copyright": "Map"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "115",
        "name": "The Great Outdoors",
        "code": null
    }],
    "owner": "Geirangerfjord - Ålesund & Sunnmøre",
    "ownerId": null,
    "address": "Overøye",
    "contact": {
        "address": "Overøye",
        "email": "rune.stoversten@mimer.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 90719011",
        "streetAddress": null,
        "postalCode": "6250",
        "city": "Stordal",
        "web": "www.stordalalpinsenter.no",
        "bookingUrl": "",
        "county": {
            "code": 15,
            "name": "MØRE OG ROMSDAL"
        },
        "municipality": {
            "code": 1526,
            "name": "STORDAL"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": {
        "tripAdvisorId": 3515909,
        "tripAdvisorUrl":
        "https://www.tripadvisor.com/Attraction_Review-g2416780-d3515909-Reviews-m34784-Stordal_Alpinsenter_Arena_Overoye-Stordal_Municipality_More_og_Romsdal_We.html",
        "name": "Stordal Alpinsenter Arena Overoye",
        "avgRating": 4.0,
        "reviewCount": 1,
        "geoId": 2416780,
        "type": "attraction",
        "vnExternIds": null
    },
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "2311",
    "name": "Atna fiskeforening",
    "geoLocation": {
        "latitude": 61.48698,
        "longitude": 11.017931,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=324&p=246&t=1",
        "alternativeText": "Piktjønna",
        "copyright": "Piktjønna"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "115",
        "name": "The Great Outdoors",
        "code": null
    }],
    "owner": "Visit Hedmark AS",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "hbond@online.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 47462881",
        "streetAddress": null,
        "postalCode": "2477",
        "city": "Stor-Elvdal",
        "web": "",
        "bookingUrl": "",
        "county": {
            "code": 4,
            "name": "HEDMARK"
        },
        "municipality": {
            "code": 430,
            "name": "STOR-ELVDAL"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "174924",
    "name": "Atelier Midtun",
    "geoLocation": {
        "latitude": 60.81523,
        "longitude": 5.80195,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=1&p=38159&t=1",
        "alternativeText": "Atelier Midtun",
        "copyright": "Atelier Midtun"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "110",
        "name": "Attraction & Culture",
        "code": null
    }],
    "owner": "Bergen Reiselivslag",
    "ownerId": null,
    "address": "Mo 20",
    "contact": {
        "address": "Mo 20",
        "email": "jarle.midtun@gmail.com",
        "fax": null,
        "mobile": null,
        "phone": " +47 41663853",
        "streetAddress": null,
        "postalCode": "5729",
        "city": "Modalen",
        "web": "http://www.atelier-midtun.com",
        "bookingUrl": "",
        "county": {
            "code": 12,
            "name": "HORDALAND"
        },
        "municipality": {
            "code": 1252,
            "name": "MODALEN"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "12004",
    "name": "Atlanten Turistsenter",
    "geoLocation": {
        "latitude": 63.12562,
        "longitude": 7.73841,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=64&p=5859&t=1",
        "alternativeText": "Atlanten Camping",
        "copyright": "Atlanten Camping"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "23",
        "name": "Hotels & More",
        "code": null
    }],
    "owner": "VisitNordvest",
    "ownerId": null,
    "address": "Dalaveien 22",
    "contact": {
        "address": "Dalaveien 22",
        "email": "resepsjonen@atlanten.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 71671104",
        "streetAddress": null,
        "postalCode": "6511",
        "city": "Kristiansund",
        "web": "www.atlanten.no",
        "bookingUrl": "",
        "county": {
            "code": 15,
            "name": "MØRE OG ROMSDAL"
        },
        "municipality": {
            "code": 1505,
            "name": "KRISTIANSUND"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "189917",
    "name": "Bastian Kongsvinger",
    "geoLocation": {
        "latitude": 60.190636635,
        "longitude": 11.998627029,
        "elevation": 0
    },
    "image": null,
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "114",
        "name": "Taste Norway",
        "code": null
    }],
    "owner": "Visit Hedmark AS",
    "ownerId": null,
    "address": "Rådhusplassen 11",
    "contact": {
        "address": "Rådhusplassen 11",
        "email": "post@bastiankongsvinger.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 62814646",
        "streetAddress": null,
        "postalCode": "2212",
        "city": "Kongsvinger",
        "web": "",
        "bookingUrl": "",
        "county": {
            "code": 4,
            "name": "HEDMARK"
        },
        "municipality": {
            "code": 402,
            "name": "KONGSVINGER"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": {
        "tripAdvisorId": 7594437,
        "tripAdvisorUrl":
        "https://www.tripadvisor.com/Restaurant_Review-g668801-d7594437-Reviews-m34784-Bastian_bar_and_restaurant-Kongsvinger_Kongsvinger_Municipality_Hedmark_Ea.html",
        "name": "Bastian bar and restaurant",
        "avgRating": 4.5,
        "reviewCount": 19,
        "geoId": 668801,
        "type": "restaurant",
        "vnExternIds": null
    },
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "12121",
    "name": "Auglend-Vandringshavn",
    "geoLocation": {
        "latitude": 58.41606,
        "longitude": 5.97955,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=85&p=12158&t=1",
        "alternativeText": "Auglend-Vandringshavn",
        "copyright": "Auglend-Vandringshavn"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "111",
        "name": "Family Fun",
        "code": null
    }],
    "owner": "Region Stavanger",
    "ownerId": null,
    "address": "Eigerøy",
    "contact": {
        "address": "Eigerøy",
        "email": "post@eigersund.kommune.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 51468000",
        "streetAddress": null,
        "postalCode": "4370",
        "city": "Eigersund",
        "web": "www.eigersund.kommune.no/auglend.5063657-259858.html",
        "bookingUrl": "",
        "county": {
            "code": 11,
            "name": "ROGALAND"
        },
        "municipality": {
            "code": 1101,
            "name": "EIGERSUND"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "5451",
    "name": "Aulestad - Bjørnstjerne Bjørnsons\u0027 home",
    "geoLocation": {
        "latitude": 61.2208,
        "longitude": 10.27088,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=277&p=2795&t=1",
        "alternativeText": "Aulestad",
        "copyright": "Aulestad"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": true,
    "categories": [{
        "id": "110",
        "name": "Attraction & Culture",
        "code": null
    }],
    "owner": "Visit Lillehammer",
    "ownerId": null,
    "address": "Aulestadvegen 6-14",
    "contact": {
        "address": "Aulestadvegen 6-14",
        "email": "post@aulestad.no",
        "fax": null,
        "mobile": null,
        "phone": " +47 61288900",
        "streetAddress": null,
        "postalCode": "2656",
        "city": "Gausdal",
        "web": "www.aulestad.no",
        "bookingUrl": "",
        "county": {
            "code": 5,
            "name": "OPPLAND"
        },
        "municipality": {
            "code": 522,
            "name": "GAUSDAL"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "276",
    "name": "Bærum Art Society",
    "geoLocation": {
        "latitude": 59.89354,
        "longitude": 10.52308,
        "elevation": 0
    },
    "image": {
        "url": "http://media.tellus.no/images/?d=10&p=2293698&t=1",
        "alternativeText": "Bærum kunstforening",
        "copyright": "Bærum kunstforening"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "110",
        "name": "Attraction & Culture",
        "code": null
    }],
    "owner": "Akershus Reiselivsråd",
    "ownerId": null,
    "address": "Engervannsveien 31",
    "contact": {
        "address": "Engervannsveien 31",
        "email": "",
        "fax": null,
        "mobile": null,
        "phone": "",
        "streetAddress": null,
        "postalCode": "1337",
        "city": "Bærum",
        "web": "https://baerumkunstforening.no/",
        "bookingUrl": "",
        "county": {
            "code": 2,
            "name": "AKERSHUS"
        },
        "municipality": {
            "code": 219,
            "name": "BÆRUM"
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}, {
    "id": "4744",
    "name": "Beaches",
    "geoLocation": null,
    "image": {
        "url": "http://media.tellus.no/images/?d=351&p=6842&t=1",
        "alternativeText": "Sjøbadet",
        "copyright": "Sjøbadet"
    },
    "hasFoodPrints": false,
    "hasGreenTravel": false,
    "categories": [{
        "id": "111",
        "name": "Family Fun",
        "code": null
    }],
    "owner": "VisitMOSS AS",
    "ownerId": null,
    "address": "",
    "contact": {
        "address": "",
        "email": "",
        "fax": null,
        "mobile": null,
        "phone": "",
        "streetAddress": null,
        "postalCode": null,
        "city": "Moss",
        "web": "",
        "bookingUrl": "",
        "county": {
            "code": 0,
            "name": null
        },
        "municipality": {
            "code": 0,
            "name": null
        }
    },
    "startTimeToday": null,
    "endTimeToday": null,
    "distanceFromClient": 0,
    "tripAdvisorProduct": null,
    "externalSystemId": null,
    "externalSource": null,
    "searchResultScore": 1
}]''')
