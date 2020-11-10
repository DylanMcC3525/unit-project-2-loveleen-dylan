import sqlite3

<<<<<<< HEAD
=======
con = sqlite3.connect("RESERVME.db")

cur = con.cursor()

cur.execute("SELECT * FROM UserInformation")
print(cur.fetchall())


def input_number_check(prompt: str) -> int:
    while True:
        response = input(prompt)
        if response.isdigit():
            response = int(response)
            if response >= 0:
                return response
        print("Please provide a valid input.")

>>>>>>> 49be050294a7d839bdbe7ef1880ad1f7402f5a71

print(
    """
    
                                RESERVEME
                  . .                     -:-             .  .  .
            .'.:,'.        .  .  .     ' .           . \ | / .
            .'.;.`.       ._. ! ._.       \          .__\:/__.
             `,:.'         ._\!/_.                     .';`.      . ' .
             ,'             . ! .        ,.,      ..======..       .:.
            ,                 .         ._!_.     ||::: : | .        ',
     .====.,                  .           ;  .~.===: : : :|   ..===.
     |.::'||      .=====.,    ..=======.~,   |"|: :|::::::|   ||:::|=====|
  ___| :::|!__.,  |:::::|!_,   |: :: ::|"|l_l|"|:: |:;;:::|___!| ::|: : :|
 |: :|::: |:: |!__|; :: |: |===::: :: :|"||_||"| : |: :: :|: : |:: |:::::|
 |:::| _::|: :|:::|:===:|::|:::|:===F=:|"!/|\!"|:::|:====:|::_:|: :|::__:|
 !_[]![_]_!_[]![]_!_[__]![]![_]![_][I_]!//_:_\\![]I![_][_]!_[_]![]_!_[__]!
 -----------------------------------"---''''```---"-----------------------
 _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ |= _ _:_ _ =| _ _ _ _ _ _ _ _ _ _ _ _
                                     |=    :    =|                      
_____________________________________L___________J________________________
--------------------------------------------------------------------------


"""
)

print(
    """
WELCOME TO ReservME WHERE YOU RESERVE FOR A ME! 

We are delighted to have you here with us today.

Let's get started!
"""
)
print("We have 5 types of rooms.")
print("\n" + "\033[1m" + "Studio Suite: ")
print(
    "\033[0m"
    + "Featuring a plush bed and living space with extra seating, a sleeper sofa, and a TV that can be seen from every angle of the suite. Each studio suite includes a workstation, a wet bar, a refrigerator, and a microwave."
)
print("$149")
print("\n\n" + "\033[1m" + "One-Bedroom Suite: ")
print(
    "\033[0m"
    + "Including a separate living room with sleeper sofa and a bedroom with a TV in both spaces. Each one-bedroom suite features a workstation, a wet bar, a refrigerator, and a microwave."
)
print("$99")
print("\n\n" + "\033[1m" + "Two-Bedroom Suite: ")
print(
    "\033[0m"
    + "Spread out in the separate living room with sleeper sofa and two bedrooms with a TV in all three spaces. Each two-bedroom suite includes a workstation, a wet bar, a refrigerator, and a microwave."
)
print("$154")
print("\n\n" + "\033[1m" + "Presidential Suite: ")
print(
    "\033[0m"
    + "Experience even more space and comfort in our Presidential Suite. Some hotels’ Presidential Suites feature an espresso machine, fireplace, a luxury bathroom feature like whirlpool tubs, or a conference table with seating for up to eight."
)
print("$259")
print("\n\n" + "\033[1m" + "Premium Suite: ")
print(
    "\033[0m"
    + "Offering the same experience as our popular one-bedroom suites, Premium Suites include additional upgrades of Premium WiFi, a Keurig coffee brewer, plus snacks and drinks which are replenished daily."
)
print("$324")


ROOMS = [
    "studio suite",
    "one-bedroom suite",
    "two-bedroom suite",
    "presidential suite",
    "premium suite",
]

PRICES = [99, 149, 154, 259, 324]


def avaliable_rooms_func():
    avaliable_rooms = input(
        "Would you like to see the avaliable rooms? [Y/N]: "
    ).lower()
    if avaliable_rooms == "y":
        cur.execute("SELECT * FROM RoomsAvailability")
        print(cur.fetchall())

    elif avaliable_rooms == "n":
        pass
    else:
        print("Invalid Input")
        avaliable_rooms_func()


avaliable_rooms_func()
room_type = input("\n" + "What type of room would you like to reserve today?: ")
input_room_type = room_type.lower()
for i in ROOMS:
    if input_room_type not in ROOMS:
        print("That room does not exist. Please try again.")
        room_type = input("\n" + "What type of room would you like to reserve today?: ")

i = ROOMS.index(input_room_type)
price = PRICES[i]


<<<<<<< HEAD
cur = con.cursor()

print("Great. Before you can reserve a hotel room we need some information.")


print(full_name, room_type, price)

cur.execute(
    "INSERT INTO UserInformation(full_name, address, email, zipcode, state, phoneNumber) VALUES(?,?,?,?,?,?)",
    (full_name, address, email, zip_code, state, phone_number),
)
cur.execute("SELECT * FROM UserInformation")
con.commit()
print(cur.fetchall())
cur.execute(
    "INSERT INTO RoomsAvailability(room_type, price, size, guest) VALUES (?, ?, ?, ?)", (input_room_type, price, number_guests, full_name)
)

=======
cur.execute("SELECT * FROM UserInformation")
print(cur.fetchall())
con.commit()
con.close()
>>>>>>> 49be050294a7d839bdbe7ef1880ad1f7402f5a71
