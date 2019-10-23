import os
import json
import time

from sensor.message import send_sms
from sensor.soil import monitor

print(""" 
 __      __         __                  _____          
/  \    /  \_____ _/  |_  ___________  /     \   ____  
\   \/\/   /\__  \\   __\/ __ \_  __ \/  \ /  \_/ __ \ 
 \        /  / __ \|  | \  ___/|  | \/    Y    \  ___/ 
  \__/\  /  (____  /__|  \___  >__|  \____|__  /\___  >
       \/        \/          \/              \/     \/ """)

print("\nWelcome to WaterMe!\n"
      "Before we can help you with measure the water level in your plants we need to make sure that we have all\n"
      "your information.\n")

number = input("Please enter your phone number:\n>>> ")
twilio_sid = input("Please enter your Twilio Account SID:\n>>> ")
twilio_token = input("Please enter your Twilio Account Token:\n>>> ")
twilio_number = input("Please enter your Twilio Phone Number: \n>>> ")

script_dir = os.path.dirname(__file__)
rel_path = "creds.json"
abs_file_path = os.path.join(script_dir, rel_path)

with open(abs_file_path, "r") as f:
    creds = json.load(f)

creds["ACCOUNT_SID"] = twilio_sid
creds["ACCOUNT_TOKEN"] = twilio_token
creds["PHONE_NUMBER"] = twilio_number

with open(abs_file_path, "w") as f:
    json.dump(creds, f)

last_output = "0"
last_sent = -500000000  # Number to make sure first message can always be sent without waiting 24 hours
while True:
    print("In While Loop")
    output = monitor()
    if output == "0":
        last = "0"
    else:
        if last_output is not "0":
            if (time.time() - last_sent) > 43200:
                send_sms(number, "Your plants are in need of watering!")
                last_sent = time.time()
        last_output = "1"

    time.sleep(1)
