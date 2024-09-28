# 2. You are given following list of stocks and their prices in last 3 days,

#     |Stock|Prices|
#     |-------|----------|
#     |info|[600,630,620]|
#     |ril|[1430,1490,1567]|
#     |mtl|[234,180,160]|

#     1. Write a program that asks user for operation. Value of operations could be,
#         1. print: When user enters print it should print following,
#             ```
#             info ==> [600, 630, 620] ==> avg:  616.67
#             ril ==> [1430, 1490, 1567] ==> avg:  1495.67
#             mtl ==> [234, 180, 160] ==> avg:  191.33
#             ```
#         2. add: When user enters 'add', it asks for stock ticker and price. If stock already exist in your list (like info, ril etc) then it will append the price to the list. Otherwise it will create new entry in your dictionary. For example entering 'tata' and 560 will add tata ==> [560] to the dictionary of stocks.


stock_prices  = {
    'info': [600,630,620],
    'ril': [1430,1490,1567],
    'mtl' :[234, 180, 160]
}

def print_stock_prices():
    for stock, prices in stock_prices.items():
        print(f'{stock} ==> {prices} ==> avg: {sum(prices)/len(prices):.2f}')
        
def add_stock_price():
    stock_ticker = input('Enter stock ticker: ')
    price = float(input('Enter price: '))
    
    if stock_ticker in stock_prices:
        stock_prices[stock_ticker].append(price)
    else:
        stock_prices[stock_ticker] = [price]
        print_stock_prices()
        return stock_prices
        
def operation():
    
    op = input("enter operation(print or add )")
    if op == "print":
        print_stock_prices()
    else:
        add_stock_price()


if __name__ == '__main__':
    operation()