import random

class bill_type():

    @staticmethod
    def bill_type_inp():
        inp_bill_type = input("What kind of bill you want to play?\n 1 - Ambata \n 2 - Ambo \n 3 - Terno \n 4 - Quaterna \n 5 - Cinquina: ")
        return inp_bill_type

    @staticmethod
    def bill_type_check():
        check = ['1', '2', '3', '4', '5']
        return check


class bill_num():
    def __init__(self, inp_num_bill="", num_played=""):
        self.inp_type_bill = inp_num_bill
        self.num_played = num_played

    @staticmethod
    def bill_num_inp():
        inp_num_bill = input("How many numbers you want to play?(1 to 10): ")
        return inp_num_bill

    @staticmethod
    def bill_num_played_static(num_played):
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

class bill_city():

    def __init__(self, city=""):
        self.city = city

    @staticmethod
    def bill_city_inp():
        inp_bill_city = input(
            "Select the city you want to play: \n 1 - Bari \n 2 - Cagliari\n 3 - Firenze\n 4 - Genova\n 5 - Milano\n 6 - Napoli\n 7 - Palermo\n 8 - Roma\n 9 - Torino\n 10 - Venezia\n 11 - All: ")
        return inp_bill_city

    @staticmethod
    def bill_city_check():
        cities = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11']

        return cities

class check_num_to_bill():

    @staticmethod
    def check_num_to_bill_static(inp_bill_type, inp_num_bill):

        if inp_bill_type == 'cinquina' and int(inp_num_bill) < 5:
            print('You have to ask at least for 5 numbers in order to play for a cinquina')
            result = False
        elif inp_bill_type == 'quaterna' and int(inp_num_bill) < 4:
            print('You have to ask at least for 4 numbers in order to play for a quaterna')
            result = False
        elif inp_bill_type == 'terno' and int(inp_num_bill) < 3:
            print('You have to ask at least for 3 numbers in order to play for a terno')
            result = False
        elif inp_bill_type == 'ambo' and int(inp_num_bill) < 2:
            print('You have to ask at least for 2 numbers in order to play for an ambo')
            result = False
        elif int(inp_num_bill) == 0:
            result = False
        else:
            result = True

        return result

class final_check_help():

    @staticmethod
    def check_help(score, inp_bill_type):
        if inp_bill_type == "2" and score >= 2:
            bills_amount = score - 1
        elif inp_bill_type == "3" and score >= 3:
            bills_amount = score - 2
        elif inp_bill_type == "4" and score >= 4:
            bills_amount = score - 3
        elif inp_bill_type == "5" and score >= 5:
            bills_amount = score - 4
        elif inp_bill_type == "1" and score >= 1:
            bills_amount = score
        else:
            bills_amount = 0

        return inp_bill_type, bills_amount


class bill_bet_money():

    @staticmethod
    def bet_money_static():
        try:
            bet_money = float(input('How mutch you want to bet?: '))
            return bet_money
        except ValueError:
            print("Your bet is invalid, retry.")
            bet_money = bill_bet_money().bet_money_static()
            return bet_money