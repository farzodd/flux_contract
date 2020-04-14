from contract import Contract

list_of_contracts = []

search_contract("ContractName")

def seach_contract(search_paramater):

    for contract in list_of_contracts:
        if search_paramater in [contract.ContractName, contract.PartyA, contract.PartyB,
                                contract.ContractText, contract.Ownership, contract.PaymentTerms,
                                contract.ContractValue, contract.DeliveryDate, self.ExpiryDate]:
            return contract



def CreateContract(ContractName, PartyA, PartyB, ContractText, Ownership, PaymentTerms, ContractValue, DeliveryDate, ExpiryDate):
    return Contract(ContractName, PartyA, PartyB, ContractText, Ownership, PaymentTerms, ContractValue, DeliveryDate, ExpiryDate)
