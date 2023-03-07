from twilio.rest import Client

class NotificationManager:
    def __ini__(self):
    self.client=Client(TWILIO_SID,TWILIO_TOKEN)
    #This class is responsible for sending notifications with the deal flight details.

    def send_sms(self, message):
        message=self.client.messaged.create(
            body=message,
            from=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,

        )

        print(message.sid)