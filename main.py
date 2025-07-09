from datetime import datetime, timedelta
from playsound import playsound as play
from time import sleep
import os


def run_alarm(alarm):
    while True:
        time_now = datetime.now().strftime("%H:%M")
        time_now = datetime.strptime(time_now, "%H:%M")
        if time_now == alarm:
            try:
                file_path = os.path.join(
                    os.path.dirname(__file__), "Include", "sound.mp3"
                )
            except:
                file_path = os.path.join(
                    os.path.dirname(__file__), "Include", "sound.mp3"
                )
                file_path = file_path.replace(
                    "\\", "/"
                )  # حل میشه powershell این مشکل در \ to / ویندوز اجرا شه نمیتونه ادرس رو بخونه و ارور میده ولی با جیگزینی powershell اگه این کد از
            run = 5
            while run > 0:
                play.playsound(file_path)
                run -= 1
            return "The alarm task {} is complete"
        # # check_time = time_now.replace(hour=12, minute=0, second=0, microsecond=0)
        # if (
        #     alarm < time_now
        # ):  # The subtraction should be reversed when the time is greater than 12; otherwise, it will set day = -1
        #     remainder = time_now - alarm
        # else:
        #     remainder = alarm - time_now
        remainder = alarm - time_now
        print(f"time now : {time_now}\nalarm : {alarm}\nremainder time : {remainder}")
        if remainder > timedelta(hours=1):
            sleep(3600)
        elif remainder > timedelta(minutes=30):
            sleep(1800)
        elif remainder > timedelta(minutes=10):
            sleep(300)
        elif remainder > timedelta(minutes=5):
            sleep(150)
        elif remainder > timedelta(minutes=1):
            sleep(30)
        else:
            sleep(10)


def main():
    times = []
    while True:
        try:
            input_time = input("Enter the hour and minute (00:00) : ")
            if input_time.title() in ("Exit", "Leave"):
                break
            input_time = datetime.strptime(
                input_time, "%H:%M"
            )  # PM یا AM شما باید ساعت را به فرمت ۲۴ ساعته وارد کنید، بدون
            if input_time.time() < datetime.now().time():
                print(
                    "The time you entered is earlier than the current time (the entered time will be for tomorrow)"
                )
            else:
                times.append(input_time)
        except TypeError:
            print("Please enter only the hour and minute")
        except ValueError:
            print("The format or hour or minute is invalid")
    times.sort()
    run = 1
    for i in times:
        print(run_alarm(i).format(run))
    return "All alarm clock tasks have been completed."


if __name__ == "__main__":
    print(main())
