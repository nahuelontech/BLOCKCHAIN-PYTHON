
from web3 import Web3

# Fill in your infura API key here
infura_url = "https://mainnet.infura.io/v3/YOUR_INFURA_API_KEY_GOES_HERE"
web3 = Web3(Web3.HTTPProvider(infura_url))
#Now we can see if its connected. And we r gonna see with this, so we have to talk to the eth:
print(web3.isConnected())         #-> True 
#Now we can further verify this. What we´re gonna do is just get the latest block on ETH
print(web3.eth.blockNumber)       #-> 7447429(the last block at that moment)
# Fill in your account here
balance = web3.eth.getBalance("YOUR_ACCOUNT_GOES_HERE") #and if we put balance it´ll give us what we have.
print(web3.fromWei(balance, "ether")) #Instead of giving our eth in wei, it´ll print the eth we have like 2´94


