import os
from bitcoin import *


def generate_keypair():
    private_key = os.urandom(32).hex()
    wif_key = encode_privkey(private_key, "wif_compressed")
    public_key = privtopub(private_key)
    compressed_pub = compress(public_key)
    uncompressed_address = pubtoaddr(public_key)
    compressed_address = pubtoaddr(compressed_pub)
    uncompressed_p2pk_address = pubkey_to_address(public_key)
    compressed_p2pk_address = pubkey_to_address(compressed_pub)
    return (
        private_key,
        wif_key,
        public_key,
        compressed_pub,
        uncompressed_address,
        compressed_address,
        uncompressed_p2pk_address,
        compressed_p2pk_address,
    )


def m_of_n_multisig_wallet():
    m = int(input("Enter the number 'm' for the m-of-n multisig: "))
    n = int(input("Enter the number 'n' for the m-of-n multisig: "))

    if m > n:
        raise ValueError("'m' should be less than or equal to 'n'")

    keys_data = [generate_keypair() for _ in range(n)]
    public_keys = [data[2] for data in keys_data]

    # Create a multisig P2SH address using the `mk_multisig_script` function
    multisig_script = mk_multisig_script(public_keys, m, n)
    address = scriptaddr(multisig_script)

    print("\nGenerated Keys:")
    for i, (
        priv,
        wif,
        pub,
        compressed_pub,
        uncompressed_addr,
        compressed_addr,
        uncompressed_p2pk_addr,
        compressed_p2pk_addr,
    ) in enumerate(keys_data, 1):
        print(f"\nKeypair {i}:")
        print(f"Private Key (HEX): {priv}")
        print(f"Private Key (WIF): {wif}")
        print(f"Public Key: {pub}")
        print(f"Compressed Public Key: {compressed_pub}")
        print(f"Bitcoin Address (Uncompressed): {uncompressed_addr}")
        print(f"Bitcoin Address (Compressed): {compressed_addr}")
        print(f"Bitcoin P2PK Address (Uncompressed): {uncompressed_p2pk_addr}")
        print(f"Bitcoin P2PK Address (Compressed): {compressed_p2pk_addr}")

    print(f"\nYour {m} of {n} multisig P2SH address is: {address}")


if __name__ == "__main__":
    m_of_n_multisig_wallet()

# P2PKH = The hash160 of a compressed public key.
# P2PK = A compressed public key (even if the original script contained an uncompressed public key). A compressed public key always starts with a 02 or 03 to indicate whether the y value is even or odd. However, if the original script contained an uncompressed public key, it gets compressed when storing it in the chainstate database to save space. We then use an 04 or 05 to indicate that it was originally an uncompressed key and to also indicate whether the original y was even or odd.
# P2SH = The hash160 of a script.
# Everything else = The full scriptpubkey.
# P2WPKH = Always starts with a 0014, followed by the hash160 of a public key.
# P2WSH = Always starts with a 0020, followed by the sha256 hash of a script.
# 00  = P2PKH <- upcoming data is the hash160 public key
# 01  = P2SH  <- upcoming data is the hash160 of a script
# 02  = P2PK  <- upcoming data is a compressed public key (nsize makes up part of the public key) [y=even]
# 03  = P2PK  <- upcoming data is a compressed public key (nsize makes up part of the public key) [y=odd]
# 04  = P2PK  <- upcoming data is an uncompressed public key (but has been compressed for leveldb) [y=even]
# 05  = P2PK  <- upcoming data is an uncompressed public key (but has been compressed for leveldb) [y=odd]
# 06+ =       <- indicates size of upcoming full script (subtract 6 to get the actual size in bytes)