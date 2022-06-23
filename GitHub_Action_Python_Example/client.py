
class HelloWorld:

    def __init__(self,
                 message=None,
                 *args, **kwargs):
        super(HelloWorld, self).__init__(*args, **kwargs)
        self.message = message or 'Hello World!'

    def get_message(self):
        return self.message
    
    def lineNotifyMessage(token, msg):          #傳送lineNotify
    headers = {"Authorization": "Bearer " + token, "Content-Type" : "application/x-www-form-urlencoded"}
    payload = {'message': msg }
    r = requests.post("https://notify-api.line.me/api/notify", headers = headers, params = payload)
        return r.status_code
