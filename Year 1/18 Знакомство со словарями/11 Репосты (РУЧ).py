st = {}
n = int(input()) - 1

inp = input().split(' ')
st[inp[0]] = {'count': int(inp[-1]), 'from': '&&'}
for _ in range(n):
    inp = input().split(' ')
    count, at = int(inp[-1]), inp[4][:-1]
    st[inp[0]] = {'count': count, 'from': at}
    while at != '&&':
        st[at]["count"] += count
        at = st[at]["from"]
for x in st.items():
    print(x[1]["count"])
