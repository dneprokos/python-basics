# TODO: Convert code_in_c_sharp.cs to Python

def main():
    print("RunningTally(tm)")
    print("Enter a number to start the tally, enter 'quit' to stop")

    run = True
    total = 0

    try:
        while run:
            name = input("Enter a number: ")
            if name == "quit":
                run = False
            else:
                total += int(name)
                print(f"Running total: {total}")
    except ValueError:
        print("Please enter a number or 'quit' to stop")