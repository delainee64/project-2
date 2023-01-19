# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 01/14/2023
# Description: Write code for recording the menu items and daily sales of a lemonade stand. LemonadeStand
# should contain a dictionary of MenuItems. It also contains a list of SalesForDay objects, and each of those
# SalesForDay objects contains a dictionary of items sold on a particular day.

class MenuItem:
    """Represents a menu item offered for sale at the lemonade stand."""

    def __init__(self, name, wholesale_cost, selling_price):
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """Returns the name of the item."""
        return self._name

    def get_wholesale_cost(self):
        """Returns the wholesale cost of the item."""
        return self._wholesale_cost

    def get_selling_price(self):
        """Returns the price of each item."""
        return self._selling_price


class SalesForDay:
    """Represents the sales made in a particular day."""

    def __init__(self, day, sales_dict):
        self._day = day
        self._sales_dict = sales_dict

    def get_day(self):
        """Returns the number of days the stand has been open."""
        return self._day

    def get_sales_dict(self):
        """Returns the items sold that day."""
        return self._sales_dict


class InvalidSalesItemError(Exception):
    pass


class LemonadeStand:
    """Represents a lemonade stand."""

    def __init__(self, name):
        self._name = name  # Name of the lemonade stand (string)
        self._current_day = 0  # Initializes current day to zero.
        self._menu = {}  # empty dictionary for menu items.
        self._sales_record = []  # Initializes sales to an empty list.

    def get_name(self):
        """Returns the name of the lemonade stand."""
        return self._name

    def add_menu_item(self, menu_item):
        """Adds an item on the menu to the dictionary."""
        self._menu[menu_item.get_name()] = menu_item

    def enter_sales_for_today(self, menu_dict):
        """Returns sales for the current day."""
        try:
            for item, key in menu_dict.items():
                if item not in self._menu.keys():
                    raise InvalidSalesItemError
            sales_for_today = SalesForDay(self._current_day, menu_dict)
            self._sales_record.append(sales_for_today)
            self._current_day += 1
        except InvalidSalesItemError as explain:
            print("Item is not listed in the menu.")

    def sales_of_menu_item_for_day(self, day, menu_item_name):
        """Returns the number of an item sold that day."""
        sales = 0
        for record in self._sales_record:
            if record.get_day() == day:
                sales_dict = record.get_sales_dict()
                sales = sales_dict.get(menu_item_name, 0)
                break
        return sales

    def total_sales_for_menu_item(self, menu_item_name):
        """Returns total number sold of a particular item over the history of the stand."""
        total_sales = 0
        for day in range(self._current_day + 1):
            total_sales += self.sales_of_menu_item_for_day(day, menu_item_name)
        return total_sales

    def total_profit_for_menu_item(self, menu_item_name):
        """Returns the total profit of a particular item over the history of the stand."""
        total_sales_of_item = self.total_sales_for_menu_item(menu_item_name)
        menu_item = self._menu.get(menu_item_name)
        total_profit = total_sales_of_item * menu_item.get_selling_price() - total_sales_of_item * \
                       menu_item.get_wholesale_cost()
        return total_profit

    def total_profit_for_stand(self):
        """Returns the total profit on all items in the history of the stand."""
        total_profit = 0
        for name, menu_item in self._menu.items():
            total_sales_of_item = self.total_sales_for_menu_item(name)
            profit = total_sales_of_item * menu_item.get_selling_price() \
                     - total_sales_of_item * menu_item.get_wholesale_cost()
            total_profit += profit
        return total_profit


# def main():
    # stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand called 'Lemons R Us'
    # item1 = MenuItem('lemonade', 0.5,
                      # 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
    # stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
    # item2 = MenuItem('nori', 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
    # stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
    # item3 = MenuItem('cookie', 0.2, 1)  # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
    # stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'

    # This dictionary records that on day zero, 5 lemonades were sold, 2 cookies were sold, and no nori was sold
    # day_0_sales = {
        # 'lemonade': 5,
       # 'cookie': 2
    # }

    # This dictionary records that on day one, 5 lemonades were sold, 3 cookies were sold, and no nori was sold
    #  day_1_sales = {
       # 'lemonade': 5,
       # 'cookie': 3
    # }

    # stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
    # stand.enter_sales_for_today(day_1_sales)  # Record the sales for day one

    # print(
        # f"lemonade profit = {stand.total_profit_for_menu_item('lemonade')}")

    # print(f"total sales for menu item 'cookie': {stand.total_sales_for_menu_item('cookie')}")


# if __name__ == "__main__":
    # main()
