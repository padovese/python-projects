json = {
    "payment_code": "6B2F4926EEFC11EAADC10242AC120008",
    "reference_code": "{{reference_code}}",
    "total_amount": 20,
    "refunded_amount": 0,
    "refund_amount": 48.56,
    "refundable_amount": 100,
    "refund_amount_net": 95,
    "refund_type": "PARTIAL",
    "force_refund": False,
    "pending_expires_in": 60,
    "change_source": "IBANKING",
    "change_agent": "agent",
    "non_refundable_fees": {
        "fee1": 0.1
    }
}

print json

print json['change_source']
print json['non_refundable_fees']
print json['non_refundable_fees']['fee1']

print len(json)