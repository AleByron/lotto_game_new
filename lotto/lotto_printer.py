class lotto_printer():

    def __init__(self, bill_type="", city="", played_numbers=""):
        self.city = city
        self.bill_type = bill_type
        self.played_numbers = played_numbers

    @staticmethod
    def printer(bill_type, city, played_numbers ):
        length = 40
        print("+" + '-' * length + "+")
        print('|' + ' ' * length + "|")
        print('|' + ' ' * 14 + 'LOTTO TICKET' + ' ' * 14 + "|")
        print('|' + ' ' * length + "|")
        print("+" + '-' * length + "+")
        print('|' + ' ' * length + "|")
        print("|" + " " + "TYPE OF BILL: " + " "*25 + "|" )
        print("|" + " " + bill_type + (39 - len(bill_type))*" " +"|" )
        print('|' + ' ' * length + "|")
        print("|" + " " + "CITY: " + " "*33 + "|")
        print("|" + " " +  city + (39 - len(city))*" " + "|" )
        print('|' + ' ' * length + "|")
        print("|" + " " + "PLAYED NUMBERS: " + " "*23 + "|")
        print("|" + " " + str(played_numbers)[1:-1] + (39 - len(str(played_numbers)[1:-1]))*" " +"|" )
        print('|' + ' ' * length + "|")
        print("+" + '-' * length + "+")



