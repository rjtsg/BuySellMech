#Python 3 file
import matplotlib.pyplot as plt

class Seller(object):
    def __init__(self,min_val):
        self.min_value = min_val #minimum value for which he sells
        self.like_sell = self.min_value #Value he is currently selling at
        self.has_sold = False #Indication if he sold something last round

class Buyer(object):
    def __init__(self,max_val):
        self.max_value = max_val #maximum value for which he buys
        self.like_buy  = self.max_value #Value that he is currently buying at
        self.has_bought = False #Indication if he bought something last round

def Trading(Seller,Buyer):
    """
    This function handels the trading. The seller sells if the price is at or
    above his like_sell value. The buyer buys if the price is at or lower than 
    his like_buy value.
    """
    if  Buyer.like_buy >= Seller.like_sell:
        Seller.has_sold = True
        Buyer.has_bought  = True
        print('A trade has been made')
    else:
        Buyer.has_bought = False
        Seller.has_sold  = False
        print('There was no deal')


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

#The main programm is a while loop, which runs for x number of steps.
#Before that we need to create the buyer and seller.

Buy = Buyer(40)
Sell = Seller(20)
steps = 100
current_step = 0
sell_price_list = []
buy_price_list = []
trade_list = []

while current_step < steps:
    Trading(Sell,Buy)
    ReflectingBuyer(Buy)
    ReflectingSeller(Sell)
    sell_price_list.append(Sell.like_sell)
    buy_price_list.append(Buy.like_buy)
    current_step += 1

plt.plot(sell_price_list)
plt.plot(buy_price_list)
plt.title('Like prices')
plt.legend(['Like sell','Like buy'])
plt.show()