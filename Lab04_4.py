#a
"""
The data structure that could be used is a dictionary
"""
#b
def binary_insert(new_float,some_list_of_floats):
    lower=0
    upper=len(some_list_of_floats)
    mid=(lower+upper)/2
    count=0
    if new_float<=some_list_of_floats[lower]:
        return lower    
    elif new_float >= some_list_of_floats[upper-1]:
        return upper
    else:
       # print upper
       # print lower
        while mid!=lower:
            #print upper
            #print lower
            if new_float>some_list_of_floats[mid]:
                lower=mid
                mid=(lower+upper)/2
            elif new_float<some_list_of_floats[mid]:
                upper=mid
                mid=(lower+upper)/2
            elif new_float==some_list_of_floats[mid]:
                return mid
    return mid+1
    
pricelist=[0.0,0.10,0.20,0.30,0.50,1.25,1.50,2.0]
invalue=2.0
inloc=binary_insert(invalue,pricelist)
print pricelist
print 'inserting ',invalue
pricelist.insert(inloc,invalue)
print pricelist
print '\n'

#c
print 
def min_cost(groc_lst,groc_price_lst):
#grocery_list is a list of strings (item names)
#item_to_price_list_dict is a dictionary with key-value
# pairs as follows: the item name (strings) is the key
# and the list of prices (floats) at different grocery is
# the value
    mincost=0
    result=[]
    for item in groc_lst:
        groc_price_lst[item].sort()
        mincost=mincost+ groc_price_lst[item][0]
        print 'minimum cost for '+ item +' is ', groc_price_lst[item][0]
    return mincost

groc_lst= ['bananas','strawberries','apples','bread']
groc_price_lst= {'bananas':[3.5,8.8,4.4],'strawberries':[0.30,0.20,0.50],'apples':[1.25,1.50,0.50,2.0],'bread':[5.0,8.0,3.0]}

mincost=min_cost(groc_lst,groc_price_lst)
print
print 'Total minimum cost is ', mincost
  
