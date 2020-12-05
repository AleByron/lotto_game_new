import random
class bill_num():
    def __init__(self, inp_num_bill="", num_played=""):
        self.inp_type_bill = inp_num_bill
        self.num_played = num_played

    @staticmethod
    def bill_num_played_m(num_played):
        counter = 0
        extracted_numbers = []
        while counter < int(num_played):
            num = random.randint(1, 90)
            if num not in extracted_numbers:
                extracted_numbers.append(num)
                counter = counter+1
            else:
                pass

        return extracted_numbers
    @staticmethod
    def bill_num_m(inp_num_bill):
        while True:
            if inp_num_bill.isdigit() == True and 0 < int(inp_num_bill) <= 10:
                return inp_num_bill
            else:
                inp = input("You should enter an integer between 1 and 10:")
                inp_num_bill = bill_num.bill_num_m(inp)
                return inp_num_bill

