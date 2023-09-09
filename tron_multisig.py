from tronapi import Tron

# Initialize Tron connection
tron = Tron()

# Set your private key (be careful with this!)
tron.private_key = 'YOUR_PRIVATE_KEY'
tron.default_address = 'YOUR_PUBLIC_ADDRESS'

# Contract details
CONTRACT_ADDRESS = 'DEPLOYED_CONTRACT_ADDRESS'
ABI = [...]  # Use the ABI from your compiled contract

# Initialize contract
contract = tron.contract(abi=ABI, contract_address=CONTRACT_ADDRESS)

# If you want to submit a transaction
# The parameters would be the destination address, value, and any additional data.
transaction = contract.submitTransaction('DESTINATION_ADDRESS', 100, '0x0').sign().broadcast()

# If you want to confirm a transaction
transaction_index = 0  # Replace with your transaction index
transaction = contract.confirmTransaction(transaction_index).sign().broadcast()

# If you want to check if an address is an owner
is_owner = contract.isOwner('CHECK_ADDRESS').call()

print(is_owner)
