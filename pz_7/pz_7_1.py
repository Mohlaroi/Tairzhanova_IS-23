#Дан символ С и строки S, S0.
# После каждого вхождения символа С
# в строку S вставить строку S0.
def change(letters, char, chan):
    return letters.replace(char, chan)
letters = 'купила КК, чтобы выпить КК с друзьями'
find = 'КК'
insert = 'Кока-колу'

res = change(letters, find, insert)
print(letters,'\n', res)