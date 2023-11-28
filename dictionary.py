acronyms ={'LOL':'Laugh out loud'}

print(acronyms)
acronyms['TBH'] = 'to be honest'

acronyms['IDK'] = 'I dont know'

print(acronyms)

acronyms['LMK'] = 'let me know'

print(acronyms['LMK'])

definition = acronyms.get('BTW')

print(definition)

acronyms['TBH'] = 'honestly'

print(acronyms['TBH'])

if definition:
    print(definition)
else:
    print("Key doesn't exist")

sentence = 'IDK' +' what happened ' + 'TBH'
translation = acronyms.get("IDK") + ' what happened ' + acronyms.get('TBH')
print('sentence:', sentence)
print('translation:', translation)