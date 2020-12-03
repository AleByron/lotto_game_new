import argparse
from lotto.ticket import ticket
from lotto.check_num_to_bill import check_num_to_bill
from lotto.lotto_printer import lotto_printer

def main():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument("-n", "-number", type=int, help="Number of tickets to generate", choices=[0, 1, 2, 3, 4, 5])
    args = parser.parse_args()
    n_ticket = args.n
    while True:


        if n_ticket == None:
            print('You should enter at least a single  bill for a ticket')
            break
        elif n_ticket == 0:
            print('See you next time')
            quit()
        elif n_ticket > 5:
            print('You can enter a maximum of 5 bills for a ticket')
            break
        elif n_ticket < 1:
            print('You should enter at least a single  bill for a ticket')
            break

        counter = 0
        while counter < n_ticket:
            lotto_ticket = ticket()
            bill_type = lotto_ticket.bill_type_ob()
            bill_num = lotto_ticket.bill_num_ob()
            check_num_bill = check_num_to_bill.check_num_to_bill_m(bill_num[0],bill_type)

            if check_num_bill == True:
                pass
            else:
                bill_num = lotto_ticket.bill_num_ob()

            bill_city = lotto_ticket.bill_city()
            print(bill_type, bill_num[1], bill_city)
            lotto_printer.printer(bill_type, bill_city, bill_num[1])
            counter = counter +1

        while True:
            play_again = input('Do you want to play again?(y/n): ')
            play_again = play_again.lower()
            if play_again == 'y':
                n_ticket = int(input("How many ticket you want to play?"))
                break
            elif play_again == 'n':
                n_ticket = 0
                break




if __name__ == "__main__":
        main()


