list_of_times = [(1,2), (2,6), (3,10), (15, 20), (20, 24)]

def is_enough_rocket(list_of_items):
    list_of_items.sort(key=lambda x: x[0])

    end_time = 0
    for item in list_of_items:
        start, finish = item

        if start >= end:

            end = finish
        else:
            end = max(end, finish)

    return end <= 24