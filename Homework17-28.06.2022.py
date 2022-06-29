# Game of Cities
"""
Returns maximum length of Game of cities sequence.

Odessa Alchevsk Kremenchug Gostomel Lugansk Kirovograd Dnepr Reni Izmail Lviv
Poltava Avdeevka Arcyz Zaporozhie Enakievo Voznesensk Konotop
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
                break
            if i == clone_cities[-1]:
                return cities_seq
        c = cities_game_rec(clone_cities, cities_seq[-1], cities_seq)
        return c
    else:
        city = clone_cities[start]
        clone_cities.remove(city)
        cities_seq.clear()
        cities_seq.append(city)
        d = cities_game_rec(clone_cities, city, cities_seq)
        return d


cities = str(
    "Alchevsk Arcyz Zaporozhie Konotop Avdeevka Poltava Reni Enakievo Kremenchug Odessa "
    "Gostomel Lugansk Kirovograd Dnepr Izmail Lviv Voznesensk"
)
cities_list = cities.lower()
cities_list = cities_list.split()
cities_list.sort()
print("list is", cities_list)
maximum = 0
iteration = 0
for i in range(len(cities_list)):
    if len(cities_game_rec(cities_list, start=i)) >= maximum:
        maximum = len(cities_game_rec(cities_list, start=i))
        iteration = i
print("max length is:", maximum, ", sequence is", cities_game_rec(cities_list, start=iteration))
