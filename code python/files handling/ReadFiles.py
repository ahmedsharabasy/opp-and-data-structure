myfile=open("C:\\Users\\ahmed\\OneDrive - Damietta University\\Desktop\\code python\\files handling\\readfiles.txt","r")

print(myfile)      #file date cbject  بيانات الفايل
print(myfile.name)
print(myfile.mode)
print(myfile.encoding)

print("*"*50)

print(myfile.read())   #تقرا محتويات الملف ولو مفيش الديفلت بتاعه -1
print(myfile.read(5)) 

print("*"*50)

#print(myfile.readline(5))   #يقرا اول خمس حروف


# for line in myfile:
#     print(line)
#     if line.startswith("y"):
#         break

# myfile.close()    