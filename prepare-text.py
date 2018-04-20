from os import listdir
from os.path import isfile, join
import pickle

contentfiles = [f for f in listdir('data/bbc-fulltext/bbc/business') if isfile(join('data/bbc-fulltext/bbc/business', f))]

heads = []
descs = []
for contentfile in contentfiles:
    with open('data/bbc-fulltext/bbc/business/%s'%contentfile) as f:
        contentraw = f.readlines()
        contentraw = [x.strip() for x in contentraw]
        contenttokens = [''.join((' {} '.format(el) if el in '[`\=~!@#$%^&*()_+\[\]\{\};\'\\:"|<,./<>?£]' else el for el in c)) for c in contentraw]        
        heads.append(contenttokens[0])
        descs.append(''.join(contenttokens[2:len(contenttokens)]))

# print('-----------head tokens-----------')
# print(heads)
# print('----------- desc tokens -----------')
# print(descs)

with open("data/tokens.pkl", "wb") as f:
    pickle.dump((heads,descs), f)

# pickle.dump(heads, open('data/tokens.pkl', 'wb'))
# pickle.dump(descs, open('data/tokens.pkl', 'wb'))

# print(pickle.load(open('data/tokens.pkl', 'rb')))
# pickle.load(open('data/tokens.pkl', 'wb'))

