#map
#predefined function

def formatedtext(text):
    return f"  {text.strip().capitalize()}  "

mytexts=['ankc','  aved','ehhjf']

#print(map(formatedtext,mytexts))

for name in map(formatedtext,mytexts):
    print(name)

print("***************************")
#lambda function   بدل ماعمل فانكشن جديده 

mytexts=['kucgcgk','  jjjj','kkkkk']
for name in map( lambda text:f"  {text.strip().capitalize()}  " ,mytexts):
    print(name)


