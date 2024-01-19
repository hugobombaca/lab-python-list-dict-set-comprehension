products = ["t-shirt", "mug", "hat", "book", "keychain"]
inventory = {}
customer_orders = set()
def initialize_inventory(products): 
        inventory={product:int(input(f"Enter the quantity of {product}s available: "))for product in products}
        return inventory

def get_customer_orders():
    num_orders = int(input("Number of orders?"))
    prdname = [input(f"Enter product name #{y+1} from the list {products}: ") for y in range(num_orders)]
    {customer_orders.add(x) for x in prdname if x in products}
    return customer_orders

def update_invetory(getorder, invup): 
    for orderedprd in getorder:
        if orderedprd in invup:
            invup[orderedprd] -= 1
            inventory = {product : item for (product,item) in invup.items() if item !=0}
    return inventory
1
def calculate_order_statistics(getorder,products):
    TPO = len(getorder)
    PPO = (TPO/len(products))*100
    order_status = (PPO,TPO)
    print(f"Total Products Ordered: {order_status[1]}")
    print(f"Percentage of Products Ordered: {order_status[0]}%")

def print_inventory(update):
    for product, x in update.items():
        print(f"{product} : {x}") 

def calculate_price(getorder):
    length= len(getorder)
    pricing = [float(input(f"Enter price for item #{item+1}: ")) for item in range(length)]
    prices = sum(pricing)
    return prices

invup = initialize_inventory(products)
getorder= get_customer_orders()
update = update_invetory(getorder,invup)
calculate_order_statistics(getorder,products)
print_inventory(update)
calculate_price(getorder)
