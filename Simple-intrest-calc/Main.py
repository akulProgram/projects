#SI = P * N * R / 100

principal = float(input("Enter the amount borrowed: "))
years = float(input("Enter period of years :"))
rate = float(input("Enter rate of interest: "))

interest = (principal * years * rate) / 100
print("The Total interest you will pay is: "+ str(interest))

