import random
rand_num = random.randint(1111,9999)
f = open("student.txt")
line_list = f.readlines()
f.close()
#print(line_list)

f2 = open("student_email.txt", "w")
for i in line_list:
    #print(i)
    split = i.split(",")
    #print(split)
    id = split[0].split(" ")[0]
    #print(id)
    fnames = split[1]
    #print(fnames)
    lastname = split[0].split(" ")[1].lower()
    l_initial = ""
    for i in fnames:
        if i.isupper() == True:
            l_initial += i + "."
            l_initial = l_initial.lower()
    #print(l_initial)
    
    #print(f"{id} {l_initial}{lastname}{rand_num} @poppleton.ac.uk")
    
    f2.write(f"{id} {l_initial}{lastname}{rand_num} @poppleton.ac.uk\n")
f2.close()         