

#                                           لازم اذاكرهم بالترتيب

#writemode     ينشئ الملف لو الملف مش موجود 
             #2-محتوى الملف بيشيله ويكتب الكلام الى انا اعطيتهوله
# myfile=open("C:\\Users\\ahmed\\OneDrive - Damietta University\\Desktop\code python\\files handling\\writefile.txt","w")
# myfile.write("zzzzzzzzzzzzzzzzzzzzz\n")
# myfile.write("zzzzzzzzzzzzzzzzzzzzzmmmmmmmmmmmmmmmmm")



# file=open(r"C:\Users\ahmed\OneDrive - Damietta University\Desktop\code python\files handling\sasi.txt","w")
# file.write("ahmed khaled\n"*20)


# mylist=["scad","ascv","scav"]
# mylist=open("C:\\Users\\ahmed\\OneDrive - Damietta University\\Desktop\\code python\\files handling\\sasi.txt","w")
# mylist.writelines(mylist)`    `




#(  append   ) بيكمل على القديم
# file=open("C:\\Users\\ahmed\\OneDrive - Damietta University\\Desktop\\code python\\files handling\\sasi.txt","a")
# file.write("ahmed khaled\n"*10)
# file.write("new line*****\n")



# ffile=open("C:\\Users\\ahmed\\OneDrive - Damietta University\\Desktop\\code python\\files handling\\truncate.txt","w")     #(1)
# ffile.write("mostafa mahmoud\nabdalla elshirif")
# hfile=open("C:\\Users\\ahmed\\OneDrive - Damietta University\\Desktop\\code python\\files handling\\truncate.txt","a")     #(2)
# hfile.truncate(5)
#                                                                                                                            #(1),(2)مينفعوش مع بعض فى وقت واحد

# hfile=open("C:\\Users\\ahmed\\OneDrive - Damietta University\\Desktop\\code python\\files handling\\truncate.txt","a") 
# print(hfile.tell())     #tell()  تحسب مكان اخر حرف والنزول سطر بيحسب بمكانين



hfile=open("C:\\Users\\ahmed\\OneDrive - Damietta University\\Desktop\\code python\\files handling\\truncate.txt","r")
hfile.seek(5)                #بيعرض الى من بعد الانديكس5          
print(hfile.read()) 


import os 
so.remove("مسار الملف الى عايز احذفه هيتحذف الملف")