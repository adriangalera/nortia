from nortia.repo import write_now_in, write_now_out


def listen_input_events(filename):
    while True:
        input_str = input("IN/OUT: ")
        if "IN" in input_str:
            print("IN")
            write_now_in(filename)
        if "OUT" in input_str:
            print("OUT")
            write_now_out(filename)
