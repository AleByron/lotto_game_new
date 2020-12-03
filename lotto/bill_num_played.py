import random

class bill_num_played():
    def __init__(self, num_played=""):
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

