class bill_type():

    @staticmethod
    def bill_type_inp():
        inp_bill_type = input("What kind of bill you want to play?\n Ambata, ambo, terno, quaterna, cinquina: ")
        return inp_bill_type

    @staticmethod
    def bill_type_check():
        check = ['ambata', 'ambo', 'terno', 'quaterna', 'cinquina']
        return check