from pytube import YouTube
#use for installing yt and its features 
link = input("Enter the Video's Link:")
# printing the vide link for above box
y_tube = YouTube(link)
# object made for the link variable
print(f"Title of Video : {y_tube.title}")
#.title method and using printf
stream = y_tube.streams.all()
#stream will be used for seein al the resolutions here
stream = y_tube.streams.filter(progressive=True)

video = list(enumerate(stream))
#enumerate will print index and its value
for i in video:
    print(i)

print("----")
index = int(input(("Enter Index of the needed stream")))

stream[index].download()
print("All Clear")
