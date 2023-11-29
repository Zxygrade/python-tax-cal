contacts ={
    'number':4,
    'students':
    [
        {"name":'Sarah', 'email':'sarah@email.com'},
        {"name":'Harry', 'email':'harry@email.com'},
        {"name":'Herm', 'email':'herm@email.com'},
        {"name":'Ron', 'email':'ron@email.com'}
       
        ]
}

print('Student emails:')
for student in contacts['students']:
    print(student['email'])