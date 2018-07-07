#this program will take a break every few hours
import time
import webbrowser
total_breaks = 3
break_count = 0
while(break_count<total_breaks)
    time.sleep(5)
    webbrowser.open("https://www.youtube.com/watch?v=dQ4w9WgXCQ")
    break_count = break_count + 1