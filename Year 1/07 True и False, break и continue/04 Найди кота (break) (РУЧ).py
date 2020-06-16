s = False

for i in range(int(input())):
    inp = input()
    if 'кот' in inp or 'Кот' in inp:
        print("МЯУ")
        break
else:
    print("НЕТ")
