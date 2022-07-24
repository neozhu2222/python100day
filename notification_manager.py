from twilio.rest import Client

TWILIO_SID = TWILIO_ACC_SID
TWILIO_AUTH_TOKEN = TWILIO_TOKEN
TWILIO_VIR_NUMBER = vir_number
TWILIO_VER_NUMBER = your_num

class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages(
            body=message,
            from=TWILIO_VIR_NUMBER,
            to=TWILIO_VER_NUMBER,
        )
        

