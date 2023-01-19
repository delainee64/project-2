# Author: Delainee Lenss
# GitHub username: delainee64
# Date: 01/14/2023
# Description: Submit a file that contains unit tests for your classes. It must have at least five
# unit tests and use at least two different assert functions.

import unittest
from LemonadeStand import MenuItem, SalesForDay, LemonadeStand


class LemonTest(unittest.TestCase):

    def test_1(self):
        """Tests get.name()"""
        name1 = LemonadeStand('Lemons R Us')
        self.assertEqual(name1.get_name(), 'Lemons R Us')

    def test_2(self):
        """Tests get.wholesale_cost()"""
        item1 = MenuItem('lemonade', 0.5, 1.5)
        self.assertEqual(item1.get_wholesale_cost(), 0.5)

    def test_3(self):
        """Tests get.selling_price()"""
        item2 = MenuItem('lemonade', 0.5, 1.5)
        self.assertEqual(item2.get_selling_price(), 1.5)

    def test_4(self):
        """Tests total_sales_for_menu_item"""
        sales1 = LemonadeStand(0)
        self.assertNotEqual(sales1.total_sales_for_menu_item('lemonade'), 5)

    def test_5(self):
        """Tests total_profit_for_stand"""
        day1 = LemonadeStand('lemonade')
        self.assertEqual(day1.total_profit_for_stand(), 0)


if __name__ == '__main__':
    unittest.main()
