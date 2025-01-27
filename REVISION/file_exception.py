def read_file(filename):
    try:
        with open(filename,"r") as file:
            content=file.read()
        print("file content:",content)
    except FileNotFoundError:
        print("error: file is not available")
    except PermissionError:
        print("error:you dont have permission to access file")
        
file=input("enter filename;")
read_file(file)

        