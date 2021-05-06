import requests

# cid = inputs['cid']
# measurementId = "G-"+inputs['measurementId']
# apiSecret = inputs['apiSecret']
# eventName = inputs["eventName"]
# currency = inputs["currency"]
# value = inputs["value"]
# tid = inputs["tid"]

cid = 1234
measurementId = "G-1234"
apiSecret = 1234
eventName = "ruler_phone_call"
currency = "GBP"
value = 10
tid = "1234ASKFUEIQ235"


def main():

    url = "https://www.google-analytics.com/mp/collect?measurement_id=%s&api_secret=%s" % (
        measurementId, apiSecret)
    transaction = False
    params = {}
    if transaction:
        params = {
            "currency": currency,
            "value": value,
            "transaction_id": tid
        }

    data = {
        "client_id": cid,
        "events": [{
            "name": eventName,
            "params": params
        }]
    }

    req = requests.post(url, params=data)
    print(req.status_code)
    print(req.text)


if __name__ == '__main__':
    main()
