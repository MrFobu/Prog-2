#Uppgift1
hour = int(input("What is the current hour? :"))
minute = int(input("What is the current minute? :"))
time = [hour, minute]

timeAdd = (((((((((10**100)/60)/24)/365.242199))/10**93)%1)*365.242199)%1)*1440 #The bullshitiest bs to ever see the light of day

for x in range(int(timeAdd)):
    if time[1] < 60:
        time[1] +=1
    elif time[1] >= 60:
        time[1] = 0
        time[0] += 1
    if time[0] >= 24:
        time[0] = 0

print(f"in a googol minutes the time would be: {time[0]}:{time[1]}")

#uppgift2
