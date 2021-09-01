import json
from web3 import Web3

# Set up web3 connection with Ganache, if u don´t it´ll give us an error
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url))

# TODO: Deploy the Greeter contract to Ganache with remix.ethereum.org
#In summary we will create a SC with remix, and it will appear in ourblockchain simulator(ganashe), we can do that with WEB3 provider insted of injected, and will directly appear in ganashe(connect to your local host, u have to write the local host   address that ganashe gives u


# Set a default account to sign transactions - this account is unlocked with Ganache
#Look at this(1). with 0 it´ll get the first account in ganashe
web3.eth.defaultAccount = web3.eth.accounts[0]
# Greeter contract ABI. Abi is just a JSON array that describes how the SC works. So we are gonna copy it from the SC details in remix. It´s public u can also see it en bscscan with public contracts
abi = json.loads('[{"constant":false,"inputs":[{"name":"_greeting","type":"string"}],"name":"setGreeting","outputs":[],"payable":false,"stateMutability":"nonpayable","type":"function"},{"constant":true,"inputs":[],"name":"greet","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"greeting","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"inputs":[],"payable":false,"stateMutability":"nonpayable","type":"constructor"}]')
# Greeter contract address - convert to checksum address. To have to do this in order to format the address. 
address = web3.toChecksumAddress('') # FILL ME IN
# Initialize contract.#Not we are gonna extensionate the contract like this
contract = web3.eth.contract(address=address, abi=abi)
# Read the default greeting.#We can call greet print-> Hello(READ THE SC TO see this is true. min 40)
print(contract.functions.greet().call())
# Set a new greeting. We wanna write data on the SC, wer gonna update the ``greeting´´ contract that we saw in remix. 
#As u can see we are calling a function from the greeting SC, and we put different message. 
#Look at (1)We need to tell it which account we are gonna be sending this from. 
tx_hash = contract.functions.setGreeting('HEELLLLOOOOOO!!!').transact() #print(tx_hash) ->it will give us Hello and the tx hash

# Wait for transaction to be mined. U wanna get a receipt back, ok the tx was succesful
web3.eth.waitForTransactionReceipt(tx_hash)
# Display the new greeting value
print('Updated contract greeting: {}'.format(   #-> It will upgrade the SC from remix and say 'HEELLLLOOOOOO!!!
    contract.functions.greet().call()
))
