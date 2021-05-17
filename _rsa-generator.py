import os
import fileinput
import time

private_key_file = "private.pem"
public_key_file = "public.pem"
kong_consumers = "kong-consumers.yaml"
kong_consumers_placeholder = "{rsa_public_key}"

# generate private RSA key and generate public RSA key from private
print(">>>> Generating the RSA keys ...")
os.system("rm -f {} {}".format(private_key_file, public_key_file))
os.system("openssl genrsa -out {} 2048".format(private_key_file))
os.system("openssl rsa -in {} -outform PEM -pubout -out {}".format(private_key_file, public_key_file))

print(">>> Reading public key")
public_key = open(public_key_file, 'r').readlines()

# format public key adding spacing before so it replaces it on yaml correctly
spacing = "    "
formated_public_key = ""
for line in public_key:
    formated_public_key += "{}{}".format(spacing, line)

print(">>> Replacing placeholder on kong consumers with public key")
with fileinput.FileInput(kong_consumers, inplace=True, backup='.bak') as file:
    for line in file:
        print(line.replace(kong_consumers_placeholder, formated_public_key), end='')