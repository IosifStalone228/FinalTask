list_of_people = ["Vasya", "Petya", "Vanya", "Slava", "Katya","Fedya", "Katya"]
syllable_number = 5

def children_counter(list1: list, syllables: int) -> int:
    list2 = list1.copy()
    while len(list2) != 0:
        a = list2[syllables % len(list2) - 1]
        list2.pop(syllables % len(list2) - 1)
        index_ = list1.index(a) + 1
    print(index_)
    return index_


children_counter(list_of_people, syllable_number)
