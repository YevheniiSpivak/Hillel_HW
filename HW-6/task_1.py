from collections import namedtuple

country = namedtuple('country', ['country_name', 'popular', 'people_km'])

canada = country('Canada', 38_250_000, '4.2 people/km²')
usa = country('USA', 336_000_000, '33.6 people/km²')
china = country('China', 1_412_000_000, '134 people/km²')
holland = country('Holland', '17_530_000', '517 people/km²')

countries = (canada, usa, china, holland)

for country in countries:
    if isinstance(country.popular, int):
        print(f'The population of {country.country_name} is {country.popular} people and {country.people_km}')
    else:
        print(f'Warning! Invalid data type. Expected <class \'int\'>, Actual {type(country.popular)}')
