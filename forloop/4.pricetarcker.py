#L2 – Problem 1: Weekly Stock Price Tracker



price = []
for i in range(1,8):
    usr_input = int(input(f"enter day{i}:"))
    price.append(usr_input)
print(price)


for day,p in enumerate(price,start=1):
    print(f"day{day}:{p}")


highest_price = max(price)
lowest_price = min(price)
total_sum =sum(price)
num_elements = len(price)
if num_elements>0:
    average = total_sum/num_elements
else:
    average = 0

print("Highest stock price :",highest_price)
print("lowest stock price :",lowest_price)
print("average stock price :",average)



