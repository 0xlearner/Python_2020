def read_file(file):
    first_every_2 = ()
    second_every_2 = ()
    line_count = 0
    for line in file:
        stripped_line = line.replace('\n', '')
        # every other line starting with the first one
        if line_count % 2 == 0:
            first_every_2 += (stripped_line, )
        elif line_count % 2 == 1:
            second_every_2 += (stripped_line, )
        line_count += 1
    return (first_every_2, second_every_2)


def sanitize(some_tuple):
    clean_string = ()
    for st in some_tuple:
        st = st.replace(' ', '')
        st = st.replace('-', '')
        st = st.replace('(', '')
        st = st.replace(')', '')
        clean_string += (st, )
    return clean_string


def analyze_friends(names, phones, all_areacodes, all_places):
    """
    names: tuple of friend names
    phones: tuple of phone numbers without special symbols
    all_areacodes: a tuple of area codes
    all_places: a tuple of states
    Prints out how many friends you have and every unique state
    that is represented by their phone numbers.
    """
    def get_unique_area_coe():
        """
        Return a tuple of all unique area codes in phones
        """
        area_codes = ()
        for ph in phones:
            if ph[0:3] not in area_codes:
                area_codes += (ph[0:3], )
        return area_codes

    def get_states(some_areacodes):
        """
        some_areacodes: tuple of area codes
        Returns a tuple of the states associated with some_area codes

        """
        states = ()
        for ac in some_areacodes:
            if ac not in some_areacodes:
                states += ('BAD AREACODE', )
            else:
                # use index to match area code with a state
                index = all_areacodes.index(ac)
                states += (all_places[index], )
        return states

    num_friends = len(names)
    unique_area_code = get_unique_area_coe()
    unique_states = get_states(unique_area_code)

    print(f'You have {num_friends},friends!')
    print('They live in:')
    for state in unique_states:
        print(state)


data_file = open('data.txt')
map_file = open('area_codes.txt')
(names,phones) = read_file(data_file)
(areacodes, place) = read_file(map_file)
data_file.close()
map_file.close()
# print(names)
# print(phones)
clean_phone = sanitize(phones)
# print(clean_phone)
analyze_friends(names,clean_phone,areacodes,place)