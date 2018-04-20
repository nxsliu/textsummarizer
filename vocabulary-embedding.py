FN = 'vocabulary-embedding'
seed  = 42
vocab_size = 40000
embedding_dim = 100
lower = False

import pickle as pkl
FN0 = 'tokens'
with open('data/%s.pkl'%FN0, 'rb') as fp:
    heads, desc = pkl.load(fp)

if lower:
    heads = [h.lower() for h in heads]

if lower:
    desc = [h.lower() for h in desc]

i=0
print(heads[i])
print(desc[i])
print(len(heads), len(set(heads)))
print(len(desc), len(set(desc)))

from collections import Counter
from itertools import chain

def get_vocab(lst):
    vocabcount = Counter(w for txt in lst for w in txt.split())
    vocab = list(map(lambda x: x[0], sorted(vocabcount.items(), key=lambda x: -x[1])))
    return vocab, vocabcount

vocab, vocabcount = get_vocab(heads+desc)

# print(vocab[:50])
# print('...',len(vocab))

# import matplotlib.pyplot as plt
# #%matplotlib inline
# plt.plot([vocabcount[w] for w in vocab])
# plt.gca().set_xscale("log", nonposx='clip')
# plt.gca().set_yscale("log", nonposy='clip')
# plt.title('word distribution in headlines and discription')
# plt.xlabel('rank')
# plt.ylabel('total appearances')
# plt.show()

empty = 0
eos = 1
start_idx = eos + 1

def get_idx(vocab, vocabcount):
    word2idx = dict((word, idx+start_idx) for idx, word in enumerate(vocab))
    word2idx['<empty>'] = empty
    word2idx['<eos>'] = eos

    idx2word = dict((idx, word) for word, idx in word2idx.items())

    return word2idx, idx2word

word2idx, idx2word = get_idx(vocab, vocabcount)

#print(word2idx, idx2word)

fname = 'glove.6B.%dd.txt'%embedding_dim
import os
datadir_base = os.path.expanduser(os.path.join('~', '.keras'))
if not os.access(datadir_base, os.W_OK):
    datadir_base = os.path.join('/tmp', '.keras')

datadir = os.path.join(datadir_base, 'datasets')
glove_name = os.path.join(datadir, fname)

if not os.path.exists(glove_name):
    path = 'glove.6B.zip'
    path = get_file(path, origin="http://nlp.stanford.edu/data/glove.6B.zip")
    unzip {datadir}/{path}

glove_n_symbols = !wc -1 {glove_name}
glove_n_symbols = int(glove_n_symbols[0].split()[0])
print(glove_n_symbols)