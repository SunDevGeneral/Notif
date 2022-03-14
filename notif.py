from plyer import notification
import time
i = 135
while True:
    notification.notify(
        title='Rappel',
        message='Point SUN',
        app_icon=None,
        timeout=10,
    )
    time.sleep(i)
