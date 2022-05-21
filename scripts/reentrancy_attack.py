from brownie import accounts, Bank, Attacker


account = accounts[0]


def main():

    bank = Bank.deploy({"from": account})

    attacker = Attacker.deploy(bank.address, {"from": account})

    amount_to_deposit = 1000000000000000000
    amount_from_attacker = amount_to_deposit / 2


    print(f"Bank initial balance {bank.balance()}")

    # Deposit some funds in bank
    bank.deposit({"from": account, "value": amount_to_deposit})

    print(f"Bank balance after deposit {bank.balance()}")

    # Call start function from attacker
    attacker.start({"from": account, "value": amount_from_attacker})

    print(f"Bank balance after attack {bank.balance()}")


    # Assert bank funds go to zero
    assert(bank.balance() == 0)
    assert(attacker.balance() == amount_to_deposit + amount_from_attacker)