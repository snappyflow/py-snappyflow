from hashlib import sha256
import base64
from Crypto import Random
from Crypto.Cipher import AES
import json

__CP_ENCRYPTED_KEY = "U25hcHB5RmxvdzEyMzQ1Ng=="
# __key = 'SnappyFlow123456'.encode('utf-8')

def get_trace_config(profile_key):

    unpad = lambda s : s[0:-ord(s[-1:])]

    key = base64.b64decode(__CP_ENCRYPTED_KEY)
    # profile_key = '1saLgj1D4xFfQV8oozU4DwzwnDovmWT+sFl7SxpcEWvs1LNSSdGWZ9s/AwARQNLMo86ZknbXjFfzWfH8iL3v+6nHrOQb54rY8jpC9/hd5LCjz3CczAo39mTNhEM5iewj0hFsvupbKqQ0cYavFDPf/lnbVz489XGyHM0WCD7h8u1WaGIQK1iBFgxCCgHze8TlHMHoob8vvzDvqlvi8rh4kXWQu2+QynkeU+ByqoLjL8cXIVdq3xx2umf20ygW1nph3gOZm7TmFUq9kTN9pht9DCVwQ1fiBx8MEfbKukhBbM1rvRQttpIWY8pS/vDLbQwJyLNlyA4NkOu5TY3zMWgdJz4K3ORaXOruCYu/KIxbUBkFyorvk/iVsxhbZvJ3zAx8FOS/sZn/2Z48c2fKlt3Thw=='

    enc = base64.b64decode(profile_key)
    iv = enc[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv )
    message = unpad(cipher.decrypt( enc[16:] )).decode('utf-8')
    try:
        data = json.loads(message)
        trace_data = {}
        for key, value in data.items():
            if key.lower().find('trace') > -1:
                trace_data[key] = value
        return trace_data
    except Exception as e:
        raise ValueError("Invalid profile key.")