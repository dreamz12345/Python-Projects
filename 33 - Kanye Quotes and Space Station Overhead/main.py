import requests
from datetime import datetime

MY_LAT = 52.237049  # Your latitude
MY_LONG = 21.017532  # Your longitude

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

# Your position is within +5 or -5 degrees of the ISS position.


def is_nighttime():
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    time_now = datetime.now()

    if time_now.hour >= sunset:
        if time_now.hour <= sunrise:
            return True
    return False


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5:
        if MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
            return True
    return False


def send_notification():
    if is_nighttime():
        if is_iss_overhead():
            print("Look up!")


send_notification()

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
