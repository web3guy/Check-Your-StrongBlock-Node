from web3 import Web3

#Replace your NODE URL BELOW
my_node_url = "https://mainnet.strongblock.com/1c6212813d5aacb0805051b3ca125badd878845e"


w3 = Web3(Web3.HTTPProvider(my_node_url))
print(w3.isConnected())

#Hurray! If everything went right, you will get 'True'  when you run this file.