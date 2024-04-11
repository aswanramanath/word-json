# import docx
# import json


# k=open('python.doc',"r")

# r=k.strip()


    



# f=open(r"word.json","w") 
# f.write(r)


# file_path = 'python.doc'  
# f2= 'word.json'


# k=open(file_path, 'r') 
# for line in k:
        
#     y=line.strip()
#     print(y)
# f=open('word.json',"w")
# f.writelines(y)

    

import json
import docx

def convert(file_path, json_file):
 
  

#  if file_path!=docx:
#     print("please enter correct formatte")
#  else:
    k=open(file_path, 'r') 
    d= k.read()

    data = {
        "dect":d
    }
    data1=str(data)
    # print(type(data1))

    # if data1:
    #     data1.("C")
    #     print("correct")
    # else:
    #     data1.replace("c","A")
    #     print("incorrect")
    jconverted= json.dumps(data)

    z=open(json_file, 'w') 
    z.write(jconverted,)



d = 'python.docx' 
j = 'word.json'
convert(d,j)

   
   
        





