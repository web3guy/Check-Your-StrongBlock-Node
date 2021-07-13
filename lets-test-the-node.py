from web3 import Web3

#Replace your NODE URL BELOW
my_node_url = "https://mainnet.strongblock.com/1c6212813d5aacb0805051b3ca125badd878845e"


#Don't thouch this one

w3 = Web3(Web3.HTTPProvider(my_node_url))
print(w3.isConnected())

