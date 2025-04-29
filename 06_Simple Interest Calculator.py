# Simple Interest Calculator

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100

print("Simple Interest Calculator")

P = float(input("Enter Principal amount (₹): "))
R = float(input("Enter Rate of Interest (% per annum): "))
T = float(input("Enter Time (in years): "))

SI = simple_interest(P, R, T)
print(f"Simple Interest = ₹{SI:.2f}")
