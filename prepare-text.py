from os import listdir
from os.path import isfile, join
contentfiles = [f for f in listdir('data/bbc-fulltext/bbc/business') if isfile(join('data/bbc-fulltext/bbc/business', f))]

heads = []
for contentfile in contentfiles:
    with open('data/bbc-fulltext/bbc/business/%s'%contentfile) as f:
        contentraw = f.readlines();        
        heads.append(contentraw)

print(len(heads))


# with open('data/bbc-fulltext/bbc/business/001.txt') as f:
#     content = f.readlines()

# content = [x.strip() for x in content]
# head = content[0]
# desc = ''.join(content[2:len(content)])

# print('-----------head tokens-----------')
# headtokens = ''.join((' {} '.format(el) if el in '[`\-=~!@#$%^&*()_+\[\]\{\};\'\\:"|<,./<>?£]' else el for el in head))
# print(headtokens)

# print('----------- desc tokens -----------')

# desctokens = ''.join((' {} '.format(el) if el in '[`\-=~!@#$%^&*()_+\[\]\{\};\'\\:"|<,./<>?£]' else el for el in desc))
# print(desctokens)

# print(content[0])  

# for x in range(2, len(content)):
#     print(content[x])