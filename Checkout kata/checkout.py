class Checkout:
    class Discount:
        def __init__(self, nrItems, price):
            self.nrItems = nrItems
            self.price = price
            
    def __init__(self):
        self.items = {}
        self.prices = {}
        self.discounts = {}
        self.total = 0

    def addItemPrice(self, item, price):
        self.prices[item] = price

    def addDiscount(self, item, nrItems, price):
        discount = self.Discount(nrItems, price)
        self.discounts[item] = discount

    def addItem(self, item):
        if item not in self.prices: raise Exception("There is no such item!")

        if item in self.items:
            self.items[item] += 1
        else:
            self.items[item] = 1

    def calculateTotal(self):
        total = 0
        for item, count in self.items.items():
            total += self._calculateItemTotal(item, count)
        return total

    def _calculateItemTotal(self, item, count):
        total = 0
        
        if item in self.discounts:
            discount = self.discounts[item]
            if count >= discount.nrItems:
                total += self._calculateItemDiscountedTotal(item, count, discount)
            else:
                total += self.prices[item] * count
        else:
            total += self.prices[item] * count

        return total
    
    def _calculateItemDiscountedTotal(self, item, count, discount):
        total = 0
        
        nrDiscounts = count // discount.nrItems
        total += nrDiscounts * discount.price
        remaining = count % discount.nrItems
        total += remaining * self.prices[item]

        return total