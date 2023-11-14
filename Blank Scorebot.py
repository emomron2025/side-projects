#Welcome to my scorebot template!
#
#After you're done putting in all your issues, set the variable "scoreissues" to however many issues you're using. This works to create
#all the files that'll store whether or not each individual issue has been solved, so that it doesn't notify the person more than once.
#
#Once you're completely done with everything, remove all the comments, add a bunch of dummy code (if you want), and run the following:
#
#pip install pyarmor
#pyarmor obfuscate <path>
#
#Replace <path> with the path to this script, and it'll convert it to hex.
#
#In task scheduler, use pythonw.exe to run this program as opposed to python.exe, so that it starts minimized.
#
#The functions are as follows.
#
#Note that all of the "check" functions return 1 if the check passes and 0 if it does not.
#
#gain(points,reason) has a number, "points", and a string, "reason". When calling it, input that many points for the desired reason.
#Example:
#gain(5,"properly answering Forensics Question 1")
#
#lose(points,reason) has a number, "points", and a string, "reason". When calling it, input that many points for the desired reason.
#Example:
#lose(5,"the correct answer has not been inputted to Forensics Question 1")
#
#checkreg(path,valuename,value) checks whether the registry key at "path" . Note that it'll return 0 both if the key has the wrong value and if it doesn't exist.
#Example:
#checkreg(r"\Software\Microsoft\Windows\Run","shutdown","C:\Windows\System32\shutdown.exe")
#would check to see if a registry key that shut down the machine for all users on startup existed. It would return 1 if so, and 0 if not. (Probably don't put this specific key in an image, since it's so, so easy to brick the VM.)
#Remember: This function only works in the Local Machine hive. If you need to reference a different hive, copy everything from within checkreg and modify as needed.
#Also, REMEMBER THE "r".
#Also also, remember that you can put fun things in HKCU to affect only one account, which people don't always check.
#
#checkforensics(path,answer) checks inside the file at "path" to see if it has the string "answer" anywhere. If so, it returns 1. If it doesn't or the file does not exist, it returns 0. (Even if the answer is a number, it still needs to be defined as a string.)
#Example:
#checkforensics("C:\Users\cyber\Desktop\question1.txt","42")
#
#checkexist(path) checks to see if a file at "path" exists. In most situations, you'll be using it to detect malware, so you need to make sure that you're checking for the output to be 0 rather than 1.
#Example:
#checkexist("C:\Windows\System32\dhcp.exe)
#(no file named dhcp.exe *should* exist within System32; it looks legitimate, though.)
#
#Read all about how to actually call functions down in the issues section.
#
#
#
#all the fancy workings
#---------------------------------------------------------------------------------------------------------------------------------------------
import winreg
import os
from plyer import notification
path = os.getcwd()
try:
    os.mkdir(f"{path}\mem")
except FileExistsError:
    pass
os.chdir(f"{path}\mem")
if not os.path.isfile("README.txt"):
    with open("README.txt", "w") as f:
        f.write("This directory exists for internal scoring purposes.\n\nDeleting or modifying files will corrupt the image and prevent full points from being awarded.")
if not os.path.isfile("score"):
    with open("score","w") as f:
        f.write(0)
global scoreissues
scoreissues = 
#intentionally left to throw an error, so that the user doesn't forget to set it
global score
score = f.read("score")
score = int(score)
i = 0
while True:
    if not os.path.isfile(f"mem{i}"):
        with open(f"mem{i}", "w") as f:
            f.write("0")
    i += 1
    if i >= scoreissues:
        break
def gain(points,reason):
    global score
    score += points
    with open("score","w") as f:
        f.write()
    notification.notify(
        title = "You gained points!",
        message = f"{points} points awarded because {reason}.",
        app_name = "Image Scorebot",
        timeout = 5,
        )
def lose(points,reason):
    global score
    score -= points
    with open("score","w") as f:
        f.write(score)
    notification.notify(
        title = 'You lost points!',
        message = f"{points} points lost because {reason}.",
        app_name = "Image Scorebot",
        timeout = 5,
    )
def checkreg(path,valuename,value):
    try:
        with winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,path) as key:
            if winreg.QueryValueEx(key,valuename)[0] == value:
                winreg.CloseKey(key)
                return 1
            else:
                winreg.CloseKey(key)
                return 0
    except WindowsError:
        winreg.CloseKey(key)
        return 0
def checkforensics(path,answer):
    try:
        with open(path, 'r') as file:
            for line in file:
                if answer in line:
                    return 1
            else:
                return 0
    except WindowsError:
        return 0
def checkexist(path):
    try:
        if os.path.exists(path):
            return 1
        else:
            return 0
    except WindowsError:
        return 0
#-------------------------------------------------------------------------------------------------------------
#call this for most issues that use any of the above programs.
#q1, q1, and q3 should be in the form of <checkforensics("C:\Users\cyber\Desktop\forensics1.txt","Kaladin Stormblessed")>
#if you need more than 3 queries, write it out yourself
#if you need less, put 1 == 1 as the arguments
#num should be the memory file that you want to store it. keep in mind that they count from 0, not 1, so there will be a number
#of memory files equal to scoreissues - 1
#points should be equal to the amount of points you want to award. (i recommend making the total number 100.)
def issue(q1,q2,q3,num,points,messageGain,messageLose):
    with open(f"mem{num}","r") as g:
        if q1 and q2 and q3 and g.read() != 1:
            with open(f"mem{num}","w") as f:
                f.write("1")
            gain(points,messageGain)
        if not q1 or not q2 or not q3 and g.read() == 1:
            with open(f"mem{num}","w") as f:
                f.write("0")
            lose(points,messageLose)
#all your shenanigans
#--------------------------------------------------------------------------------------------------------------





issue(checkforensics("C:\Users\emomron2025\Desktop\question1.txt","Kaladin"),True,True,4,17,"you correctly answered Forensics 1","you incorrectly answered Forensics 1")






#------------------------------------------------------------------------------------------------------------
#DO NOT WRITE ANYTHING BELOW THIS
#creates a file that you can look at with all the scores
scorelist = []
for i in range(scoreissues):
    with open(f"mem{i}","r") as f:
        scorelist.append(f.read())
if not os.path.isfile("scoringdata"):
    with open("scoringdata", "w") as f:
        f.write("".join(scorelist))