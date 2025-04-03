#-------if else-----
a=10
b=20
if(a>b):
    print("a is greater")
else:
    print("b is greater")

#------nested if-----------
income=50000
cr_score=700
emp_status="employed"
if(income>=40000):
    if(cr_score>=650):
        if(emp_status=="employed"):
            print("you are eligible for loan")
        else:
            print(" you need to be employed to get loan")
    else:
        print("your credit score is too low for loan")
else:
    print("your income is too low to qualify for loan")            