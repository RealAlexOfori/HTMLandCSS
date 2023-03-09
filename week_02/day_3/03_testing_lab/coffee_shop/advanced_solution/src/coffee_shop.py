class CoffeeShop:

    def __init__(self, name, till):
        self.name = name
        self.till = till
        #self.drinks = []
        self.stock = {}


    def add_drink(self, drink):
        if drink in self.stock:
            self.stock[drink] += 1
        else:
            self.stock[drink] = 1


    def stock_level(self, drink):
        if drink in self.stock:
            return self.stock[drink]
        else:
            return 0

    def stock_value(self):
        total = 0

        for drink in self.stock:
            total += (drink.price * self.stock[drink])

        return total

    def drink_names(self):
        drink_list = list(self.stock.keys())
        # drink_name_list = []
        # for drink in drink_list:
        #     drink_name_list.append(drink.name)
        drink_name_list = [drink.name for drink in drink_list]
        return drink_name_list


    def drinks_customer_can_afford(self, customer):
        drink_list = list(self.stock.keys())
        # affordable_drinks = []
        # for drink in drink_list:
        #     if customer.sufficient_funds(drink):
        #         affordable_drinks.append(drink.name)
        affordable_drinks = [drink.name for drink in drink_list if customer.sufficient_funds(drink)]
        return affordable_drinks

    def can_serve(self, customer, drink):
        if not self.customer_is_old_enough(customer):
            return False
        if self.customer_too_energetic(customer):
            return False
        if not self.customer_can_afford_drink(customer, drink):
            return False
        if self.stock_level(drink) == 0:
            return False
        return True;


    def serve(self, customer, drink):
        if self.can_serve(customer, drink):
            self.stock[drink] -= 1
            customer.buy_drink(drink)
            self.till += drink.price


    def customer_is_old_enough(self, customer):
        return customer.age >= 16


    def customer_can_afford_drink(self, customer, drink):
        return customer.sufficient_funds(drink)


    def customer_too_energetic(self, customer):
        return customer.energy >= 50
