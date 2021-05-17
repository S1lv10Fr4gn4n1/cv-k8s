import jwt

private_key_file = "private.pem"
public_key_file = "public.pem"
iss = "my-dummy-key"
payload = {"sub": "YWJhY2F0ZQ==", "name": "s1lv10", "exp": 1652531966, "nbf": 1621003166}

# generate jwt token using private and public keys
print(">>>> Generating the JWT token ...")
private_key = open(private_key_file, 'r').read()
public_key = open(public_key_file, 'r').read()
headers = {"iss": iss}
encoded = jwt.encode(payload, private_key, algorithm="RS256", headers = headers)
print(encoded)