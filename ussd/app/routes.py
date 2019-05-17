from flask import request
from . import app
'''
    USSD callback endpoint to AF(Africanstalking) API
    @return -> response 
'''

# Menu options for user input
MENU_OPTIONS = {
    "": ["CON Personal Helper\n", "1. Get Service Codes.\n"],
    "1": ["CON Select Options\n", "1. Recharge.\n", "2. Check Balance.\n"],
    "1*1": ["CON Select Network\n", "1. Glo.\n", "2. Mtn.\n"],
    "1*1*1": ["END Recharge without Data Bonus = *123*PIN#\n", "Recharge with Data Bonus = *222*PIN#\n"],
    "1*1*2": ["END Recharge = *555*PIN#\n"],
    "1*2*1": ["END Check Balance = #124#\n"],
    "1*2*2": ["END Check Balance = *556#\n"],
}
_default = MENU_OPTIONS[""]
@app.route("/", methods=['GET', 'POST'])
def ussd_callback():
    # get request fields
    sessionId = request.args.get("sessionId", None)
    phoneNumber = request.args.get("phoneNumber", None)
    networkCode = request.args.get("networkCode", None)
    serviceCode = request.args.get("serviceCode", None)
    text = request.args.get("text", None)
    response = ""
    print(sessionId, PhoneNumber, networkCode,text, end=",\n")
    response = "".join(MENU_OPTIONS.get(text, _default))
    

    return response

    

