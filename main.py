from contract import Contract

list_of_contracts = []

def return_contract_info(name):
    #this receives a name that is guarenteed to belong to an existing contract
    for contract in list_of_contracts:
        if contract.name == name:
            return contract
    return "contract doesn't exist"

def seach_contract(search_paramater):
    #this takes in a parameter, and if it matches any contract paramater, return the contract

    for contract in list_of_contracts:
        if search_paramater in [contract.ContractName, contract.PartyA, contract.PartyB,
                                contract.ContractText, contract.Ownership, contract.PaymentTerms,
                                contract.ContractValue, contract.DeliveryDate, self.ExpiryDate]:
            return contract
        if search_paramater in contract.ContractText:
            return contract



def CreateContract(ContractName, PartyA, PartyB, ContractText, Ownership, PaymentTerms, ContractValue, DeliveryDate, ExpiryDate):
    list_of_contracts.append(Contract(ContractName, PartyA, PartyB, ContractText, Ownership, PaymentTerms, ContractValue, DeliveryDate, ExpiryDate))
