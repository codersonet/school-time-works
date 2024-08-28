import os

# Generate a random 24-byte string and convert it to a hex representation
secret_key = os.urandom(24).hex()

# Print the secret key with a message
print(f"Your secret key: {secret_key}")
