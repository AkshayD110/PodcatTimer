
podcastTime=int(input("what is the podcast default runtime (in minutes)?\n"))
#improve the try function here
if (podcastTime<1):
    raise ValueError("Podcast time should be more that a minute")
timeTakenToReachOffice_inMins=30

ifrunat1point5speed=lambda podcastTime: (podcastTime/1.5)
toFinishWithinReachingOffice=lambda podcastTime: (podcastTime/timeTakenToReachOffice_inMins)

whenRunAt1point5speed=ifrunat1point5speed(podcastTime)
speedToRunAt=toFinishWithinReachingOffice(podcastTime)

print(f"If run at 1.5X speed, it will take {whenRunAt1point5speed} minutes to complete")
print(f"To finish the podcast within reaching office, run it at {speedToRunAt}X pace")