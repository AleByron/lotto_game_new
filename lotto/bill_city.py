class bill_city():

    def __init__(self, city=""):
        self.city = city

    @staticmethod
    def bill_city_m(city):
        cities = ['bari', 'cagliari', 'firenze', 'genova', 'milano', 'napoli', 'palermo', 'roma', 'torino', 'venezia',
                  'all']

        city = city.lower()
        if city not in cities:
            city=input('Invalid city, retry: ')
            bill_city.bill_city_m(city)

        return city.lower()