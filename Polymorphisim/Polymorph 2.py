class India:
    capital_city = "New Delhi"
    language = "Hindi"
    country = 'India'

    @classmethod
    def capital(cls):
        print(f"Capital of {cls.country} is ", cls.capital_city)

    @classmethod
    def lang(cls):
        print(f"Language of {cls.country} is ", cls.language)


class USA(India):
    capital_city = "Washing Ton DC"
    language = "English"
    country = "USA"


obj_ind = India()
obj_usa = USA()
countries = (obj_ind, obj_usa)

for country in countries:
    print(" ")
    country.lang()
    country.capital()
    print(" ")

