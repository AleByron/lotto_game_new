import random

class extraction:
    def __init__(self, extracted_numbs="", inp_city_type="", num_played="", inp_bill_type="" ):
        self.extracted_numbs = extracted_numbs
        self.inp_city_type = inp_city_type
        self.num_played = num_played
        self.inp_bill_type = inp_bill_type

    def numbers(self):
        self.extracted_numbs = {'bari':[], 'cagliari':[], 'firenze':[], 'genova':[], 'milano':[], 'napoli':[], 'palermo':[], 'roma':[], 'torino':[], 'venezia':[]}
        for city in self.extracted_numbs:
            x = 0
            while x < 10:
                n = random.randint(1, 90)
                if n not in self.extracted_numbs[city]:
                    self.extracted_numbs[city].append(n)
                    x = x + 1
                else:
                    pass
        return self.extracted_numbs

    def check_help(self, score, inp_bill_type):
        if inp_bill_type == "ambo" and score >= 2:
            bills_amount = score - 1
        elif inp_bill_type == "terno" and score >= 3:
            bills_amount = score - 2
        elif inp_bill_type == "quaterna" and score >= 4:
            bills_amount = score - 3
        elif inp_bill_type == "cinquina" and score >= 5:
            bills_amount = score - 4
        elif inp_bill_type == "ambata" and score >= 1:
            bills_amount = score
        else:
            bills_amount = 0

        return inp_bill_type, bills_amount

    def checker(self, inp_city_type, num_played, inp_bill_type):

        winners = {}
        score = 0

        for city in self.extracted_numbs:
            #print(city)
            if city == inp_city_type and city != 'all':
                numb = self.extracted_numbs[city]
                print(numb)
                for n in num_played:
                    if n in numb:
                        score = score + 1
                won_bills = extraction.check_help(self, score, inp_bill_type)
                if won_bills[1] != 0:
                    winners[city] =  won_bills
            elif inp_city_type == 'all':
                for city_all in self.extracted_numbs:
                    score = 0
                    for n in num_played:
                        if n in self.extracted_numbs[city_all]:
                            score = score + 1
                    won_bills = extraction.check_help(self, score, inp_bill_type)
                    if won_bills[1] != 0:
                        winners[city_all] = won_bills

        return winners









