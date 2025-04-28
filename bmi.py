#functions
def calculate_bmi(height, weight):
    print("Height = " + str(height))        #str() function changes the input value to string
    print("Weight = " + str(weight))

    bmi = weight/(height**2)
    print("BMI = " + str(bmi))
    return bmi

    
def classify_bmi(bmi):
    if(bmi<18.5):
        print("Under Weight")
    elif(bmi>=18.5 and bmi<=25.0):
        print("Normal Weight")
    else:
        print("Over Weight")


#main

bmi_calculated = calculate_bmi(weight=57, height=1.73)  #can only concatenate str to str
classify_bmi(bmi_calculated)
print()