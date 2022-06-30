# Game of Cities
"""
Returns maximum length of Game of cities sequence.

cities = (
    "Odessa Alchevsk Kremenchug Gostomel Lugansk Kirovograd Dnepr "
    "Reni Izmail Lviv Poltava Avdeevka Arcyz Zaporozhie Enakievo Voznesensk Konotop"
)
 """


def cities_game_rec(list_of_cities: list, city: str = "", cities_seq=None, start: int = 0) -> list:
    if cities_seq is None:
        cities_seq = list()
    clone_cities = list_of_cities.copy()
    if city != "":
        for i in clone_cities:
            if str(cities_seq[-1])[-1] == i[0]:
                cities_seq.append(i)
                clone_cities.remove(i)
                cities_game_rec(clone_cities, cities_seq[-1], cities_seq)
                break
        return cities_seq
    else:
        city = clone_cities[start]
        clone_cities.remove(city)
        cities_seq.clear()
        cities_seq.append(city)
        return cities_game_rec(clone_cities, city, cities_seq)


cities = str(input("Please enter cities sequence, divided by space: "))
cities_list = cities.lower()
cities_list = cities_list.split()
cities_list.sort(reverse=True)
print("list is", cities_list)
maximum = 0
iteration = 0
for index in range(len(cities_list)):
    if len(cities_game_rec(cities_list, start=index)) >= maximum:
        maximum = len(cities_game_rec(cities_list, start=index))
        iteration = index
print("max length is:", maximum, ", sequence is", cities_game_rec(cities_list, start=iteration))
