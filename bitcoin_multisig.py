import os
from bitcoin import *


def generate_keypair():
    private_key = os.urandom(32).hex()
    public_key = privtopub(private_key)
    return private_key, public_key


def m_of_n_multisig_wallet():
    m = int(input("Enter the number 'm' for the m-of-n multisig: "))
    n = int(input("Enter the number 'n' for the m-of-n multisig: "))

    if m > n:
        raise ValueError("'m' should be less than or equal to 'n'")

    public_keys = []

    for _ in range(n):
        _, pub_key = generate_keypair()
        public_keys.append(pub_key)

    # Create a multisig P2SH address using the `mk_multisig_script` function
    multisig_script = mk_multisig_script(public_keys, m, n)
    address = scriptaddr(multisig_script)

    print(f"\nYour {m} of {n} multisig P2SH address is: {address}")


if __name__ == "__main__":
    m_of_n_multisig_wallet()
