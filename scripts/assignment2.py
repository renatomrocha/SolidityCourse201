from brownie import ArrayStorage, MappingStorage, accounts

account = accounts[0]
account1 = accounts[1]
account2 = accounts[2]
account3 = accounts[3]
account4 = accounts[4]
account5 = accounts[5]


def deploy_array_storage():
    return ArrayStorage.deploy({"from": account})

def deploy_mapping_storage():
    return MappingStorage.deploy({"from": account})


def get_gas_for_add_entity(storage, _account):
    tx = storage.addEntity(10,{"from": _account})
    return tx.gas_used


def get_gas_on_edit(storage, _account):

    first_add_gas = get_gas_for_add_entity(storage,_account)
    for i in range(8):
        get_gas_for_add_entity(storage,accounts[i + 1])

    edit_tx = storage.updateEntity(i,{"from": accounts[i+1]})


    return (first_add_gas, edit_tx.gas_used)


def main():
    array_storage = deploy_array_storage()
    mapping_storage = deploy_mapping_storage()

    mapping_create_gas, mapping_edit_gas = get_gas_on_edit(mapping_storage, account)

    array_create_gas, array_edit_gas = get_gas_on_edit(array_storage, account)
    
    print(f"Mapping spent {mapping_create_gas} to create an entity and {mapping_edit_gas} to edit the last element")

    print(f"Array spent {array_create_gas} to create an entity and {array_edit_gas} to edit the last element")
