st = []


def print_only_new(text):
    if text not in st:
        st.append(text)
        print(text)
