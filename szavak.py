bekert_szo = input('1. feladat: Adjon meg egy szót: ')
van = False
mgh = 'aeiou'

for letter in bekert_szo:
    if letter in mgh and not van:
        print('van benne maganhangzo')
        van = True
if not van:
    print('nics benne maganhangzo')

words = []
with open('szoveg.txt') as file:
    for word in file:
        words.append(word.strip('\n'))

hossz = 0
hely = 0
for index, word in enumerate(words):
    if len(word) > hossz:
        hossz = len(word)
        hely = index
    
print(f'2. feladat:')
print(f'{words[hely]} {hossz}')

oh = []
for word in words:
    cout = 0
    for letter in word:
        if letter in mgh:
            cout += 1
        else:
            cout -= 1
    if cout > 0:
        oh.append(word)

print('3. feladat:')
print(' '.join(oh))
print(f'{len(oh)}/{len(words)}: {len(oh) / len(words):.2f}%')

tre_char = input('4. feladat: Adjon meg egy szoreszletet: ')
fem_char = []
for word in words:
    if len(word) == 5:
        fem_char.append(word)

bra_orden = []
with open('letra.txt', 'w', encoding = 'utf-8') as letra:
    for word in fem_char:
        if tre_char in word[1:4]:
            bra_orden.append(word)
    for word in bra_orden:
        if len(bra_orden) > 1:
            print(word, file=letra)

