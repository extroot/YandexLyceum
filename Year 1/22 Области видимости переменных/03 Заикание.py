last = ""


def print_without_duplicates(message):
    global last
    if message != last:
        print(message)
        last = message
