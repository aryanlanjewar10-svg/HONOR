from abc import ABC, abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def get_payment_details(self):
        pass

    @abstractmethod
    def pay(self,amount:float)->None:
        pass

class RazorCardPayment(PaymentMethod):
    def __init__(self, card_number:str, card_holder:str, expiry_date:str):
        self.card_number=card_number
        self.card_holder=card_holder
        self.expiry_date=expiry_date

    def get_payment_details(self):
        return {
            "card_number":self.card_number,
            "card_holder":self.card_holder,
            "expiry_date":self.expiry_date
        }

    def pay(self, amount: float)->None:
        print(f"Paid {amount} using Razor Card.")

class RazorUpiPayment(PaymentMethod):
    def __init__(self, upi_id:str):
        self.upi_id = upi_id

    def get_payment_details(self):
        return {
            "upi_id": self.upi_id
        }

    def pay(self, amount: float)->None:
        print(f"Paid {amount} using Razor UPI.")

class StripeCardPayment(PaymentMethod):
    def __init__(self,card_number: str,card_holder: str,expiry_date: str):
        self.card_number=card_number
        self.card_holder=card_holder
        self.expiry_date=expiry_date

    def get_payment_details(self):
        return {
            "card_number":self.card_number,
            "card_holder":self.card_holder,
            "expiry_date":self.expiry_date
        }

    def pay(self, amount: float)->None:
        print(f"Paid {amount} using Stripe Card.")

class StripeUpiPayment(PaymentMethod):
    def __init__(self,upi_id: str):
        self.upi_id = upi_id

    def get_payment_details(self):
        return {
            "upi_id": self.upi_id
        }

    def pay(self, amount: float)->None:
        print(f"Paid {amount} using Stripe UPI.")   


class FactoryPaymentMethod(ABC):
    factory: dict={}

    @classmethod
    def get_payment_object(cls,payment_type:str,**kwargs)->PaymentMethod:
        if payment_type in cls.factory:
            return cls.factory[payment_type](**kwargs)
        else:
            raise ValueError(f"Payment type '{payment_type}' not supported.")

class RazorPayFactory(FactoryPaymentMethod):
    factory={
        "card":RazorCardPayment,
        "upi":RazorUpiPayment
    }

class StripeFactory(FactoryPaymentMethod):
    factory={
        "card":StripeCardPayment,
        "upi":StripeUpiPayment
    }

class Aggregator(ABC):
    def __init__(self, name:str,processing_fee:float):
        self.name=name
        self.processing_fee=processing_fee
    
    @abstractmethod
    def call_get_payment_object(self,payment_type:str,amount:float, **kwargs)->bool:
        pass

class RazorpayAggregator(Aggregator):
    def __init__(self):
        super().__init__("Razorpay", 0.02)
        self.factory=RazorPayFactory

    def call_get_payment_object(self,method_type:str,amount:float, **kwargs)->bool:
        payment_obj = self.factory.get_payment_object(method_type, **kwargs)
        final_amount=amount * (1+self.processing_fee)
        payment_obj.pay(final_amount)
        return True

class StripeAggregator(Aggregator):
    def __init__(self):
        super().__init__("Stripe", 0.029)
        self.factory = StripeFactory

    def call_get_payment_object(self,method_type: str,amount: float,**kwargs)->bool:
        payment_obj=self.factory.get_payment_object(method_type, **kwargs)
        final_amount = amount * (1+self.processing_fee)
        payment_obj.pay(final_amount)
        return True

class AggregatorFactory:
    factory: dict={
        "razorpay": RazorpayAggregator,
        "stripe": StripeAggregator
    }

    @classmethod
    def get_aggregator_object(cls, aggregator_type: str) -> Aggregator:
        if aggregator_type in cls.factory:
            return cls.factory[aggregator_type]()
        else:
            raise ValueError(f"Aggregator type '{aggregator_type}' not supported.")

def main():
    aggregator_name = input("Select Aggregator (razorpay/stripe):")
    method_type = input("Select Method (card/upi):")
    amount = float(input("Enter Amount:"))

    if method_type == "card":
        card_number = input("Enter Card Number: ")
        kwargs = {"card_number": card_number}
    else:
        upi_id = input("Enter UPI ID:")
        kwargs = {"upi_id": upi_id}

    aggregator = AggregatorFactory.get_aggregator_object(aggregator_name)
    success = aggregator.call_get_payment_object(method_type, amount, **kwargs)

    print("Payment Successful!" if success else "Payment Failed!")

main()
