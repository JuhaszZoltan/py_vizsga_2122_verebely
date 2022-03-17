from module import f1, f2, f3_0, f3_2, f3_3, f3_4, f3_5

print('1. feladat:')
f1()
print('2. feladat:')
f2()
print('3. feladat:')
bs = f3_0('solsys.txt', 'utf-8')
print(f'\t3.1: {len(bs)} bolygó van a naprendszerben')
print(f'\t3.2: a naprendszerben egy bolygónak átlagosan {f3_2(bs)} holdja van')
print(f'\t3.3: a legnagyobb térfogatú bolygó a {f3_3(bs)}')
kn = input(f'\t3.4: írd be a keresett bolygó nevét: ')
if f3_4(bs, kn):
    print('\t\tvan ilyen nevű bolygó a naprendszerben')
else:
    print('\t\tsajnos nincs ilyen nevű bolygó a naprendszerben')
ksz = int(input(f'\t3.5 Írj be egy egész számot: '))
print(f'\t\ta következő bolygóknak van {ksz}-nál/nél több holdja:')
print(f'\t\t{f3_5(bs, ksz)}')
