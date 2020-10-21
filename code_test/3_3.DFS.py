
import base64
import json

def main():
    header = {"alg":"HS256","typ":"JWT"}
    header_string = json.dumps(header)
    byte_header = header_string.encode("UTF-8")
    encoded_header = base64.b64encode(byte_header).decode("utf-8")
    encoded_header = str(encoded_header).replace('=', "")
    print(encoded_header)


    payload = {
        "iss": "velopert.com",
        "exp": "1485270000000",
        "https://velopert.com/jwt_claims/is_admin": True,
        "userId": "11028373727102",
        "username": "velopert"
    }
    payload_string = json.dumps(payload)
    byte_payload = payload_string.encode("UTF-8")
    encoded_payload = base64.b64encode(byte_payload).decode("utf-8")
    encoded_payload = str(encoded_payload).replace('=', "")
    print(encoded_payload)
    print(encoded_header+"."+encoded_payload)

    import hmac
    import hashlib
    api_key = 2342342348273482374343434
    API_SECRET = 892374928347928347283473

    message = '{}'.format(encoded_header+"."+encoded_payload)
    signature = hmac.new(
        bytes(API_SECRET),
        msg=message,
        digestmod=hashlib.sha256()
    ).hexdigest().upper()

    print(signature)
    return 0


if __name__ == "__main__":
    main()

