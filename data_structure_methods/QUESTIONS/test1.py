
def main():
    while True:
        string = input("enter a string: ")
        print(f"upper cased : ",string.upper())

        cent = int(input("enter the width of centering :"))
        center_result= string.center(cent)
        print(f"centered string :",center_result)

        index1 = input("Enter a substring to count : ")
        index_result = string.count(index1) 
        print(f"count of {index1} :",index_result)

        suffix = input("Enter a suffix to check at the end :" )
        result = string.endswith(suffix)
        print(f"End with {result} is true")

        name = input("enter the name : ")
        age = int(input("enter your age :"))
        formatted = "hello, my name is {} and my age is {} ".format(name,age)
        print(f"formated string : {formatted}")

if __name__=="__main__":
    main()

