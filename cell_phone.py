class CellPhone :
    
    def __init__(self, model, phone_number):
        self.model = model
        self.phone_number = phone_number
        self.contacts = {
            'Guy1' : '1111111111',
            'Guy2' : '2222222222',
            'Guy3' : '3333333333',
            'Guy4' : '4444444444',
            'Guy5' : '5555555555',
            'Guy6' : '6666666666',
        }
        self.messages_recieved = []
        self.vibrate_on = True

    def recieve_text(self, message):
        print(message)
        self.messages_recieved.append(message)

    def toggle_vibrate_mode(self):
        self.vibrate_on = not self.vibrate_on

    def send_text(self, message):
        print(message)

    