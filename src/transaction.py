import pandas as pd
import click
from IPython.display import display, display_html


class Transaction:
    """
    Transaction Objects that hold transaction data
    Instanciating reuire no parameter

    Functionaly / Method :
    1. Add Item
    2. Update Item :
        a. Rename Item
        b. Change Quantity
        c. Change Price
    3. Delete Item
        a. Single Item
        b. All Item
    4. Check Order
    5. Calculate Total Ordr

    """

    def __init__(self) -> None:
        """
        Instanciating Object with empty dictionary to store data and empty data frame that will store total order data
        """
        self.transaction_dict = {}
        self.total_df = None

    def validate_dictionary(self):
        """
        Function that validate transaction data whether each value comply with its proper data types :
        item_name : Str
        item_amt : Int
        price_per_item : Float


        Raises:
            ValueError: if any value contain inapropriate data types
        """
        # loop over item
        for item_name in self.transaction_dict.keys():
            # typechecking
            if (
                self.transaction_dict[item_name]["item_amt"].isnumeric() == False
                or self.transaction_dict[item_name]["price_per_item"].isdecimal()
                == False
            ):
                raise ValueError(
                    f"Terdapat kesalahan input pada jumlah barang ,jumlah barang harus angka"
                )

    def add_item(self, item_name: str, item_amount: int, price_per_item: float):
        """
        Function to add transaction data ,item_name, item_amount, price_per_item

        Args:
            item_name (str): Item Name
            item_amount (int): Quantity of Item
            price_per_item (float): Price per Item

        Raises:
            ValueError: If Item Name Already Exists

        Returns:
            _type_: Object with added transaction_dictionary
        """
        # Check if any inserted name already exists in object dictionary
        if item_name in list(self.transaction_dict.keys()):
            raise ValueError("Item sudah ada , silahkan untuk update harga / jumlah")

        # Add Transaction
        self.transaction_dict[item_name] = {
            "item_name": item_name,
            "item_amt": item_amount,
            "price_per_item": price_per_item,
        }
        print(f"Berhasil Menambahkan Item: {self.transaction_dict[item_name]} ")

        return self

    def update_item_name(self, old_name, new_name):
        """
        Function to rename item name

        Args:
            old_name (_type_): Item Name to Replace
            new_name (_type_): New Item Name

        Raises:
            ValueError: if the old name does not exists in transaction_dict
        """

        if old_name not in self.transaction_dict.keys():
            raise ValueError(f"Nama Item yang akan anda ganti : {old_name},tidak ada")
        # Replace Dictionary Key
        self.transaction_dict[new_name] = self.transaction_dict[old_name]
        self.transaction_dict[new_name]["item_name"] = new_name
        # Validate Data to Make Sure it's proper

        # Delete old Keys
        del self.transaction_dict[old_name]

    def update_item_qty(self, item_name, new_qty):
        """
        Function to update Item Quantity

        Args:
            item_name (_type_): Item Name
            new_qty (_type_): Updated  Quantity

        Raises:
            ValueError: if new quantity is not numeric
        """
        # validate data type
        if new_qty.isnumeric() == False:
            raise ValueError("Quantity harus berupa angka")

        # replace value
        self.transaction_dict[item_name]["item_amt"] = new_qty

    def update_item_price(self, item_name, new_price):
        """
        Function to update item price

        Args:
            item_name (_type_): Item Name
            new_price (_type_): Updated Price

        Raises:
            ValueError: if new price is not decimal
        """
        # validate data type
        if new_price.isdecimal() == False:
            raise ValueError("Harga Barang harus angka")

        # replace value
        self.transaction_dict[item_name]["price_per_item"] = new_price

    def delete_item(self, item_name):
        """
        Function to delete single item

        Args:
            item_name (_type_): Item Name to Delete

        Raises:
            ValueError: if item_name doesnot exist in transaction_dict
        """
        # validate if item_name exists
        if item_name not in list(self.transaction_dict.keys()):
            raise ValueError("Item yang anda ingin hapus tidak ada atau belum di Input")
        else:
            # if exists it will delete the item name
            del self.transaction_dict[item_name]

    def delete_all(self):
        """
        Function to delete all transaction data in transaction_dict
        """
        # Deleting all Keys
        self.transaction_dict.clear()

    def check_order(self):
        """
        Function to check order, such as checking data type in transaction_dict and convert transaction_dict into pandas dataframe

        """
        self.validate_dictionary()
        # convert transaction dict into pd.DataFrame
        total_df = pd.DataFrame.from_records(data=list(self.transaction_dict.values()))
        # change data type from string to its proper dtype
        total_df["item_amt"] = total_df["item_amt"].astype("int")
        total_df["price_per_item"] = total_df["price_per_item"].astype("float")
        # calculate total_price
        total_df["total_price"] = total_df["item_amt"] * total_df["price_per_item"]
        display(total_df)
        self.total_df = total_df

        return self

    def calculate_discount(self, total_cart: float):
        """
        Function to calculate discount based on total_cart value

        Args:
            total_cart (float): total cat value from dataframe

        Returns:
            float:  discount
        """
        if total_cart > 500_000:
            return 0.1
        elif (total_cart > 300_000) & (total_cart <= 500_000):
            return 0.08
        elif (total_cart > 200_000) & (total_cart <= 300_000):
            return 0.05
        else:
            return 0

    def total_price(self):
        """
        function to calculate total price to pay by customer

        Raises:
            ValueError: If customer click total price without check order first

        Returns:
            float,float: total_payment,discount rate
        """
        # check if the check_order has been executed :
        # if total_df is empty the check order page has not been executed
        if not self.total_df.empty or self.total_df != None:
            total_cart = self.total_df["total_price"].sum()
            discount = self.calculate_discount(total_cart)
            total_payment = (1 - discount) * total_cart
            return total_payment, discount
        else:
            raise ValueError("Check Order Terlebih Dahulu")
