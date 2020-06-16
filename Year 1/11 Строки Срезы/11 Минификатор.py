for _ in range(int(input())):
    inp = input()
    new_inp = ""
    startF = True  # Флаг начальных пробелов
    pFlag = False  # Флаг пробелов в строке
    qFlag = False  # Флаг кавычек
    for i in range(len(inp)):
        if startF and inp[i] != ' ':
            startF = False
        elif startF:
            new_inp += inp[i]
            continue

        if inp[i] == "'" and not qFlag:
            qFlag = True
            new_inp += inp[i]
            continue

        if inp[i] == "'" and qFlag and (inp[i - 1] != '\\' or
                                        (inp[i - 1] == '\\' and inp[i - 2] == '\\')):
            qFlag = False

        if qFlag:
            pass
        else:
            if inp[i] == ' ':
                if not pFlag:
                    pFlag = True
                    new_inp += inp[i]
                    continue
                continue
            elif pFlag and inp[i] != ' ':
                pFlag = False
            if inp[i] == '#':
                break
        new_inp += inp[i]

    print(new_inp)
