import mymodule
mymodule.sayhi('Pin')

name = mymodule.person['name']
age = mymodule.person['age']
country = mymodule.person['country']

print('name: ', name)

for x,y in mymodule.person.items():
    print(x," : ",y)

import json 

y = json.loads(mymodule.x)
print(y['city'])
