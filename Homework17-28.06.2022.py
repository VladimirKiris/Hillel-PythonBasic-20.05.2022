# Game of Cities
"""
Returns maximum length of Game of cities sequence.

cities = (
    "Odessa Alchevsk Kremenchug Gostomel Lugansk Kirovograd Dnepr Reni Izmail Lviv Poltava Avdeevka Arcyz Zaporozhie
    Enakievo Voznesensk Konotop"
)

cities = ("Караганда Артем Вена Братислава Берлин Варшава Бразилиа Одесса Харбин "
          "Краков Париж Лондон Женева Милан Барселона Копенгаген Амстердам Акоб"
          )

"""


def chain(start_city: str, list_of_cities: list) -> list:
    remaining = list(list_of_cities)   # WHY list(list_of_cities), not list_of_cities?!
    remaining.remove(start_city)
    next_city = []
    for i in remaining:
        if i[0] == start_city[-1]:
            next_city.append(i)
    max_chain = []
    for c in next_city:
        check_chain = chain(c, remaining)
        if len(check_chain) > len(max_chain):
            max_chain = check_chain
    return [start_city] + max_chain


cities = str(input("Please enter cities sequence, divided by space: "))
cities_list = cities.lower()
cities_list = cities_list.split()
print("list is", cities_list)
maximum = list("")
for city in cities_list:
    lst = chain(city, cities_list)
    if len(lst) >= len(maximum):
        maximum = lst
print(maximum)
