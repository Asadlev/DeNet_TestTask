from django.shortcuts import render
from web3 import Web3
import json
from django.http import JsonResponse


# Подключаю к сети, но у меня нет аккаунта в polygon
infura_url = "https://polygon-mainnet.infura.io/v3/Ваш-ID"
web3 = Web3(Web3.HTTPProvider(infura_url))

# Адрес контракта ERC20 токена
token_address = "0x1a9b54a3075119f1546c52ca0940551a6ce5d2d0"
# Преобразование адреса в формат checksum
token_address = Web3.to_checksum_address(token_address)

# ABI для ERC20 токена
abi = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "decimals",
        "outputs": [{"name": "", "type": "uint8"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "symbol",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "name",
        "outputs": [{"name": "", "type": "string"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    },
    {
        "constant": True,
        "inputs": [],
        "name": "totalSupply",
        "outputs": [{"name": "totalSupply", "type": "uint256"}],
        "payable": False,
        "stateMutability": "view",
        "type": "function"
    }
]

contract = web3.eth.contract(address=token_address, abi=abi)

def get_balance(request):
    address = request.GET.get('address')
    balance = contract.functions.balanceOf(address).call()
    decimals = contract.functions.decimals().call()
    return JsonResponse({'balance': balance / 10 ** decimals})

def get_balance_batch(request):
    addresses = json.loads(request.body).get('addresses')
    balances = []
    decimals = contract.functions.decimals().call()
    for address in addresses:
        balance = contract.functions.balanceOf(address).call()
        balances.append(balance / 10 ** decimals)
    return JsonResponse({'balances': balances})

def get_top(request):
    n = int(request.GET.get('n'))
    # Здесь должна быть логика для получения топ N адресов по балансам токена
    # ...
    return JsonResponse({'top_addresses': []})

def get_top_with_transactions(request):
    n = int(request.GET.get('n'))
    # Здесь должна быть логика для получения топ N адресов по балансам токена с датами последних транзакций
    # ...
    return JsonResponse({'top_addresses_with_transactions': []})

def get_token_info(request):
    symbol = contract.functions.symbol().call()
    name = contract.functions.name().call()
    total_supply = contract.functions.totalSupply().call()
    decimals = contract.functions.decimals().call()
    return JsonResponse({
        'symbol': symbol,
        'name': name,
        'totalSupply': total_supply / 10 ** decimals
    })