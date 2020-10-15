# import time
# from plyer import notification

# if __name__ == "__main__":
#     while True:
#         notification.notify(
#             title="Please drink some water",
#             message = "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
#             app_icon = "D:\\Coding With Rick\\Rick\\Notify\\Water-Notification\\icon.ico",
#             timeout = 10
#         )
#         time.sleep(60*60)
import time
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Please drink some water",
            message = "The National Academies of Sciences, Engineering, and Medicine determined that an adequate daily fluid intake is: About 15.5 cups (3.7 liters) of fluids for men. About 11.5 cups (2.7 liters) of fluids a day for women.",
            app_icon = "D:\\Coding With Rick\\Rick\\Notify\\Water-Notification\\icon.ico",
            timeout = 10
        )
        time.sleep(60*60)