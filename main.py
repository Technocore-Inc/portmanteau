import hashlib
import os
import base58
from bitcoinlib.keys import Key, HDKey
import bech32
import ecdsa
from eth_hash.auto import keccak
from eth_keys import keys
import mnemonic


def print_symbol_to_end_of_line(symbol):
    """Print a symbol to the end of the terminal line"""
    columns, _ = os.get_terminal_size()
    print(symbol * columns)


def compressed_to_uncompressed_public_key(compressed_public_key_hex):
    """Convert a compressed public key in hex format to an uncompressed public key"""
    # Convert the compressed public key hex to bytes
    compressed_public_key_bytes = bytes.fromhex(compressed_public_key_hex)

    # Get the ECDSA curve for SECP256k1
    curve = ecdsa.SECP256k1

    # Determine the parity of the Y coordinate from the compressed public key format
    is_even = compressed_public_key_bytes[0] == 0x02

    # Get the X coordinate from the compressed public key
    x = ecdsa.util.string_to_number(compressed_public_key_bytes[1:])

    # Calculate the corresponding Y coordinate
    alpha = (pow(x, 3, curve.curve.p()) + 7) % curve.curve.p()
    y = pow(alpha, (curve.curve.p() + 1) // 4, curve.curve.p())

    # Correct the Y coordinate based on its parity
    if is_even != (y % 2 == 0):
        y = curve.curve.p() - y

    # Construct the uncompressed public key
    uncompressed_public_key_bytes = b'\x04' + \
        x.to_bytes(32, 'big') + y.to_bytes(32, 'big')

    return uncompressed_public_key_bytes.hex()


def get_master_private_key(mnemonic_code):
    """Generate the master private key from a mnemonic phrase"""
    seed = mnemonic.Mnemonic.to_seed(mnemonic_code)
    hd_key = HDKey.from_seed(seed)
    return hd_key


def private_key_to_wif(private_key_hex):
    private_key_bytes = bytes.fromhex(private_key_hex)
    private_key_bytes_with_prefix = b"\x80" + private_key_bytes
    sha256_1 = hashlib.sha256(private_key_bytes_with_prefix).digest()
    sha256_2 = hashlib.sha256(sha256_1).digest()
    checksum = sha256_2[:4]
    private_key_bytes_with_checksum = private_key_bytes_with_prefix + checksum
    wif = base58.b58encode(private_key_bytes_with_checksum)
    return wif.decode()


def get_eth_keys_and_address(master_private_key):
    """Get the private key, public key, and address for Ethereum from a master private key"""

    # derive the first account from the master key
    account_key = master_private_key.subkey_for_path("m/44h/60h/0h")

    # derive the first external key from the account key
    external_key = account_key.subkey_for_path("0/0")

    # get the private key as a hexadecimal string
    private_key_hex = external_key.private_hex

    # get the private key as a hexadecimal string
    eth_private_key = keys.PrivateKey(bytes.fromhex(private_key_hex))

    # Get the public key from the private key
    eth_public_key = eth_private_key.public_key

    # Get the address from the public key
    eth_address = eth_public_key.to_checksum_address()

    return eth_private_key, eth_public_key, eth_address


def public_key_to_bech32_address(public_key_hex):
    public_key_bytes = bytes.fromhex(public_key_hex)
    sha256_hash = hashlib.sha256(public_key_bytes).digest()
    ripemd160_hash = hashlib.new("ripemd160", sha256_hash).digest()
    hrp = "bc"
    witver = 0
    witprog = ripemd160_hash
    addr = bech32.encode(hrp, witver, witprog)
    return addr


def generate_private_key_and_address(master_priv_key, network="BTC"):
    """Generate a private key and address from a master private key"""

    if network == "BTC":
        # derive the first account from the master key
        account_key = master_priv_key.subkey_for_path("m/84h/0h/0h")

        # derive the first external key from the account key
        external_key = account_key.subkey_for_path("0/0")

        # get the private key as a hexadecimalstring
        private_key_hex = external_key.private_hex

        # get the public key as a hexadecimal string
        public_key_hex = external_key.public_hex

        # compute the bc1 address from the public key
        address = public_key_to_bech32_address(public_key_hex)

        return private_key_hex, address

    if network == "TRX":
        # derive the first account from the master key
        account_key = master_priv_key.subkey_for_path("m/44h/195h/0h")

        # derive the first external key from the account key
        external_key = account_key.subkey_for_path("0/0")

        # get the private key as a hexadecimal string
        private_key_hex = external_key.private_hex

        # get the public key as a hexadecimal string
        public_key_hex = external_key.public_hex

        # Convert the private key hex to bytes
        uncompressed_public_key = compressed_to_uncompressed_public_key(
            public_key_hex)  # Remove prefix

        # Convert the uncompressed public key hex to bytes
        public_key_bytes = bytes.fromhex(
            uncompressed_public_key[2:])

        # Compute the Keccak-256 hash of the public key
        keccak_hash = keccak(public_key_bytes)

        # Take the last 20 bytes of the Keccak-256 hash
        address_bytes = keccak_hash[-20:]

        # Add the TRON address prefix (0x41)
        trx_address_bytes = b'\x41'+address_bytes

        # Encode the address bytes using Base58Check
        trx_address = base58.b58encode_check(trx_address_bytes).decode()

        return private_key_hex, trx_address


if __name__ == "__main__":
    # the mnemonic code
    MNEMONICCODE = "abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon abandon about"
    print ('Trust wallet mnemonic:\t', MNEMONICCODE)

    # generate the master private key from the mnemonic code
    master_private_key = get_master_private_key(MNEMONICCODE)
    print("Master private key:\t", master_private_key.private_hex)
    print_symbol_to_end_of_line("*")

    # generate a private key and address for Bitcoin
    private_key, bc1_address = generate_private_key_and_address(
        master_private_key, network="BTC")
    print("BTC Private key:\t", private_key)
    print("BTC WIF:\t\t", private_key_to_wif(private_key))
    print("BTC Address:\t\t", bc1_address)
    print_symbol_to_end_of_line("-")

    # generate a private key and address for Tron
    private_key, TRX_address = generate_private_key_and_address(
        master_private_key, network="TRX")
    print("TRX Private key:\t", private_key)
    print("TRX Address:\t\t", TRX_address)
    print_symbol_to_end_of_line("-")

    # generate a private key and address for Ethereum
    eth_private_key, eth_public_key, eth_address = get_eth_keys_and_address(
        master_private_key)
    print("ETH Private key:\t", eth_private_key)
    print("ETH Public key:\t\t", eth_public_key)
    print("ETH Address:\t\t", eth_address)
    print_symbol_to_end_of_line("-")
