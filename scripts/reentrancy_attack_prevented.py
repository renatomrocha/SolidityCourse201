from brownie import accounts, UnsafeBank, SafeUnsafeBank, Attacker


account = accounts[0]


def main():

    UnsafeBank = SafeUnsafeBank.deploy({"from": account})

    attacker = Attacker.deploy(UnsafeBank.address, {"from": account})

    amount_to_deposit = 1000000000000000000
    amount_from_attacker = amount_to_deposit / 2


    print(f"UnsafeBank initial balance {UnsafeBank.balance()}")

    # Deposit some funds in UnsafeBank
    UnsafeBank.deposit({"from": account, "value": amount_to_deposit})

    print(f"UnsafeBank balance after deposit {UnsafeBank.balance()}")
    print(f"Account balance after deposit {UnsafeBank.balances(account.address)}")

    # Call start function from attacker
    attacker.start({"from": account, "value": amount_from_attacker})

    print(f"UnsafeBank balance after attack {UnsafeBank.balance()}")


    # Assert UnsafeBank funds are the same, withdraw function never executed due to reentrancy
    assert(UnsafeBank.balance() == amount_to_deposit + amount_from_attacker)
    # Assert attacker funds are still deposited
    assert(UnsafeBank.balances(attacker.address) == amount_from_attacker)
    