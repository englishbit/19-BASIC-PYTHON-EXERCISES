day=int(input("enter the day:"))
hours=int(input("enter the hours:"))
minute=int(input("enter the minute:"))

dy_to_hr=day*24
hrs_to_mnt=(hours+dy_to_hr)*60
second=(minute+hrs_to_mnt)*60
print(second)

