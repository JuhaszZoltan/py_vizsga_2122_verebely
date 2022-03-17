from math import sqrt

def f1():
    n:int = pow(int(input(f'\tÍrj be egy számot: ')), 2)
    s:str = input(f'\tÍrj be egy szöveget: ').lower() + ' '
    print(f'\tOP: {n * s}')


def f2():
    a:float = float(input('\tadd meg az [a] értékét: '))
    b:float = float(input('\tadd meg az [b] értékét: '))
    c:float = float(input('\tadd meg az [c] értékét: '))
    if a+b>c and a+c>b and b+c>a:
        print('\tlétezhet háromszög ilyen oldalhosszokkal')
        if (a*a + b*b) == c*c or (a*a + c*c) == b*b or (b*b + c*c) == a*a:
            print('\tez a háromszög derékszögű')
        else:
            print('\tez a háromszög NEM derékszögű')
        if a==b or a==c or b==c:
            print('\tez a háromszög egyenlő szárú')
        else:
            print('\tez a háromszög NEM egyenlő szárú')
        k = a + b + c
        s = k / 2
        t = sqrt(s*(s-a)*(s-b)*(s-c))
        print(f'\ta háromszög kerülete: {k} cm')
        print(f'\ta háromszög területe: {t} cm^2')
    else:
        print('\tnem létezik olyan háromszög, melynek ezek volnának az oldalhosszai!')


class Bolygo:
    def __init__(self, r:str):
        v = r.strip().split(';')
        self.nev:str = v[0]
        self.holdak:int = int(v[1])
        self.terfogat:float = float(v[2])


def f3_0(f:str, e:str):
    bs:list[Bolygo] = []
    for r in open(file=f, encoding=e):
        bs.append(Bolygo(r))
    return bs


def f3_2(bs:list[Bolygo]):
    sum = 0
    for b in bs:
        sum += b.holdak
    return sum / len(bs)


def f3_3(bs:list[Bolygo]):
    m = 0
    for i in range(1, len(bs)):
        if bs[i].terfogat > bs[m].terfogat:
            m = i
    return bs[m].nev


def f3_4(bs:list[Bolygo], k:str):
    for b in bs:
        if b.nev.lower() == k.lower():
            return True
    return False


def f3_5(bs:list[Bolygo], k:int):
    ns:list[str] = []
    for b in bs:
        if b.holdak > k:
            ns.append(b.nev)
    return ns