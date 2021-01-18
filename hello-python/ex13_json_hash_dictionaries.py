#this is actually a hash, or in python it wd be called dictionaries aka dict

json = {
    "code": "6B2F4926EEFC11EAADC10242AC120008",
    "reference_code": "{{reference_code}}",
    "amount": 20,
    "ded_amount": 0,
    "und_amount": 48.56,
    "dable_amount": 100,
    "amount_net": 95,
    "type": "PARTIAL",
    "force": False,
    "expires_in": 60,
    "source": "IBANKING",
    "agent": "agent",
    "non_ref": {
        "fee1": 0.1
    }
}

print json

print json['source']
print json['non_ref']
print json['non_ref']['fee1']

print len(json)

json["new_field"] = "some value"

print json

del json["new_field"]

print json