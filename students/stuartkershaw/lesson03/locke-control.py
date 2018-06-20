#!/usr/bin/env python3


from locke import Locke


def apply_selection(selection):
    arg_dict = {
        '1': enter_num_boats,
        '2': quit
    }
    try:
        if not arg_dict.get(selection):
            raise KeyError
        arg_dict.get(selection)()
    except KeyError:
        print('Oops, invalid selection.')


def locke_interface():
    options = 'Please select from the menu:\n'\
              '1) set number of boats for passage\n'\
              '2) quit\n'
    while True:
        selection = input(options)
        apply_selection(selection)


def enter_num_boats():
    while True:
        try:
            num_boats = int(input('Please enter the number of boats to enter: '))
            if not num_boats > 0:
                raise ValueError
        except ValueError:
            print('Please provide a whole number greater than zero.')
        else:
            # gate_size = 'SMALL' if num_boats <= 5 else 'LARGE'
            small_locke = Locke(5)
            large_locke = Locke(10)
            print('{} boats granted for entry.'.format(num_boats))
            # print('Opening {} gates.'.format(gate_size))
            break


def main():
    locke_interface()


if __name__ == "__main__":
    main()
