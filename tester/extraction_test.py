
class extraction:


    def extracted_numbers(self):
        extracted_n = {'bari': [84, 3, 46, 67, 66, 82, 49, 35, 80, 68], 'cagliari': [65, 39, 67, 44, 62, 74, 22, 85, 3, 80], 'firenze': [75, 47, 84, 36, 63, 56, 88, 51, 3, 74], 'genova': [37, 38, 68, 84, 10, 14, 44, 65, 22, 40], 'milano': [55, 40, 37, 18, 42, 78, 15, 81, 60, 84], 'napoli': [8, 17, 14, 18, 50, 33, 20, 23, 62, 77], 'palermo': [9, 15, 88, 56, 28, 84, 25, 86, 81, 2], 'roma': [78, 13, 61, 42, 59, 65, 48, 49, 17, 54], 'torino': [72, 89, 27, 23, 31, 70, 76, 83, 36, 28], 'venezia': [59, 13, 5, 18, 80, 62, 41, 85, 57, 60]}
        return extracted_n

    def winner(self):
        win = {'bari': ('1', 3), 'cagliari': ('1', 3), 'firenze': ('1', 1), 'genova': ('1', 2), 'milano': ('1', 2), 'palermo': ('1', 2), 'roma': ('1', 2), 'venezia': ('1', 3)}
        return win