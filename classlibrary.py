class multiplefunctions():
    def Subfields():
        lists = ["Machine Learning", "Neural Networks", "Vision", "Robotics", "Speech Processing", "Natural Language Processing"]
        print('Sub-fields in AI are:')
        for i in lists:    
            print(i)
    
    def oddEven():
        num= int(input("Enter your number:"))
        if (num%2)==0:
            print(num, 'is Even number')
        else:
            print(num, 'is Odd number')
    
    def Elegible():
        gender = input('Enter your gender:').lower()
        age = int(input('Enter your age:'))
        if gender=='male' and age>=21:
            print('Eligible')
        elif gender =='female' and age>=18:
            print('Eligible')
        else:
            print('Not Eligible')
    
    def percentage():
        Subject1 = int(input('Subject1'))
        Subject2 = int(input('Subject2'))
        Subject3 = int(input('Subject3'))
        Subject4 = int(input('Subject4'))
        Subject5 = int(input('Subject5'))                      
        Total = Subject1+Subject2+Subject3+Subject4+Subject5
        print('Subject1 =', Subject1)
        print('Subject1 =', Subject2)
        print('Subject1 =', Subject3)
        print('Subject1 =', Subject4)
        print('Subject1 =', Subject5)
        print( 'Total:', Total)
        print('Percentage:', Total/5)

    def triangle():
        Height= int(input('Enter height:'))
        Breadth= int(input('Enter breaadth:'))
        print('Area formula: (Height*Breadth)/2')
        print("Area of Triangle:", (Height*Breadth)/2)
        Height1=int(input('Enter height1:'))
        Height2=int(input('Enter height2:'))
        Breadth2=int(input('Enter breadth1:'))
        print('Perimeter formula: Height1+Height2+Breadth2')
        print('Perimeter of Triangle:',  Height1+Height2+Breadth2)
        message = 'Perimeter of Triangle:'

