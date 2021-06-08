name = "Super Happy Friendly Vending Machine"

product = "Neru Neru Neru ne"

products = ["Coffee","Tea","Ginger Ale","Orange Juice"]

prices = [130,140,150,160]

stocks = [100,50,30,70]

inventory = 100

money = 20000

cost = 200

def greet_customer():
    print("Welcome to " + name + "\n")

def show_products():
    for x in products:
        print(x,end = "\t")
        
def show_prices():
    for x in prices:
        print(xend = "\t")

def show_selection_number():
    for x in range(len(products)):
        print(x+1,end = "\t")
        
        

greet_customer()

show_products()

print("\n")
show_prices()

print("\n")

show_selection_number()

print("\n")


customer_money = input("Please enter some money \n")

if customer_money.isdigit():
    customer_money = int(customer_money)
    customer_product = input("Please enter product number")
    if customer_product.isdigit():
        cusomer_product = int(costomer_product)
        if customer_product > 0 and \
           customer_product <= len(products):
    #check the cost and inventory
     if customer_money >= prices[customer_product-1]:
        stocks[customer_product-1] -= 1
        change = custmer_money - \
                 prices[customer_product-1]
        money += prices[customer_product-1]

    print("Your change is " + str(change))
    print("We have" + \
          str(stocks[customer_product-1]) \
          +products[customer_product-1]
        print("Thank you")
    else:
        fix this!!!
        print("Not enough money")



#money = money + customer_money

#print(customer_money)
#print(type(customer_money))



