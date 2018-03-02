#mainly suits DeveloperTea podcast right now.
podcastTime=int(input("what is the podcast default runtime (in minutes)?\n"))
#improve the try function here
if (podcastTime<1):
    raise ValueError("Podcast time should be more that a minute")
timeTakenToReachOffice_inMins=30

ifrunat1point5speed=lambda podcastTime: (podcastTime/1.5)
toFinishWithinReachingOffice=lambda podcastTime: (podcastTime/timeTakenToReachOffice_inMins)

whenRunAt1point5speed=ifrunat1point5speed(podcastTime)
speedToRunAt=toFinishWithinReachingOffice(podcastTime)
if(whenRunAt1point5speed>60):
    timeInHours,timeInMins=divmod(whenRunAt1point5speed,60)
    print(f"If run at 1.5X speed, it will take {timeInHours} Hours and  {timeInMins} minutes to complete")
    print("You won't be able to finish it before reaching office !")
else:
    print(f"If run at 1.5X speed, it will take {whenRunAt1point5speed} minutes to complete")
    print(f"To finish the podcast within reaching office, run it at {speedToRunAt}X pace")




