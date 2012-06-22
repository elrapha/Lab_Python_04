"""
The Shoprite CEO has decided that he wants to advertise a list of all the foods that his store
sells. He asks the computer scientists at his company to do this for him.
"""
#a
#lists

#b
item={'Apples':7.30,'Bananas':5.50,'Bread':1.00,'Carrots':10.00,'Champagne':20.90,'Strawberries':32.60}
item['Chicken']=6.50
#print item
in_stock=[]
for key in item.keys():
    in_stock.append(key)
#print in_stock

#c Tuples
always_in_stock=tuple(in_stock)
#print  always_in_stock

#d
print 'Come to shoprite! We always sell: '
for item in always_in_stock:
    print item














