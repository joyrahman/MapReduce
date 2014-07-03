#!/python 

import json

word_data = {
    "words": 0,
    "wordlist": {}
}

with open('/dev/input', 'r') as f:
    for line in f.xreadlines():
        for word in [w.lower().strip('\t ,.!\'') for w in line.split()]:
                word_data['words'] += 1
                word_data['wordlist'][word] = word_data['wordlist'].get(word, 0) + 1

toplist = dict(sorted(word_data['wordlist'].items(), key=lambda(k,v): v, reverse=True)[:200])
word_data['wordlist'] = toplist

with open('/dev/out/wordcount-reducer', 'w') as f:
    f.write(json.dumps(word_data, encoding="latin_1"))
