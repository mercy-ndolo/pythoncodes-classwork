#compound interest
def compound_intrest(principle,rate_per_month,time_in_months):
 return (principle * rate_per_month * time_in_months /100)+ principle
principle = int(input("Enter your principle:"))
rate_per_month = float(input("Enter rate_per_month:"))
time_in_months = int(input("Enter the time_in_months:"))

CD = compound_intrest(principle,rate_per_month,time_in_months)
print("your Compound Intrest is = %.2f"%CD)