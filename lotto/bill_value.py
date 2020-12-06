class bill_value():
    def __init__(self, won_bets, inp_bill_type, inp_num_bill, bet_money, inp_city_type):
        self.won_bets = won_bets
        self.inp_bill_type = inp_bill_type
        self.inp_num_bill = inp_num_bill
        self.bet_money = bet_money
        self.inp_city_type = inp_city_type



    def bill_value_met(self):
        final_value = 0
        bill_num = int(self.inp_num_bill)
        if self.inp_city_type == "all":
            bet_money = self.bet_money/10
        else:
            bet_money = self.bet_money


        for won in self.won_bets:
            if self.inp_bill_type == "ambata":
                bill_values = [11.23, 5.61, 3.74, 2.80, 2.24, 1.87, 1.60, 1.40, 1.24, 1.12]
                final_value = final_value + bet_money * bill_values[bill_num - 1]*int(self.won_bets[won][1])
            elif self.inp_bill_type == 'ambo':
                bill_values = [250, 83.33, 41.66, 25, 16.66, 11.90, 8.92, 6.94, 5.55]
                final_value = final_value + bet_money * bill_values[bill_num - 2]*int(self.won_bets[won][1])
            elif self.inp_bill_type == 'terno':
                bill_values = [4500, 1125, 450, 225, 128.57, 80.35, 53.57, 37.50]
                final_value = final_value + bet_money * bill_values[bill_num - 3]*int(self.won_bets[won][1])
            elif self.inp_bill_type == 'quaterna':
                bill_values = [120000, 24000, 8000, 3428.57, 1714.28, 952.38, 571.42]
                final_value = final_value + bet_money * bill_values[bill_num - 4]*int(self.won_bets[won][1])
            elif self.inp_bill_type == 'cinquina':
                bill_values = [6000000, 1000000, 285714.28, 107142.85, 47619.04, 23809.52]
                final_value = final_value + bet_money * bill_values[bill_num - 5]*int(self.won_bets[won][1])

        final_value_taxed = final_value - (final_value / 100) * 8

        return round(final_value,2), round(final_value_taxed,2)