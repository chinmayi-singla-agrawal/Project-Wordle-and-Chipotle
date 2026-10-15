# Author   : Chinmayi Singla Agrawal
# Email    : csinglaagraw@umass.edu
# Spire ID : 35726631

order1 = ('manan', 'holyoke', 'FLAT3', 'chicken', 'white', 'pinto', False, 'queso blanco', 'cheese', 'fajita veggies', 'sour cream')
order2 = ('allison', 'greenfield', 'MAGIC', 'carnitas', 'brown', 'black', True, 'cheese', 'fajita veggies', 'sour cream', 'guacamole', 'tomato salsa')


def get_protein(order):
    protein = order[3]
    if protein == 'chicken':
        return 2.5
    elif protein == 'steak':
        return 3.5
    elif protein == 'barbacoa':
        return 3.5
    elif protein == 'carnitas':
        return 3.0
    elif protein == 'veggies':
        return 2.5
    else:
        return 0


def get_rice(order):
    rice = order[4]
    if rice == 'white':
        return 2.5
    elif rice == 'brown':
        return 3.5
    else:
        return 0

def get_beans(order):
    beans = order[5]
    if beans == 'black':
        return 2.5
    elif beans == 'pinto':
        return 2.5
    else:
        return 0

def get_burrito(order):
    burrito = order[6]
    if burrito == True:
        return 2.0
    else:
        return 0


def get_toppings(order):
    total = 0
    if 'guacamole' in order:
        if 'veggies' == order[3]:
            pass
        else:
            total = total + 2.75
    if 'tomato salsa' in order:
        total = total + 2.5
    if 'chili corn salsa' in order:
        total = total + 1.75
    if 'tomatillo green chili salsa' in order:
        total = total + 2.0
    if 'sour cream' in order:
        total = total + 2.5
    if 'fajita veggies' in order:
        if 'veggies' == order[3]:
            pass
        else:
            total = total + 2.5
    if 'cheese' in order:
        total = total + 2.0
    if 'queso blanco' in order:
        total = total + 2.75
    return total



def apply_discount(order, total):
    if order[2] == 'MAGIC':
        total = total - (total*0.05)
    if order[2] == 'SUNDAYFUNDAY':
        total = total - (total*0.1)
    if order[2] == 'FLAT3':
        total = total - 3
    return total


def approximate_time(order):
    delivery_time = 0
    if 'amherst' in order:
        delivery_time = 15
    if 'north amherst' in order:
        delivery_time = 15
    if 'south amherst' in order:
        delivery_time = 15
    if 'hadley' in order:
        delivery_time = 15
    if 'northampton' in order:
        delivery_time = 30
    if 'south hadley' in order:
        delivery_time = 30
    if 'belchertown' in order:
        delivery_time = 30
    if 'sunderland' in order:
        delivery_time = 30
    if 'holyoke' in order:
        delivery_time = 45
    if 'greenfield' in order:
        delivery_time = 45
    if 'deerfield' in order:
        delivery_time = 45
    if 'springfield' in order:
        delivery_time = 45
    return delivery_time


def generate_invoice(order):
    if order[6] == True:
        a = 'Yes'
    else:
        a = 'No'

    total = get_protein(order)+get_rice(order)+get_beans(order)+get_burrito(order)+get_toppings(order)
        
    print(f'Welcome to Chipotle Mexican Grill Hadley, {order[0]}.\nYour invoice is displayed below:\nProtein: {order[3]} - ${get_protein(order)}\nRice: {order[4]} rice - ${get_rice(order)}\nBeans: {order[5]} beans - ${get_beans(order)}')
    print(f'Burrito: {a} - ${get_burrito(order)}')
    print(f'Toppings: {', '.join(order[7:])} - ${get_toppings(order)}')
    print(f'Subtotal: ${total}\nDiscount Code: {order[2]}\nTotal: ${apply_discount(order,total)}\nYou Save: ${total-apply_discount(order,total)}')
    print(f'Your order will be ready in {approximate_time(order)} minutes.\nEnjoy your meal and have a good day!')

    

    

    

    

