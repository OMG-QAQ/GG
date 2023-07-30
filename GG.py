import time

def countdown(minutes):
    seconds = minutes * 60
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = "{:02d}:{:02d}".format(mins, secs)
        print(f"Time left: {timer}", end="\r")
        time.sleep(1)
        seconds -= 1
    
    print("\nTime's up! Stay focused!")

# 设置专注时间为25分钟
focus_minutes = 25

countdown(focus_minutes)
