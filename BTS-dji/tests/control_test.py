from BTS_dji import controler  # import kbd

controler.start()  # start the keyboard listener

while True:
    input = controler.get_state(0)  # get the state of the keyboard
    print(input["a"])  # print the state of the "a" key
