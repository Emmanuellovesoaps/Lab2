def calculate_bmi(height, weight):  
    
    print("Height = " + str(height))
    print("Weight = " + str(weight))

    
    bmi = weight/(height*height)

    print(f'bmi = {bmi}')

    if bmi < 18.5 :
        print("Under Weight")
        return -1
    elif bmi <= 25.0 and bmi >= 18.5 :
        print("Normal Weight")
        return 0
    else:
        print("Over Weight")
        return 1
    
result = calculate_bmi(weight= 57, height= 1.73)
print("Return value:", result)