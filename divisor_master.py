def simple_number(n):
    if n > 2:
        i = 2
        lim = n ** 0.5
        while i <= lim:
            if n % i == 0:
                return False
                break
            i += 1
        else: return True

    else: return True


def list_of_divs(n):
    i = 1
    new_list = []
    lim = n / 2
    while i <= lim:
        if n % i == 0:
            new_list.append(i)
        i += 1
    new_list.append(n)
    return new_list


def max_simple_div(n):
    all_divs = list(list_of_divs(n))
    all_divs.reverse()
    i = 0
    while i < len(all_divs):
        if simple_number(all_divs[i]) == True:
            break
        i += 1
    return all_divs[i]

def max_div(n):
    all_divs = list(list_of_divs(n))
    all_divs.reverse()
    return all_divs[1]


print(simple_number(99))
print(list_of_divs(99))
print(max_simple_div(99))
print(max_div(99))

