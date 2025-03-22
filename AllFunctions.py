class AllFunctions():
    def Subfields():
        print("Sub-fields in AI are: ")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")

    def OddEven():
        num=int(input("Enter The Number: "))
        if(num%2==0):
            print(num ,"is Even Number ") 
        else:
            print(num ,"is Odd Number ") 

    def Eligible():
        gender=input("Your Gender : ")
        age=int(input("Your Age : "))
        if gender == "Male" and age>20:
            print("Eligible")
        elif gender == "Female" and age>17:
            print("Eligible")
        else:
            print("Not Eligible")

    def Percentage():
        sub1=int(input("Subject1:"))
        sub2=int(input("Subject2:"))
        sub3=int(input("Subject3:"))
        sub4=int(input("Subject4:"))
        sub5=int(input("Subject5:"))
        Total=sub1+sub2+sub3+sub4+sub5
        print("Total : ",Total)
        percent=Total/500*100
        print("Percentage : ",percent)

    def Triangle():
        Height=int(input("Height : "))
        Breadth=int(input("Breadth: "))
        print("Area formula: (Height*Breadth)/2")
        print("Area of Triangle:",(Height*Breadth)/2)
        Height1=int(input("Height1 : "))
        Height2=int(input("Height2 : "))
        Breadth=int(input("Breadth : "))
        print("Perimeter formula: Height1+Height2+Breadth")
        print("Perimeter of Triangle: ",Height1+Height2+Breadth)


