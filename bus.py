def available_bus():
    first_bus = "First bus : from Rafah to Gaza"
    Sacand_bus = "Sacand bus: from Rafah to khanyounes"
    third_bus = "Third bus : from Rafah to DerAlbalah"
    fourth_bus = "Fourth bus : from Rafah to Shjaeea"
    fifth_bus = "Fifth bus : from Rafah to Bethannon"
    print(" For Today There is 5 Buses :-")
    print(first_bus)
    print(Sacand_bus)
    print(third_bus)
    print(fourth_bus)
    print(fifth_bus)

def info():

 print(" in First bus(Rafah-Gaza) : the available seats is 3 and a free seats is 1")
 print(" in Sacand bus(Rafah- khanyounes) : the available seats is 5  and a free seats is 3")
 print(" in Third bus(Rafah- DerAlbalah) : the available seats is 2  and a free seats is 1")
 print(" in Fourth bus(Rafah-Shjaeea) : the available seats is 1  and a free seats is 1")
 print(" in Fifth bus(Rafah-Bethannon) : the available seats is 3 and a free seats is 1")
def reservation():
     number_bus = int(input("Enter the Bus Number: "))
     if number_bus == 1:
            seat_1 = "The Third seat is on the left next to the window And the seat number is (14) "
            seat_2 = "The Fourth seat is on the left next to the window And the seat number is (18) "
            seat_3 = "The Fifth seat is on the left next to the window And the seat number is (22)"
            seat_4 = "The seat is free and a seat is in the last of bus and the number is (60)"
            print("the available seats is 3 and a free seats is 1:-" )
            print(seat_1)
            print(seat_2)
            print(seat_3)
            print(seat_4)
            book= int(input("Which seat would you like to book? :"))
            print("Successfully booked")
     elif number_bus == 2:
         seat_1 = "The Third seat is on the left next to the window And the seat number is (14) "
         seat_2 = "The Fourth seat is on the left next to the window And the seat number is (18) "
         seat_3 = "The Fifth seat is on the left next to the window And the seat number is (22)"
         seat_4 = "The sixth  is on the left next to the window And the seat number is (26)"
         seat_5 = "The seventh seat is on the left next to the window And the seat number is (30) "
         seat_6 = " The seat is free and a seat is in the last of bus And the seat number is (58) "
         seat_7 = "The seat is free and a seat is in the last of bus And the seat number is (59)"
         seat_8 = "The seat is free and a seat is in the last of bus And the seat number is (60)"
         print("the available seats is 5 and a free seats is 3 :-")
         print(seat_1)
         print(seat_2)
         print(seat_3)
         print(seat_4)
         print(seat_5)
         print(seat_6)
         print(seat_7)
         print(seat_8)
         book = int(input("Which seat would you like to book? :"))
         print("Successfully booked")
     elif number_bus == 3:
         seat_1 = "The Fourth seat is on the left next to the window And the seat number is (18) "
         seat_2 = "The Fifth seat is on the left next to the window And the seat number is (22)"
         seat_3= "The seat is free and a seat is in the last of bus and the number is (60)"
         print("the available seats is 2 and a free seats is 1 :-")
         print(seat_1)
         print(seat_2)
         print(seat_3)
         book = int(input("Which seat would you like to book? :"))
         print("Successfully booked")
     elif number_bus == 4:
         seat_1 = "The Fifth seat is on the left next to the window And the seat number is (22)"
         seat_2 = "The seat is free and a seat is in the last of bus and the number is (60)"
         print("the available seats is 1 and a free seats is 1 :-")
         print(seat_1)
         print(seat_2)
         book = int(input("Which seat would you like to book? :"))
         print("Successfully booked")
     elif number_bus == 5:
         seat_1 = "The Third seat is on the left next to the window And the seat number is (14) "
         seat_2 = "The Fourth seat is on the left next to the window And the seat number is (18) "
         seat_3 = "The Fifth seat is on the left next to the window And the seat number is (22)"
         seat_4 = "The seat is free and a seat is in the last of bus and the number is (60)"
         print("the available seats is 3 and a free seats is 1:-")
         print(seat_1)
         print(seat_2)
         print(seat_3)
         print(seat_4)
         book = int(input("Which seat would you like to book? :"))
         print("Successfully booked")


def welcome():
    print("Welcome ")
    print("We serve at many cities inside Gaza Strip")
    i= int(input("log in or sing up? enter 1 for log in or 0 for sing up :"))
    if i == 1 :
      user = str(input("Enter UserName : "))
      passw = int(input("Enter Password :"))
      print(" welcome back")
    else:
        user = str(input("Enter UserName : "))
        passw = int(input("Enter Password :"))
        conpass = int(input("Enter Password :"))
        if conpass == passw :
         print("successfully registered")
        else:
              print("Please match the password")



def main():
        print("1.Buses Available")
        print("2.Information For State")
        print("3.Reservation")
        print()
        print("Enter your choice: ")
        choice = int(input())


        if(choice == 1):
          available_bus()

        elif (choice == 2):
            info()

        elif (choice == 3):
            reservation()


        else:
            print("Please enter a valid choice")


if __name__ == "__main__":
    welcome()
    main()