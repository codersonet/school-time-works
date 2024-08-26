import os

# Generate a random 24-byte string and convert it to a hex representation
secret_key = os.urandom(24).hex()
print(secret_key)
