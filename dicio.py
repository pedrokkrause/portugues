import unidecode

s='AÁÀÂÃÄaáàâãäBbCÇcçDdEÉÈÊËeéèêëFfGgğĞHhIÍÌÎÏiíìîïJjKkLlMmNnOÓÒÔÖÕoóòôöõPpQqRrSsşŞTtUÚÙÛÜuúùûüVvWwXxYyZz'
s2=unidecode.unidecode(s)
trans = str.maketrans(s, s2)

def unikey(seq):
    return seq[0].translate(trans)


palavras = []
with open("palavras.txt") as file:
    for line in file:
        palavras.append(line.rstrip())
with open("br-utf8.txt") as file:
    for line in file:
        palavras.append(line.rstrip())
palavras = list(set(palavras))
palavras = sorted(palavras, key=unikey)
print(len(palavras))
with open('portuguescompleto.txt', 'w') as f:
    for item in palavras:
        f.write("%s\n" % item)

palavras = []
with open("palavras.txt") as file:
    for line in file:
        palavras.append(unidecode.unidecode(line.rstrip()))
with open("br-utf8.txt") as file:
    for line in file:
        palavras.append(unidecode.unidecode(line.rstrip()))
palavras = list(set(palavras))
palavras.sort()
print(len(palavras))
with open('portuguescompletoSemAcento.txt', 'w') as f:
    for item in palavras:
        f.write("%s\n" % item)