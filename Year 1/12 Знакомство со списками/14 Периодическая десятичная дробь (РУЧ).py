number = int(input())
st, period, x = [], [], 1

while x not in st:
    st.append(x)
    period.append((10 * x) // number)
    x = (10 * x) % number

for num in period[st.index(x):]:
    print(num, end="")
