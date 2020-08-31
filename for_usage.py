foods=['apples','bananas','cherries','donuts']
amounts=[11,22,33,44]
preference=[True,False,False,True]
"""
for i,food in enumerate(foods):
    print('{} - {}'.format(amounts[i],food))
    
for amount, food, like in zip(amounts,foods,preference):
    print('{} - {} - {}'.format(amount,food,like))

"""
def find_amounts(fruit_name):
    #found_index=foods.index(fruit_name)
    isValid=False
    for food,amount in zip(foods,amounts):
        if food==fruit_name:
            isValid=True
            print('{}:{}'.format(food,amount))
            break
        pass
    if isValid==False:
        print('Sorry, your {} is not available'.format(fruit_name))
        pass

if __name__=='__main__':
    find_amounts('bananas')
    find_amounts('pizza')
    pass


