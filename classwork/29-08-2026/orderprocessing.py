# get order calculator the total and use payment method to pay
# method to pay - card, upi

import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List,Dict

@dataclass            # class to store item details
class Item:
    name: str
    price: float
    quantity: int

# __init__ -> contructor
# __str__ -> string representation of the object
class Order:
    # constructor :
    def __init__(self,items: List[Item]):
        self.items = items

    @classmethod
    def from_dict(cls, items_dict: List[Dict]) -> 'Order':
        items = [Item(**item) for item in items_dict]
        return cls(items)

    @property
    def total_items(self) -> int:
        return sum(item.quantity for item in self.items)

    @property
    def grand_total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)



    def calculate_total(self) -> float:
        return sum(item.price * item.quantity for item in self.items)

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        pass    # always use pass in abstract

class CardPayment(PaymentMethod):   #inheritance
    def __init__(self, card_number: str, card_holder: str, expiry_date: str):
        self.card_number = card_number
        self.card_holder = card_holder
        self.expiry_date = expiry_date
        
    def pay(self, amount: float) -> None:   #runtime polymorpism
        print(f"Paid {amount} using Card.")

class UpiPayment(PaymentMethod):
    def __init__(self, upi_id: str):
        self.upi_id = upi_id

    def pay(self, amount: float) -> None:
        print(f"Paid {amount} using UPI.")

class PaymentAggregator:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, amount: float) -> None:
        self.payment_method.pay(amount)

def process_order(payment_method: PaymentMethod) -> None:
    while True:
        try:
            print("\n--- Order Processing ---")
            user_choice = input("Do you want to process an order? (yes/no): ").strip().lower()
            
            if user_choice == 'no':
                print("Exiting order processing.")
                break
            elif user_choice != 'yes':
                print("Invalid input. Please enter 'yes' or 'no'.")
                continue
            
            # Get item details from user
            item_name = input("Enter item name: ").strip()
            if not item_name:
                print("Item name cannot be empty.")
                continue
            
            try:
                quantity = int(input("Enter quantity: ").strip())
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue
            except ValueError:
                print("Quantity must be a valid integer.")
                continue
            
            try:
                price = float(input("Enter price: ").strip())
                if price < 0:
                    print("Price cannot be negative.")
                    continue
            except ValueError:
                print("Price must be a valid number.")
                continue
            
            # Create item and order
            item = Item(name=item_name, price=price, quantity=quantity)
            order = Order(items=[item])
            
            # Process payment
            total_amount = order.calculate_total()
            print(f"Total amount to be paid: {total_amount}")
            payment_aggregator = PaymentAggregator(payment_method)
            payment_aggregator.process_payment(total_amount)
            
        except AttributeError as ae:
            print(f"Attribute Error: {ae}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")