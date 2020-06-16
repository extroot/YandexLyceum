def bracket_check(text):
    st = []
    for x in text:
        if x == "(":
            st.append(1)
        else:
            if len(st) == 0:
                print("NO")
                return
            st.pop(-1)
    if len(st) == 0:
        print("YES")
    else:
        print("NO")


if __name__ == "__main__":
    bracket_check(input())
