import psutil
import time
from datetime import date, timedelta
from storage import update_storage,get_bandwith_data,get_presets
from config import user_presets
connected_process_pid = []

def check_cap(total_mb):
    presets = get_presets()
    cap = presets[0]["usage_limits"]
    if total_mb >= cap:
        # print("Data Usage has reached Limit !!")
        return True
    # elif total_mb >= (80/100)*cap :
        # print("Data Usage nearing limit.")
    return False

def save_bandwith_data(total_mb,cap_reached):
    current_date =  str(date.today())
    old_data = get_bandwith_data()
    if old_data != []:
        last_entry = old_data[len(old_data)-1]    
        if  last_entry["date"] == current_date:
            last_entry["total_mb"] = total_mb
            last_entry["usage_limit"] = cap_reached
            update_storage(old_data)
        else:
            new_data = {"date":current_date,"total_mb": total_mb,"usage_limit":cap_reached}
            old_data.append(new_data)
            update_storage(old_data)
    else:
        new_data = {"date":current_date,"total_mb": total_mb,"usage_limit":cap_reached}
        old_data.append(new_data)
        update_storage(old_data)

def track_data_usage():
    total_bytes = 0
    total_mb = 0
    while True: 
        old = psutil.net_io_counters().bytes_recv
        time.sleep(1)
        new = psutil.net_io_counters().bytes_recv
        total_bytes+=(new-old)
        total_mb = total_bytes/1048576
        save_bandwith_data(total_mb,check_cap(total_mb))
        print(f'Used in last second: {total_bytes} bytes | Total today: {total_mb:.2f} MB')


while True:
    user_input = input("\nBandwith Guardian - 1\nEdit Config - 2\nClose - 3\n")
    match user_input:
        case "1":
    #    print(f'Used in last second: {total_bytes} bytes | Total today: {total_mb:.2f} MB')
            track_data_usage()
        case "2":
            user_presets()
        case "3":
            break






# def check_date():
#     saved_date = date.today()
#     print(saved_date)
#     print(date.today() > saved_date)

# check_date()

# print(psutil.Process())
# print(psutil.net_connections())

# for proc in psutil.process_iter(['pid', 'name', 'username']):
#     print(proc.info)

# all_connections = psutil.net_connections()
# for connection in all_connections:
#     if connection.status == "ESTABLISHED":
#             connected_process_pid.append(connection.pid)

# for id in connected_process_pid:
#     if id is not None: 
#         print(psutil.Process(id))

