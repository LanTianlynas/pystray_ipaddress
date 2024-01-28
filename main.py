import time
from threading import Thread, Event
import pystray
import requests
from PIL import Image, ImageDraw, ImageFont

FLAGS_FOLDER_PATH = "./flags"

def get_ip_info():
    try: 
        ip_info = requests.get("https://ipinfo.io/json").json()
        return ip_info.get("country","").lower(), ip_info.get("ip", "unknown")
    except Exception as e:
            print(f"Error fetching IP info: {e}")
            return "", "unknown"

def create_image(country_code):
    if country_code:
        flag_path = f"{FLAGS_FOLDER_PATH}/{country_code}.png"
        try:
            flag = Image.open(flag_path)
            return flag
        except FileNotFoundError:
            print(f"Flag not found: {flag_path}")
    
    print("No country code provided")
    return create_placeholder_image()

def create_placeholder_image():
    img = Image.new('RGB', (64, 32), color="white")
    d = ImageDraw.Draw(img)
    fnt = ImageFont.load_default()
    d.text((10,10), "No Flag", font=fnt, fill="black")
    return img
    
def update_icon(icon, stop_event):
    while not stop_event.is_set():
        country_code, ip = get_ip_info()
        flag = create_image(country_code)
        if flag:
            icon.icon = flag
            icon.title = ip
        else:
            print(f"Error creating flag for country code: {country_code}")
        time.sleep(2)

def exit_action(icon, stop_event):
    print("Exiting...")
    stop_event.set()
    icon.stop()
    print(stop_event.is_set())


stop_event = Event()
icon = pystray.Icon("ip-flag", icon=create_placeholder_image())
icon.menu = pystray.Menu(
    pystray.MenuItem("Exit", lambda icon: exit_action(icon, stop_event))
)
update_thread = Thread(target=update_icon, args=(icon, stop_event))
update_thread.start()  
icon.run()  
