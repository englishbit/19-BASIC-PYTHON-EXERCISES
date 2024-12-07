day=int(input("enter the day:"))
hours=int(input("enter the hours:"))
minute=int(input("enter the minute:"))
dy_to_mnt=24*60
hrs_to_mnt=hours*60
second=(minute+dy_to_mnt+hrs_to_mnt)*60
print(second)

