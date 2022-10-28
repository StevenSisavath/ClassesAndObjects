class AlarmClock :

    def __init__(self) :
        self.current_time = 0
        self.alarm_is_on = True
        self.alarm_time = 0
        self.toggle_result = ''
    
    def set_current_time(self):
        self.current_time = input('What is the current time?')
        print(self.current_time)

    def set_alarm_on_or_off(self):
        self.toggle = input('Toggle alarm on or off?')
        if self.toggle == 'on':
            self.alarm_is_on = True
            self.toggle_result = 'Alarm is ON'
        elif self.toggle == 'off':
            self.alarm_is_on = False
            self.toggle_result = 'Alarm is OFF'
        else:
            self.alarm_is_on = False
            self.toggle_result = 'on or off was not entered. Alarm is OFF'

    def set_alarm_time(self):
        self.alarm_time = input('What time would you like to set your alarm to?')
        print(self.alarm_time)
        # return self.alarm_time

