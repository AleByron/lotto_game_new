class lotto_printer():

    def __init__(self, bill_type="", city="", played_numbers="", extracted_numbers="", winners = ""):
        self.city = city
        self.bill_type = bill_type
        self.played_numbers = played_numbers
        self.extracted_numbers = extracted_numbers
        self.winners = winners

    @staticmethod
    def printer(bill_type, city, played_numbers ):
        length = 40
        print("\n")
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
        print("\n")

    @staticmethod
    def extraction_printer(extracted_numbers):
        print("\n")
        print("THE EXTRACTED NUMBERS ARE:")
        print("\n")
        for extr_city in extracted_numbers:
            print(extr_city.capitalize())
            print(*extracted_numbers[extr_city], sep=", ")
        print("\n")

    @staticmethod
    def winner_printer(winners):
        for win in winners:
            print("You won {bill_n} {bill_t} on {bill_c} ".format(bill_n = winners[win][1], bill_t=winners[win][0], bill_c=win))


