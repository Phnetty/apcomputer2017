def calculate():
    print 'If you have a letter grade, enter in 4 for A, 3.5 for A/B, 3 for B, 2.5 for B/C, and 2 for D.'
    print 'Enter in your number of classes.' #This is getting the number of classes someone is taking.
    classes = raw_input()
    counter = 1
    GPA = 0
    if counter <= int(classes):
        print 'Enter in your grade for the first class. If you have a different number of classes than the provided amount, enter in 0 to the other unused classes.' #This following string of code tells what the grades of the classes are.
        grade1 = raw_input() 
        GPA = GPA + int(grade1)
        counter = counter + 1
    if counter <= int(classes):
        print 'Enter in your grade for your second class, if you dont have 2 or more classes, enter 0 for the rest of the classes.'
        grade2 = raw_input()
        GPA = GPA + int(grade2)
        counter = counter + 1
    if counter <= int(classes):
        print 'Enter in your grade for your third class, if you dont have 3 or more classes, enter 0 for the rest of the classes.'
        grade3 = raw_input()
        GPA = GPA + int(grade3)
        counter = counter + 1
    if counter <= int(classes):
        print 'Enter in your grade for your fourth class, if you dont have 4 or more classes, enter 0 for the rest of the classes.'
        grade4 = raw_input()
        GPA = GPA + int(grade4)
        counter = counter + 1
    if counter <= int(classes):
        print 'Enter in your grade for your fifth class, if you dont have 5 or more classes, enter 0 for the rest of the classes.'
        grade5 = raw_input()
        GPA = GPA + int(grade5)
        counter = counter + 1
    if counter <= int(classes):
        print 'Enter in your grade for your sixth class, if you dont have 6 or more classes, enter 0 for the rest of the classes.'
        grade6 = raw_input()
        GPA = GPA + int(grade6)
        counter = counter + 1
    if counter <= int(classes):
        print 'Enter in your grade for your seventh class, if you dont have 7 or more classes, enter 0 for the rest of the classes.' #These classes are optional for people who aren't taking these classes.
        grade7 = raw_input()
        GPA = GPA + int(grade7)
        counter = counter + 1
    if counter <= int(classes):
        print 'Enter in your grade for your eighth class, if you dont have 8 or more classes, enter 0 for the rest of the classes.' #Should they put in zero for the classes they aren't taking,then it will work as if they hadn't had those classes listed.
        grade8 = raw_input()
        GPA = GPA + int(grade8)
        counter = counter + 1
    if counter <= int(classes):
        print 'Enter in your grade for your ninth second class, if you dont have 9 or more classes, enter 0 for the rest of the classes.' #This is because by adding nothing, you can still divide by the number of classes you had grades in and still get an average.
        grade9 = raw_input()
        GPA = GPA + int(grade9)
    
    Final_GPA = int(GPA) / int(classes) #This then divides them by the number of classes the person is taking.
    print Final_GPA
    
calculate()
        
        