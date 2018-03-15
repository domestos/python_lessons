
inputfile = "../user_files.txt"
outputfile = "../password_files.txt"
line_to_loock = "valera"


myfile1 = open(inputfile, mode='r+', encoding='utf8')

# if 'w'- the file will be overwritten
# if 'a' - information will be added
myfile2 = open(outputfile, mode='a', encoding='utf8')
#print(myfile.read())




def read_file():
    for num,  line in enumerate(myfile1, 1):
        if "valera" in line:
            print("hello "+str(num)+" "+ line.strip())


#myfile1.close()


def write_file():
    for num, line in enumerate(myfile1, 1):
        if line_to_loock in line:
            print("line N:"+str(num) + " : " + line.strip())
            myfile2.write("Found line: "+line)
#myfile2.close()

#read_file()
write_file()

