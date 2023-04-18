massive_ = [10, 15, 13, 9, 7, 11, 14]
def sort(massive_):

    if len(massive_) <= 1:
        return massive_
    else:
        element_ = massive_[0]
        less_el = [x for x in massive_[1:] if x < element_]
        bigger_el = [x for x in massive_[1:] if x >= element_]
        return sort(less_el) + [element_] + sort(bigger_el)

print(sort(massive_))