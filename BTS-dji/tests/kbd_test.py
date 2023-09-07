from BTS_dji import kbd  # import kbd

kbd.start()  # start the keyboard listener

while True:
    input = kbd.get_state(0)  # get the state of the keyboard
    print(input["a"])  # print the state of the "a" key
