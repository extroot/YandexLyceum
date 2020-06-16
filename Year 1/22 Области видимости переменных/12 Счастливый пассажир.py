def lucky(ticket):
    global lastTicket
    ticket = str(ticket).rjust(6, '0')
    return "Счастливый" if sum([int(i) for
                                i in ticket[:3]]) == sum([int(i)
                                                          for i in ticket[3:]]) and sum(
        [int(i) for i in str(lastTicket)[:3]]) == sum([int(i) for i in str(lastTicket)[3:]])\
        else "Несчастливый"
