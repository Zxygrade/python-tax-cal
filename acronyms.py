acronyms = ['SMH'];
word ="BFN";

acronyms.append('LOL');
acronyms.append('IDK');
acronyms.append('LMAO');
acronyms.remove('LMAO');
acronyms.append('TBH')
if word in acronyms:
    print(word +' is in the list');
else:
    print(word +' is NOT in the list');
#print(acronyms)
for acronym in acronyms:
    print(acronym);