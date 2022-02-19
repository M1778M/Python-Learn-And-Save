def randstr(tool:int):
    from random import randint as rnd
    out = ''
    this = 'abcdefgijklmnopqrstuvwxyz'
    this_ = list(this)
    for i in range(tool):
        for c in this_[rnd(0,26):]:
            out += str(c)
    return out[tool:]


while True:
    get = input("?.>RandomString:>interInt-/")
    try:
        print(randstr(int(get)))
    except Exception:
        raise ValueError

