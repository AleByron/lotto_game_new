class check_num_to_bill():
    def __init__(self, inp_num_bill, inp_type_bill):
        self.inp_type_bill = inp_num_bill
        self.inp_type_bill = inp_type_bill

    @staticmethod
    def check_num_to_bill_m(inp_num_bill, inp_type_bill):
        print(inp_num_bill)
        if inp_type_bill == 'cinquina' and int(inp_num_bill) < 5:
            print('You have to ask at least for 5 numbers in order to play for a cinquina')
            result = False
        elif inp_type_bill == 'quaterna' and int(inp_num_bill) < 4:
            print('You have to ask at least for 4 numbers in order to play for a quaterna')
            result = False
        elif inp_type_bill == 'terno' and int(inp_num_bill) < 3:
            print('You have to ask at least for 3 numbers in order to play for a terno')
            result = False
        elif inp_type_bill == 'ambo' and int(inp_num_bill) < 2:
            print('You have to ask at least for 2 numbers in order to play for an ambo')
            result = False
        elif int(inp_num_bill) == 0:
            result = False
        else:
            result = True

        return result



