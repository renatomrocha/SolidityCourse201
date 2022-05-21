from brownie import accounts, Bank, SafeBank, Attacker


account = accounts[0]


def main():

    bank = SafeBank.deploy({"from": account})

    attacker = Attacker.deploy(bank.address, {"from": account})

    amount_to_deposit = 1000000000000000000
    amount_from_attacker = amount_to_deposit / 2


    print(f"Bank initial balance {bank.balance()}")

    # Deposit some funds in bank
    bank.deposit({"from": account, "value": amount_to_deposit})

    print(f"Bank balance after deposit {bank.balance()}")
    print(f"Account balance after deposit {bank.balances(account.address)}")

    # Call start function from attacker
    attacker.start({"from": account, "value": amount_from_attacker})

    print(f"Bank balance after attack {bank.balance()}")


    # Assert bank funds are the same, withdraw function never executed due to reentrancy
    assert(bank.balance() == amount_to_deposit + amount_from_attacker)
    # Assert attacker funds are still deposited
    assert(bank.balances(attacker.address) == amount_from_attacker)
    