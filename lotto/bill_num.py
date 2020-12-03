class bill_num():
    def __init__(self, inp_num_bill):
        self.inp_type_bill = inp_num_bill

    @staticmethod
    def bill_num_m(inp_num_bill):
        while True:
            if inp_num_bill.isdigit() == True and 0 < int(inp_num_bill) <= 10:
                return inp_num_bill
            else:
                inp = input("You should enter an integer between 1 and 10:")
                inp_num_bill = bill_num.bill_num_m(inp)
                return inp_num_bill

