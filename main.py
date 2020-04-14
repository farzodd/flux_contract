from contract import Contract

def CreateContract(ContractName, PartyA, PartyB, ContractText, Ownership, PaymentTerms, ContractValue, DeliveryDate, ExpiryDate):
    return Contract(ContractName, PartyA, PartyB, ContractText, Ownership, PaymentTerms, ContractValue, DeliveryDate, ExpiryDate)
