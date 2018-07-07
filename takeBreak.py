#this program will take a break every few hours
import time
import webbrowser
total_breaks = 3
break_count = 0
print("this program started on "+time.ctime())
while(break_count<total_breaks):
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=-qlJiGGvPUI")
    break_count = break_count + 1
print("completed")