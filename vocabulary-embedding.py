FN = 'vocabulary-embedding'
seed  = 42
vocab_size = 40000
embedding_dim = 100
lower = False

import pickle as pkl
FN0 = 'tokens'
with open('data/%s.pkl'%FN0, 'rb') as fp:
    heads, desc, keywords = pkl.load(fp)

if lower:
    heads = [h.lower() for h in heads]

if lower:
    desc = [h.lower() for h in desc]

i=0
heads[i]