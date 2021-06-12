# deployment example from https://web3py.readthedocs.io/en/stable/contracts.html

import json

from web3 import Web3
from inline_contract import compiled_sol

# see the object 
# print(compiled_sol)
# print(compiled_sol['contracts']['Greeter'].keys())
w3 = Web3(Web3.EthereumTesterProvider())

w3.eth.default_account = w3.eth.accounts[0]

bytecode = compiled_sol['contracts']['Greeter.sol']['Greeter']['evm']['bytecode']['object']

abi = json.loads(compiled_sol['contracts']['Greeter.sol']['Greeter']['metadata'])['output']['abi']

# THIS IS WHERE THE MAGIC HAPPENS --> create the smart contract object
Greeter = w3.eth.contract(abi=abi, bytecode=bytecode)

w3.eth.contract(abi=abi, bytecode=bytecode)

tx_hash = Greeter.constructor().transact()

tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)

greeter = w3.eth.contract(
    address = tx_receipt.contractAddress,
    abi=abi
)

# no need to write information
print(greeter.functions.greet().call())

tx_hash = greeter.functions.setGreeting('Ey!').transact()
tx_receipt = w3.eth.wait_for_transaction_receipt(tx_hash)
greet = greeter.functions.greet().call()
print(greet)