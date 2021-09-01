from web3 import Web3
#We gotta download ganashe, to obtain that RPC address. Just for the simulation, and we dont have to use a real account with ETH..
ganache_url = "http://127.0.0.1:7545"
web3 = Web3(Web3.HTTPProvider(ganache_url)) 
#print(web3.isconnected()) -> true ; and we´ll also do print(web3.eth.blockNumber) -> at the beggiining it´ll give us 0 cuz we haven´t started our blockchain.
#Copy the variables from ganache(private keys, accounts...)
account_1 = '' # Fill me in
account_2 = '' # Fill me in
private_key = '' # Fill me in
#we r gonna send us cryptocurrency to our account 1. So we r gonna build, sign, send, get hash.
nonce = web3.eth.getTransactionCount(account_1)
#first we r gonna build the dictionary, that contains all the transaction info
tx = {
    'nonce': nonce, 
    'to': account_2,
    'value': web3.toWei(1, 'ether'),
    'gas': 2000000, #This will be the top limit
    'gasPrice': web3.toWei('50', 'gwei'),
}
#we r gonnna sign it
signed_tx = web3.eth.account.signTransaction(tx, private_key)
#we r gonna send the transaction
tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction) # -> print(tx_hash) -> it worked

print(web3.toHex(tx_hash)) # -> it gives us the transaction hash ofc. And u can take a look with ganashe
