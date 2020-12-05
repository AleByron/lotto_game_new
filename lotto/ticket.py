from lotto.bill_type import bill_type
from lotto.bill_num import bill_num
from lotto.bill_city import bill_city
from lotto.check_num_to_bill import check_num_to_bill

class ticket():
    def __init__(self, inp_num_bill="", inp_city_type="", num_played="", inp_bill_type="", extracted_numbers=""):
        self.inp_num_bill = inp_num_bill
        self.inp_city_type = inp_city_type
        self.num_played = num_played
        self.inp_bill_type = inp_bill_type
        self.extracted_numbers = extracted_numbers

    def bill_type_ob(self):
        inp_bill_type = input("What kind of bill you want to play?\n Ambata, ambo, terno, quaterna, cinquina: ")
        bt = bill_type(inp_bill_type)
        result = bt.bill_type_m(inp_bill_type)
        self.inp_bill_type = result
        return result

    def bill_num_ob(self):

        inp_bill_num = input("How many number you want to play?: ")
        bn = bill_num(inp_bill_num)
        number_of_numbers = bn.bill_num_m(inp_bill_num)
        self.inp_num_bill = number_of_numbers
        bnp = bill_num(number_of_numbers)
        result = bnp.bill_num_played_m(number_of_numbers)

        return number_of_numbers, result

    def bill_city(self):
        inp_bill_city = input(
            "Select the city you want to play: \n Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia or all: ")
        bc = bill_city(inp_bill_city)
        result = bc.bill_city_m(inp_bill_city)
        return result

    def check_num_to_bill_ob(self):
        bill = check_num_to_bill(self.inp_num_bill, self.inp_bill_type)
        result = bill.check_num_to_bill_m(self.inp_num_bill, self.inp_bill_type)
        return result

