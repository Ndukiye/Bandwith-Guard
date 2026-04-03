
from config import user_presets
from storage import get_bandwith_data,get_presets
from datetime import date


def display_usage(data,presets):
    if not data:
        print("No bandwidth data yet. Monitor must be running.")
        return
    if not presets:
        print("No preset configured. Use option 2 to set up.")
        return
    item_data = data[-1]
    item_presets = presets[0]
    print(f'Plan: {item_presets["data_plan"]}, Cap: {item_presets["usage_limits"]}mb, Used: {item_data["total_mb"]}mb, Speed: {item_data["speed_mbps"]}mbps')
    

while True:
    user_input = input("\nBandwith Guardian - 1\nEdit Config - 2\nClose - 3\n")
    match user_input:
        case "1": 
            display_usage(get_bandwith_data(),get_presets())
        case "2":
            user_presets()
        case "3":
            break

