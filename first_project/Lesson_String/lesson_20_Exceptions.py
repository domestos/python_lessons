import sys
filename = "./lesson_20"



while True:
    try:
        myfile = open(filename, mode='r', encoding='utf8')
    except Exception:
        print("inside EXCEPT")
        print("Error found: "+ str(sys.exc_info()[1]))
        filename = input("enter Correct file name:")
    else:
        print("inside ELSE")
        print(myfile.read())
        sys.exit()
    finally:
        print("inside FINALLY")

print("==================THE END===============================")

