#Python 3 file
import matplotlib.pyplot as plt
import random

class Seller(object):
    def __init__(self,min_val):
        self.min_value = min_val #minimum value for which he sells
        self.like_sell = self.min_value #Value he is currently selling at
        self.has_sold = False #Indication if he sold something last round
        self.sold_objects = 0

class Buyer(object):
    def __init__(self,max_val):
        self.max_value = max_val #maximum value for which he buys 
        self.like_buy  = self.max_value #Value that he is currently buying at
        self.has_bought = False #Indication if he bought something last round
        self.bought_objects = 0

def Trading(Seller,Buyer):
    """
    This function handels the trading. The seller sells if the price is at or
    above his like_sell value. The buyer buys if the price is at or lower than 
    his like_buy value.
    """
    if Seller.has_sold == False:
        if  Buyer.like_buy >= Seller.like_sell:
            Seller.has_sold = True
            Buyer.has_bought  = True
            Seller.sold_objects += 1
            Buyer.bought_objects += 1
            print('A trade has been made')
        else:
            Buyer.has_bought = False
            Seller.has_sold  = False
            print('There was no deal')
    else:
        Buyer.has_bought = False


def ReflectingBuyer(Buyer):
    """
    If the buyer sells his product he tries to ask more the
    following day, if he does not sell he lowers his price. This works vice versa
    for the buyer: if he buys the next day he wants to pay less, if he is not 
    able to buy he wants to pay more the next day. This stopss when the limits
    are reached.  
    """
    increase_step = 0.01

    if Buyer.has_bought == True:
        Buyer.like_buy *= (1-increase_step)
    elif Buyer.like_buy * (1+increase_step) >= Buyer.max_value and Buyer.has_bought == False:
        Buyer.like_buy = Buyer.max_value
    else:
        Buyer.like_buy *= (1+increase_step)
    Buyer.has_bought = False #return to normal state

def ReflectingSeller(Seller):
    """
    If the buyer sells his product he tries to ask more the
    following day, if he does not sell he lowers his price. This works vice versa
    for the buyer: if he buys the next day he wants to pay less, if he is not 
    able to buy he wants to pay more the next day. This stopss when the limits
    are reached.  
    """
    increase_step = 0.01

    if Seller.has_sold == True:
        Seller.like_sell *= (1+increase_step)
    elif Seller.like_sell * (1-increase_step) <= Seller.min_value and Seller.has_sold == False:
        Seller.like_sell = Seller.min_value
    else: 
        Seller.like_sell *= (1-increase_step)
    Seller.has_sold = False #return to normal state

#The main programm is a while loop, which runs for x number of steps.
#Before that we need to create the buyer and seller.

Buy1 = Buyer(40)
# Buy2 = Buyer(35)
Sell1 = Seller(20)
Sell2 = Seller(35)
Buyers_list = [Buy1]
Sellers_list = [Sell1,Sell2]
steps = 1000
current_step = 0
sell_price_list1 = []
sell_price_list2 = []
buy_price_list1 = []
buy_price_list2 = []


while current_step < steps:
    random_buyers = random.sample(Buyers_list,len(Buyers_list))
    random_sellers = random.sample(Sellers_list,len(Sellers_list))
    for i in random_buyers:
        for j in random_sellers:
            Trading(j,i)
    for i in Buyers_list:
        ReflectingBuyer(i)
    for i in Sellers_list:
        ReflectingSeller(i)
    sell_price_list1.append(Sell1.like_sell)
    sell_price_list2.append(Sell2.like_sell)
    buy_price_list1.append(Buy1.like_buy)
    # buy_price_list2.append(Buy2.like_buy)
    current_step += 1

plt.plot(sell_price_list1)
plt.plot(sell_price_list2)
plt.plot(buy_price_list1)
# plt.plot(buy_price_list2)
plt.title('Like prices')
plt.legend(['Like sell1','Like sell2','Like buy1'])
plt.show()

# print('Seller sold {} objects, buyer 1 bought {} objects and buyer 2 bought {} objects' \
#     .format(Sell.sold_objects, Buy1.bought_objects, Buy2.bought_objects))