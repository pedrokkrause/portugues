# Todas as Palavras da Língua Portuguesa
A partir das palavras disponibilizadas em:
- https://github.com/pythonprobr/palavras 
- https://www.ime.usp.br/~pf/dicios/index.html
- https://github.com/AlfredoFilho/Palavras_PT-BR
- https://github.com/fserb/pt-br
- https://natura.di.uminho.pt/download/sources/Dictionaries/wordlists/LATEST/

E também das palavras do Wikcionário, disponíveis em https://kaikki.org/dictionary/rawdata.html, filtradas conforme o seguinte código:
```python
import json
import string

allowed_characters = frozenset(string.ascii_letters + '-')
vogals = frozenset('aeiou')

with open("portugues/pt-extract.jsonl", encoding="utf-8") as f, open('portugues/wikcionario.txt','w', encoding="utf-8") as g:
    for i,line in enumerate(f):
        data = json.loads(line)
        if data.get('lang') == "Português":
            word = data['word']
            chars = frozenset(word)
            if ' ' not in word and not word.startswith('-') and not word.endswith('-') and not chars.difference(allowed_characters) and len(vogals.difference(word)) != 5:
                g.write(word+'\n')
```

Todas foram combinadas em um arquivo com cerca de 2.078.076 termos e 25MB, com repetições removidas e sem acentuações.

Apesar do título de caráter apelativo, é preciso observar que muitos dos termos contidos no arquivo são questionáveis, isto é, muitos dificilmente podem ser verdadeiramente considerados palavras. Nesse sentido, espera-se com esse trazer não um dicionário, vocabulário, ou similar, mas sim provavelmente uma coleção de todos os termos concebíveis de uso durante a comunicação em português.
