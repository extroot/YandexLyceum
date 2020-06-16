def who_are_you_and_hello():
    while True:
        text = input()
        if text.istitle() and text.isalpha():
            print(f"Привет, {text}!")
            break


if __name__ == "__main__":
    who_are_you_and_hello()
