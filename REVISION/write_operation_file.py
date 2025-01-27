def write_file(filename):
    try:
        with open(filename,"w") as file:
            data=input("enter data to write:")

            file.write(data)
            print("data written successfully!")
    except PermissionError:
        print("error: dont have permission")
    except Exception as e:
        print("unexpected exception",e)
    else:
        print("you are eda")

write=input("enter filename:")
write_file(write)
    