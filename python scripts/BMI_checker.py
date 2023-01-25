weight=int(input('enter your weight: '))
height=float(input('enter your height in feet: '))


def body_mass_index(weight,height):
    bmi = weight/(height**2)
    bmi = round(bmi,1)
    
    if bmi < 18.5:
        print(f'your BMI is : {bmi}, you are underweight')
    elif 18.4 < bmi < 25:
        print(f'your BMI is : {bmi}, you are normal')
    elif 25.9 < bmi < 30:
        print(f'your BMI is : {bmi}, you are overweight')
    elif 29.9 < bmi < 35:
        print(f'your BMI is : {bmi}, class 1 obesity ')
    elif 34.9 < bmi < 40:
        print(f'your BMI is : {bmi}, class 2 obesity')
    else:
        print(f'your BMI is : {bmi}, extreme scenario consult your doctor')
body_mass_index(weight, height)