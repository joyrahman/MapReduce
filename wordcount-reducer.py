#!/python

import os
import json

total_stats = {
    "books": 0,
    "words": 0,
    "wordlist": {}
}

count = 0
for filename in os.listdir('/dev/in'):
    with open(os.path.join('/dev/in', filename), 'r') as f:
        stats = json.loads(f.read())

    total_stats['words'] += stats['words']
    total_stats['books'] += 1
    
    for word in stats['wordlist'].keys():
        total_stats['wordlist'][word] = total_stats['wordlist'].get(word, 0) + stats['wordlist'][word]

print 'Total books: %d' % total_stats['books']
print 'Total words: %d' % total_stats['words']

for wordpair in sorted(total_stats['wordlist'].items(), key=lambda(k,v): v, reverse=True)[:100]:
    print '%7d %s' % (int(wordpair[1]), wordpair[0])
