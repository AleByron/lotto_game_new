from lotto.bill_type import bill_type
from lotto.bill_num import bill_num
from lotto.bill_num_played import bill_num_played
from lotto.bill_city import bill_city

class ticket():
    def __init__(self, inp_num_bill="", inp_city_type="", num_played="", inp_bill_type=""):
        self.inp_num_bill = inp_num_bill
        self.inp_city_type = inp_city_type
        self.num_played = num_played
        self.inp_bill_type = inp_bill_type
    def bill_type_ob(self):
        inp_bill_type = input("What kind of bill you want to play?\n Ambata, ambo, terno, quaterna, cinquina: ")
        bt = bill_type(inp_bill_type)
        result = bt.bill_type_m(inp_bill_type)
        return result

    def bill_num_ob(self):

        inp_bill_num = input("How many number you want to play?: ")
        bn = bill_num(inp_bill_num)
        number_of_numbers = bn.bill_num_m(inp_bill_num)
        bnp = bill_num_played(number_of_numbers)
        result = bnp.bill_num_played_m(number_of_numbers)

        return number_of_numbers, result



    def bill_city(self):
        inp_bill_city = input(
            "Select the city you want to play: \n Bari, Cagliari, Firenze, Genova, Milano, Napoli, Palermo, Roma, Torino, Venezia or all: ")
        bc = bill_city(inp_bill_city)
        result = bc.bill_city_m(inp_bill_city)
        return result





