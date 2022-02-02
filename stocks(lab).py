#CS175-50
#Noah Ferker
#stocks

#Inputs
COMMISSION_RATE = float(input('What was the commision rate?: '))
NUM_SHARES = int(input('How many shares did you purchase?: '))
PURCHASE_PRICE = float(input('What was the purchase price?: '))
SELLING_PRICE = float(input('What was the selling price?: '))
#Variables
amountPaidForStock = NUM_SHARES * PURCHASE_PRICE
purchaseCommission = COMMISSION_RATE * amountPaidForStock
totalPaid = amountPaidForStock + purchaseCommission
stockSoldFor = NUM_SHARES * SELLING_PRICE
sellingCommission = COMMISSION_RATE * stockSoldFor
totalReceived = stockSoldFor - sellingCommission
profitOrLoss = totalReceived - totalPaid
#Display
print("Amount paid for stock: ","$", amountPaidForStock)
print("Commission paid on the purchase: ","$", purchaseCommission)
print("Amount the stock sold for: ", "$", stockSoldFor)
print("Commission paid on the sale: ", "$", sellingCommission)
print("Profit (or loss if negative): ", "$", profitOrLoss)
