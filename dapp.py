import configparser
from web3 import Web3

parser = configparser.ConfigParser()
parser.read('config.conf')
# our alchemy app url: https://dashboard.alchemyapi.io/apps/xbzqp9yd7xzb0zcl
alchemy_url = parser.get('alchemy', 'alchemy_app_url')
metamask_key = parser.get('metamask', 'private_key')

# create a client object that we can use to connect to our alchemy-hosted ropsten test net
web3 = Web3(Web3.HTTPProvider(alchemy_url)) # --> connects this app to a web3 provider

# see if we're connected:
print(web3.isConnected())

# see the latest block number:
print(web3.eth.blockNumber)

# check balance for 