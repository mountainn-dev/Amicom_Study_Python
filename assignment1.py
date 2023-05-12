
def deposit(asset,money):
    pocket = asset[0]
    balance = asset[1]
    pocket -= money
    balance += money
    return [pocket,balance]
def withdraw(asset,money):
    pocket = asset[0]
    balance = asset[1]
    pocket += money
    balance -= money
    return [pocket,balance]

pocket = 20000    #수중 잔액
balance = 10000   #계좌 잔액
asset_info = [pocket,balance]

asset_info = deposit(asset_info,10000)
asset_info = withdraw(asset_info,5000)