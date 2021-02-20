def bmi_calc():
    n = int(input("How many people would you like to check the BMI for? "))
    bmis = []
    for person in range(n):
        temp = input("Weight and height: ").split()
        bmi = int(temp[0]) / (float(temp[1])**2)
        if bmi < 18.5:
            bmis.append("Underweight ")
        elif bmi < 25:
            bmis.append("Normal weight ")
        elif bmi < 30:
            bmis.append("Overweight ")
        else:
            bmis.append("Obese ")

    return ''.join(x for x in bmis)
        

print(bmi_calc())