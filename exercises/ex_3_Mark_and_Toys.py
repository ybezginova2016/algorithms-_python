"""
Mark and Jane are very happy after having their first child.
Their son loves toys, so Mark wants to buy some. There are a number
of different toys lying in front of him, tagged with their prices.
Mark has only a certain amount to spend, and he wants to maximize
the number of toys he buys with this money. Given a list of toy
prices and an amount to spend, determine the maximum number
of gifts he can buy.

Note Each toy can be purchased only once.

Example
The budget is  units of currency. He can buy items that cost [1, 2, 3] for 6,
or [3, 4] for 7 units. The maximum is 3 items.

Function Description

Complete the function maximumToys in the editor below.

maximumToys has the following parameter(s):

int prices[n]: the toy prices
int k: Mark's budget

"""
def maximumToys(prices, k):
    prices.sort()  # sort the prices in ascending order
    num_toys = 0
    for price in prices:
        if price <= k:
            k -= price  # subtract the price of the toy from the budget
            num_toys += 1
        else:
            break  # if the toy is too expensive, stop buying toys
    return num_toys

prices = [390, 290, 99, 790]
budget = 1500

print(maximumToys(prices, budget))

"""
The function takes in a list of toy prices and the budget as inputs. 
First, we sort the toy prices in ascending order so that we can buy 
the cheapest toys first. We initialize the number of toys to 0 and 
loop through each toy price. If the price of the toy is less than 
or equal to the budget, we subtract the price of the toy from the 
budget and increment the number of toys. If the price of the toy is 
greater than the budget, we break out of the loop since we can't buy 
any more toys. Finally, we return the number of toys that were bought.
"""

# To keep track of which toys were bought, you can store the prices of the bought toys in a separate list.
def maximumToys2(prices, k):
    prices.sort()
    num_toys = 0
    bought_toys = []
    for price in prices:
        if price <= k:
            k -= price
            num_toys += 1
            bought_toys.append(price)

        else:
            break
    return num_toys, bought_toys

num_toys, bought_toys = maximumToys2(prices, budget)
print("Number of toys bought:", num_toys)
print("Prices of the bought toys:", bought_toys)
