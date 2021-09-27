import pytest
from checkout import Checkout

class TestCheckout:
    def setup_method(self, method):
        self.checkout = Checkout()
        self.checkout.addItemPrice("Apple", 1)
        self.checkout.addItemPrice("Banana", 2)

    def test_canCalculateTotal(self):
        self.checkout.addItem("Apple")
        assert self.checkout.calculateTotal() == 1

    def test_getCorrectTotalWithMultipleItems(self):
        self.checkout.addItem("Apple")
        self.checkout.addItem("Banana")
        assert self.checkout.calculateTotal() == 3

    def test_canAddDiscountRule(self):
        self.checkout.addDiscount("Apple", 3, 2)

    def test_getDiscount(self):
        self.checkout.addDiscount("Apple", 3, 2)
        self.checkout.addItem("Apple")
        self.checkout.addItem("Apple")
        self.checkout.addItem("Apple")
        assert self.checkout.calculateTotal() == 2

    def test_exceptionItemWithNoPrice(self):
        with pytest.raises(Exception):
            self.checkout.addItem("Cocoa")