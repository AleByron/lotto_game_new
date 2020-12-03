class bill_type():
    def __init__(self, inp_type_bill):
        self.inp_type_bill = inp_type_bill

    @staticmethod
    def bill_type_m(inp_type_bill):
        try:
            checkType = ['ambata', 'ambo', 'terno', 'quaterna', 'cinquina']
            inp_type_bill = inp_type_bill.lower()
            if inp_type_bill not in checkType:
                inp_type_bill = input('Your bill is invalid, retry: ')
                bill_type.bill_type_m(inp_type_bill)
            print(inp_type_bill)
            return inp_type_bill
        except EOFError:
            bill_type.bill_type_m(inp_type_bill)
            return inp_type_bill