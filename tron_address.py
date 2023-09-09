import os
import hashlib
import base58
from coincurve import PublicKey
from Crypto.Hash import keccak


def generate_tron_key_pair():
    """Generates a TRON key pair (private key, public key, address, base58 address)"""
    private_key = os.urandom(32)
    public_key = PublicKey.from_valid_secret(private_key).format(compressed=False)[1:]
    keccak_hash = keccak.new(digest_bits=256, data=public_key).digest()
    tron_address = "41" + keccak_hash[-20:].hex()
    return {
        "private_key": private_key.hex(),
        "public_key": public_key.hex(),
        "address": tron_address,
        "base58_address": to_base58(tron_address),
    }


def to_base58(hex_address):
    addr_bytes = bytes.fromhex(hex_address)
    double_hash = hashlib.sha256(hashlib.sha256(addr_bytes).digest()).digest()
    checksum = double_hash[:4]
    full_bytes = addr_bytes + checksum
    return base58.b58encode(full_bytes).decode("utf-8")


def from_base58(base58_address):
    decoded = base58.b58decode(base58_address)
    addr_bytes = decoded[:-4]
    checksum = decoded[-4:]
    double_hash = hashlib.sha256(hashlib.sha256(addr_bytes).digest()).digest()
    new_checksum = double_hash[:4]
    if new_checksum != checksum:
        raise ValueError("Invalid checksum")
    return addr_bytes.hex()


# Get TRON key pair
key_pair = generate_tron_key_pair()
print("NEW TRON KEY PAIR")
print("Private Key: ", key_pair["private_key"])
print("Public Key: ", key_pair["public_key"])
print("Address (Hex): ", key_pair["address"])
print("Address (Base58): ", key_pair["base58_address"])
print("*" * 50)

# Example usage of conversion functions
example_base58 = "TNPeeaaFB7K9cmo4uQpcU32zGK8G1NYqeL"
example_hex = "418840E6C55B9ADA326D211D818C34A994AECED808"

print("Converted from Base58 to Hex: ", from_base58(example_base58))
print("Converted from Hex to Base58: ", to_base58(example_hex))
