import unittest
from lotto.ticket import ticket


class Test_lotto_game(unittest.TestCase):


    def test_bill_type(self):
        result = ticket().bill_type_ob("ambo")
        self.assertIn( result, "ambata ambo terno quaterna cinquina")