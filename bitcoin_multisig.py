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
