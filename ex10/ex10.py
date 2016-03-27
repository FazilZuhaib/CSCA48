bin0 = []
bin1 = []
bin2 = []
bin3 = []
bin4 = []
bin5 = []
bin6 = []
bin7 = []
bin8 = []
bin9 = []


def place_bin(item, level):
    '''(int) -> NoneType
    Places the given int into the appropriate bin.
    '''
    # make a string version of item
    sitem = str(item)
    # get the character of the sig dig we are looking for
    if level <= len(sitem):
        sig_string = sitem[-level]
    else:
        sig_string = '0'
    # make sig_dig an indigt
    sig_dig = int(sig_string)
    if sig_dig == 0:
        bin0.append(item)
    elif sig_dig == 1:
        bin1.append(item)
    elif sig_dig == 2:
        bin2.append(item)
    elif sig_dig == 3:
        bin3.append(item)
    elif sig_dig == 4:
        bin4.append(item)
    elif sig_dig == 5:
        bin5.append(item)
    elif sig_dig == 6:
        bin6.append(item)
    elif sig_dig == 7:
        bin7.append(item)
    elif sig_dig == 8:
        bin8.append(item)
    elif sig_dig == 9:
        bin9.append(item)


def put_main(input_list, result):
    '''(list, list) -> NoneType
    Move things from bin0 -9 to main in ascending order.
    '''
    while input_list != []:
        item = input_list.pop(0)
        result.append(item)
    return result


def radix_sort(input_list, level=1, max_len=-1, main=[]):
    '''(list) -> list
    return a sorted list from min to max.

    '''
    max_len = len(str(max(input_list)))
    if level <= max_len:
        # loop throught the entire list
        main = input_list[:]
        while main != []:
            place_bin(main[0], level)
            main.pop(0)

        main = put_main(bin0, main)
        main = put_main(bin1, main)
        main = put_main(bin2, main)
        main = put_main(bin3, main)
        main = put_main(bin4, main)
        main = put_main(bin5, main)
        main = put_main(bin6, main)
        main = put_main(bin7, main)
        main = put_main(bin8, main)
        main = put_main(bin9, main)
        main = radix_sort(main, level + 1, max_len, main)
    return main

