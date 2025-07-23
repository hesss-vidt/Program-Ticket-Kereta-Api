import os                                        #O(1)
import datetime                                  #O(1)
import random                                    #O(1)

route_list = [                                   #O(1)
    ("Minstowe", "Cowstone", 3),
    ("Oldcastle", "New North", 5),
    ("Oldcastle", "Freeham", 2),
    ("Cowstone", "New North", 4),
    ("Cowstone", "Bingborough", 6),
    ("Cowstone", "Donningpool", 7),
    ("Cowstone", "Highbrook", 5),
    ("New North", "Bingborough", 3),
    ("New North", "Donningpool", 6),
    ("New North", "Wington", 4),
    ("New North", "Highbrook", 2),
    ("Freeham", "Cowstone", 2),
    ("Freeham", "Donningpool", 3),
    ("Freeham", "Wington", 5),
    ("Bingborough", "Donningpool", 2),
    ("Bingborough", "Highbrook", 1),
    ("Donningpool", "Wington", 4),
    ("Donningpool", "Highbrook", 5),
    ("Donningpool", "Old Mere", 2),
]

train_class = {                                                 #O(1)
    "Economy": {"capacity": 25, "price": 20},
    "Business": {"capacity": 30, "price": 30},
    "Exclusive": {"capacity": 35, "price": 40}
}


def validate_date(date_text):
    try:                                                        #O(1)
        datetime.datetime.strptime(date_text, "%d/%m/%Y")       #O(1)
        return True                                             #O(1)
    except ValueError:                                          #O(1)
        return False                                            #O(1)
                                                                #Total Kompleksitas waktu untuk fungsi validate_date adalah T(n) = 5 = O(1)
def validate_time(time_text):                                              
    try:                                                        #O(1)
        datetime.datetime.strptime(time_text, "%H:%M")          #O(1)
        return True                                             #O(1)
    except ValueError:                                          #O(1)
        return False                                            #O(1)
                                                                #Total Kompleksitas waktu untuk fungsi validate_time adalah T(n) = 5 = O(1)

def order_ticket():
    os.system('cls')                                                                                                                #O(1)                                                                                    
    station_names = set()                                                                                                           #O(1)
    for u, v, _ in route_list:                                                                                                      #O(E)                                                                              
        station_names.add(u)                                                                                                        #O(1)                             
        station_names.add(v)                                                                                                        #O(1)

    print("Make sure you already check your route before you order a ticket.")                                                      #O(1)
    
    while True:                                                                                                                     #O(k)
        start = input("\nFrom : ").strip().title()                                                                                  #O(1)
        end = input("To : ").strip().title()                                                                                        #O(1)

        if start not in station_names or end not in station_names:                                                                  #O(1)
            print("Invalid origin or destination. Please check the routes.")                                                        #O(1)
            input("Press Enter to try again...\nMake sure you already check your route before you order a ticket")                  #O(1)
            continue                                                                                                                #O(1)
        break                                                                                                                       #O(1)

    path, duration = shortest_path(start, end)                                                                                      #O(E*V + V^2 log V)
    if path:                                                                                                                        #O(1)
        print(f"\nHere is the shortest route from {start} to {end}:")                                                               #O(1)
        print(" -> ".join(path))                                                                                                    #O(V)
        print(f"Duration: {duration} hours")                                                                                        #O(1)
    else:                                                                                                                           #O(1)
        print("Route not found.")                                                                                                   #O(1)
        return                                                                                                                      #O(1)
    
    print("\nMake sure you already check your belongings before chooosing the class.")                                              #O(1)
    class_choice = input("Choose class (Economy, Business, Exclusive): ").strip().capitalize()                                      #O(1)
    if class_choice in train_class:                                                                                                 #O(1)
        capacity = train_class[class_choice]["capacity"]                                                                            #O(1)
        class_price = train_class[class_choice]["price"]                                                                            #O(1)
    else:                                                                                                                           #O(1)
        print("Invalid class.")                                                                                                     #O(1)
        return                                                                                                                      #O(1)

    while True:                                                                                                                     #O(k)
        print("\nPlease insert your data:")                                                                                         #O(1)
        name = input("Name                         : ").strip()                                                                     #O(1)
        departure_date = input("Departure Date (DD/MM/YYYY)  : ").strip()                                                           #O(1)
        departure_time = input("Departure Time (HH:MM)       : ").strip()                                                           #O(1)

        if not validate_date(departure_date) or not validate_time(departure_time):                                                  #O(1)
            print("\nInvalid date or time format. Please use DD/MM/YYYY and HH:MM.\n")                                              #O(1)
            continue                                                                                                                #O(1)

        confirm = input("\nAre you sure about all the data above? (Yes/No): ").strip().lower()                                      #O(1)
        if confirm == "yes":                                                                                                        #O(1)
            break                                                                                                                   #O(1)

    depart_dt = datetime.datetime.strptime(f"{departure_date} {departure_time}", "%d/%m/%Y %H:%M")                                  #O(1)
    arrive_dt = depart_dt + datetime.timedelta(hours=duration)                                                                      #O(1)

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"                                                                                         #O(1)
    train_no = f"{random.randint(100, 999)}-{random.choice(alphabet)}"                                                              #O(1)
    seat_no = random.randint(1, 60)                                                                                                 #O(1)
    platform = random.randint(1, 10)                                                                                                #O(1)
    cost_per_hour = 15                                                                                                              #O(1)
    total_cost = duration * cost_per_hour + class_price                                                                             #O(1)

    line = "+" + "-"*54 + "+"                                                                                                       #O(1)
    print("\n" + line)                                                                                                              #O(1)
    print("|{:^54}|".format("TRAIN TICKET"))                                                                                        #O(1)
    print(line)                                                                                                                     #O(1)
    print("| ORIGIN       | {:<37} |".format(start.upper()))                                                                        #O(1)
    print(line)                                                                                                                     #O(1)
    print("| DATE       : {:<15}  TIME      : {:<10} |".format(departure_date, departure_time) )                                    #O(1)
    print("| TRAIN#     : {:<15}  CLASS     : {:<10} |".format(train_no, class_choice.upper()))                                     #O(1)
    print("| PLATFORM   : {:<15}  SEAT      : {:<10} |".format(platform, seat_no))                                                  #O(1)
    print(line)                                                                                                                     #O(1)
    print("| DESTINATION  | {:<37} |".format(end.upper()))                                                                          #O(1)
    print(line)                                                                                                                     #O(1)
    print("| DATE       : {:<15}  TIME      : {:<10} |".format( arrive_dt.strftime('%d/%m/%Y'), arrive_dt.strftime('%H:%M')))       #O(1)
    print(line)                                                                                                                     #O(1)
    print("| PASSENGER NAME : {:<35} |".format(name.upper()))                                                                       #O(1)
    print(line)                                                                                                                     #O(1)
    print(f"Total cost: ${total_cost}")                                                                                             #O(1)


    again = input("\nOrder Another Ticket? (Yes/No): ").strip().lower()                                                             #O(1)
    if again == "yes":                                                                                                              #O(1)
        order_ticket()                                                                                                              #O(1)              
                                                                                                                                    #Total Kompleksitas Waktu untuk fungsi order_ticket adalah T(n) = 63 + E + (E*V + V^2 log V) = O(E*V + V^2 log V)
                                                                                                                                    #Total Kompleksitas Ruang untuk fungsi order_ticket adalah T(n) = O(V + E)
                                                                                                                                    ##E = jumlah node/stasiun, V = jumlah edge/rute
def shortest_path(start, end):
    stations = []                                                                   #O(1)
    for from_station, to_station, duration in route_list:                           #O(E)
        if from_station not in stations:                                            #O(V)
            stations.append(from_station)                                           #O(1)
        if to_station not in stations:                                              #O(V)
            stations.append(to_station)                                             #O(1)

    station_index = {name: i for i, name in enumerate(stations)}                    #O(V)
    n = len(stations)                                                               #O(1)

    routes = [[] for _ in range(n)]                                                 #O(V)
    for from_station, to_station, duration in route_list:                           #O(E)
        u = station_index[from_station]                                             #O(1)
        v = station_index[to_station]                                               #O(1)
        routes[u].append((v, duration))                                             #O(1)
        routes[v].append((u, duration))                                             #O(1)

    max_duration = float('inf')                                                     #O(1)
    travel_time = [max_duration] * n                                                #O(V)
    previous_station = [None] * n                                                   #O(V)
    start_idx = station_index[start]                                                #O(1)
    travel_time[start_idx] = 0                                                      #O(1)
    queue = [(0, start_idx)]                                                        #O(1)

    while queue:                                                                    #O(V)
        queue.sort(reverse=True)                                                    #O(V log V)
        current_duration, current_station = queue.pop()                             #O(1)

        if travel_time[current_station] < current_duration:                         #O(1)
            continue                                                                #O(1)

        for neighbor_station, trip_duration in routes[current_station]:
            total_duration = current_duration + trip_duration                       #O(1)
            if total_duration < travel_time[neighbor_station]:                      #O(1)
                travel_time[neighbor_station] = total_duration                      #O(1)
                previous_station[neighbor_station] = current_station                #O(1)
                queue.append((total_duration, neighbor_station))                    #O(1)

    end_idx = station_index[end]                                                    #O(1)
    if travel_time[end_idx] == max_duration:                                        #O(1)
        return None, max_duration                                                   #O(1)

    path = []                                                                       #O(1)
    while end_idx is not None:                                                      #O(V)
        path.append(stations[end_idx])                                              #O(1)
        end_idx = previous_station[end_idx]                                         #O(1)

    path.reverse()                                                                  #O(V)
    return path, travel_time[station_index[end]]                                    #O(1)
                                                                                    #Total Kompleksitas Waktu untuk fungsi shortest_path adalah T(n) = 27 + (E * V) + (V^2 log V) = O(E * V + V^2 log V)
                                                                                    #Total Kompleksitas Ruang untuk fungsi shortest_path adalah T(n) = O(V + E)
                                                                                    #E = jumlah node/stasiun, V = jumlah edge/rute
def view_routes():
    os.system("cls")                                                                #O(1)
    print("Cost = $15/hour")                                                        #O(1)
    print("+" + "-"*32 + "+" + "-"*20 + "+")                                        #O(1)
    print("|       Routes (2-ways)          |  Duration (hours)  |")                #O(1)
    print("+" + "-"*32 + "+" + "-"*20 + "+")                                        #O(1)

    display = []                                                                    #O(1)
    for from_station, to_station, duration in route_list:                           #O(E)
        key1 = from_station + "-" + to_station                                      #O(1)
        key2 = to_station + "-" + from_station                                      #O(1)
        if key1 not in display and key2 not in display:                             #O(1)
            route_str = f"{from_station}  --  {to_station}"                         #O(1)
            print(f"| {route_str:<30} | {str(duration):^18} |")                     #O(1)
            display.append(key1)                                                    #O(1)
    print("+" + "-"*32 + "+" + "-"*20 + "+")                                        #O(1)
    print("Take your route")                                                        #O(1)
    print("="*15)                                                                   #O(1)

    while True:                                                                     #O(k)
        station_names = set()                                                       #O(1)
        for u, v, _ in route_list:                                                  #O(E)
            station_names.add(u)                                                    #O(1)
            station_names.add(v)                                                    #O(1)
        while True:                                                                 #O(1)
            start = input("\nFrom: ")                                               #O(1)
            if start in station_names:                                              #O(1)
                break                                                               #O(1)
            print(f"'{start}' is not in the route list.")                           #O(1)
        while True:                                                                 #O(1)
            end = input("To : ")                                                    #O(1)
            if end in station_names:                                                #O(1)
                break                                                               #O(1)
            print(f"'{end}' is not in the route list.")                             #O(1)

        path, duration = shortest_path(start, end)                                  #O(E * V + V^2 log V)
        if path:                                                                    #O(1)
            print(f"\nHere is the shortest route from {start} to {end}:")           #O(1)
            print(" -> ".join(path))                                                #O(V)
            print(f"Duration: {duration} hours")                                    #O(1)
        else:                                                                       #O(1)
            print("Routes not found.")                                              #O(1)

        ulang = input("\nSee another route? \nYes/No : ").strip().lower()           #O(1)
        if ulang != 'yes':                                                          #O(1)
            break                                                                   #O(1)
                                                                                    #Total Kompleksitas Waktu untuk fungsi view_routes adalah T(n) = 35 + k + (E * V + V^2 log V) =  O(E * V  + V^2 log V)
                                                                                    #Total Kompleksitas Ruang untuk fungsi view_routes aalah T(n) = O(V + E)

def knapsack_recommend(items, capacity, divisible=True):
    def priority_score(priority):                                                                                                                       #O(1)
        return 100 - (priority * 20)                                                                                                                    #O(1)

    if divisible:                                                                                                                                       #O(1)
        items_sorted = sorted(items, key=lambda x: priority_score(x['priority']) / x['weight'], reverse=True)                                           #O(n log n)
        total_weight = 0                                                                                                                                #O(1)
        selected = []                                                                                                                                   #O(1)

        for item in items_sorted:                                                                                                                       #O(n)
            if total_weight + item['weight'] <= capacity:                                                                                               #O(1)
                selected.append({"name": item['name'], "weight": item['weight'], "taken": item['weight'], "is_whole": True})                            #O(1)
                total_weight += item['weight']                                                                                                          #O(1)
            else:                                                                                                                                       #O(1)
                remaining = capacity - total_weight                                                                                                     #O(1)
                if remaining > 0:                                                                                                                       #O(1)
                    selected.append({"name": item['name'], "weight": item['weight'], "taken": remaining, "is_whole": False})                            #O(1)
                    total_weight += remaining                                                                                                           #O(1)
                break                                                                                                                                   #O(1)
        return selected, total_weight                                                                                                                   #O(1)
    else:                                                                                                                                               #O(1)
        n = len(items)                                                                                                                                  #O(1)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]                                                                                               #O(n * c)
        keep = [[False] * (capacity + 1) for _ in range(n + 1)]                                                                                         #O(n * c)

        for i in range(1, n + 1):                                                                                                                       #O(n)
            weight = int(items[i-1]["weight"])                                                                                                          #O(1)
            score = priority_score(items[i-1]['priority'])                                                                                              #O(1)
            for w in range(capacity + 1):                                                                                                               #O(c)
                if weight <= w:                                                                                                                         #O(1)
                    if dp[i-1][w - weight] + score > dp[i-1][w]:                                                                                        #O(1)
                        dp[i][w] = dp[i-1][w - weight] + score                                                                                          #O(1)
                        keep[i][w] = True                                                                                                               #O(1)
                    else:                                                                                                                               #O(1)
                        dp[i][w] = dp[i-1][w]                                                                                                           #O(1)
                else:                                                                                                                                   #O(1)
                    dp[i][w] = dp[i-1][w]                                                                                                               #O(1)

        w = capacity                                                                                                                                    #O(1)
        selected = []                                                                                                                                   #O(1)
        total_weight = 0                                                                                                                                #O(1)
        for i in range(n, 0, -1):                                                                                                                       #O(n)
            if keep[i][w]:                                                                                                                              #O(1)
                selected.append({"name": items[i-1]['name'], "weight": items[i-1]['weight'], "taken": items[i-1]['weight'], "is_whole": True})          #O(1)
                total_weight += int(items[i-1]["weight"])                                                                                               #O(1)
                w -= int(items[i-1]["weight"])                                                                                                          #O(1)

        selected.reverse()                                                                                                                              #O(1)
        return selected, total_weight                                                                                                                   #O(1)
                                                                                                                                                        #Total Kompleksitas Waktu untuk fungsi knapsack_recommend adalah T(n) = 36 + n log n + (n * c) = O(n log n) jika divisible dan O(n * c) jika indivisible
                                                                                                                                                        #Total Kompleksitas Ruang untuk fungsi knapsack_recommend adalah T(n) = O(n)
                                                                                                                                                        #c = capacity
def view_train():
    os.system('cls')                                                                                                                                    #O(1)                                                   
    print("+" + "-"*11 + "+" + "-"*20 + "+" + "-"*10 + "+")                                                                                             #O(1)
    print("| Class     |  Max Capacity (kg) | Cost ($) |")                                                                                              #O(1)
    print("+" + "-"*11 + "+" + "-"*20 + "+" + "-"*10 + "+")                                                                                             #O(1)
    for cls, info in train_class.items():                                                                                                               #O(1)
        print(f"| {cls:<9} | {info['capacity']:^18} | {info['price']:^8} |")                                                                            #O(1)
    print("+" + "-"*11 + "+" + "-"*20 + "+" + "-"*10 + "+")

    choice = input("\nWe can help you choose what to bring, do you want to try?\nYes/No = ").lower()                                                    #O(1)
    if choice != 'yes':                                                                                                                                 #O(1)
        return                                                                                                                                          #O(1)

    cls_choice = input("Choose class: ").strip().capitalize()                                                                                           #O(1)
    if cls_choice not in train_class:                                                                                                                   #O(1)
        print("Invalid class selection!")                                                                                                               #O(1)
        return                                                                                                                                          #O(1)

    capacity = train_class[cls_choice]['capacity']                                                                                                      #O(1)

    n_input = input("\nGive your item priority scale from 1 (very important) to 5 (not important)\nHow many things you want to bring? : ")              #O(1)
    if not n_input.isdigit():                                                                                                                           #O(1)
        print("Invalid number.")                                                                                                                        #O(1)
        return                                                                                                                                          #O(1)
    n_item = int(n_input)                                                                                                                               #O(1)

    items = []                                                                                                                                          #O(1)
    for i in range(n_item):                                                                                                                             #O(1)
        name = input(f"Item - {i+1}          : ")                                                                                                       #O(1)
        weight = float(input("Weight (kg)       : "))                                                                                                   #O(1)
        priority = int(input("Priority (1-5)    : "))                                                                                                   #O(1)
        print()                                                                                                                                         #O(1)
        items.append({'name': name, 'weight': weight, 'priority': priority})                                                                            #O(1)
       
    divisible = input("Can your items be divided into parts? (Yes/No) : ").strip().lower() == 'yes'                                                     #O(1)
    rec_type = "Fractional" if divisible else "Indivisible"                                                                                             #O(1)
    result, total_weight = knapsack_recommend(items, capacity, divisible)                                                                               #O(n log n) jika divisible dan O(n * c) jika indivisible

    print(f"\n--- Recommendation ({rec_type}) ---")                                                                                                     #O(1)
    print(f"With a capacity of {capacity} kg, we recommend you to bring:")                                                                              #O(1)
    for item in result:                                                                                                                                 #O(n)
        taken = item['taken']                                                                                                                           #O(1)
        name = item['name'] + ("" if divisible and not item['is_whole'] else "")                                                                        #O(1)
        print(f"- {name} ({taken:.2f} kg)")                                                                                                             #O(1)
    
    print(f"\nTotal weight: {total_weight:.2f} kg")                                                                                                     #O(1)
    print("\nYou can use our recommendation or choose another class to carry more.")                                                                    #O(1)
    again = input("\nTry another class or with different items? (Yes/No): ").strip().lower()                                                            #O(1)
    if again == 'yes':                                                                                                                                  #O(1)
        view_train()                                                                                                                                    #O(1)
                                                                                                                                                        #Total Kompleksitas Waktu untuk fungsi view_train adalah T(n) = 38 + n + n log n atau n * c = O(n log n) jika divisible dan O(n * c) jika indivisible
                                                                                                                                                        #Total Kompleksitas Ruang adalah T(n) = O(n)
while True:                                                 
    os.system("cls")                                    #O(1)
    print(" Welcome to Amba Express")                   #O(1)
    print("=" * 40)                                     #O(1)
    print("1. Order Ticket")                            #O(1)
    print("2. View Routes")                             #O(1)
    print("3. View Train")                              #O(1)
    print("4. Exit  ")                                  #O(1)
    print("=" * 40)                                     #O(1)
    pilihan = int(input("Choose (1-4): "))              #O(1)

    if pilihan == 1:                                    #O(1)
        order_ticket()                                  #O(E*V + V^2 log V)
    elif pilihan == 2:                                  #O(1)
        view_routes()                                   #O(E*V + V^2 log V)
    elif pilihan == 3:                                  #O(1)
        view_train()                                    #O(n log n) atau O(n * c) 
    elif pilihan == 4:                                  #O(1)
        os.system('cls')                                #O(1)
        print("Thank you for using our program")        #O(1)
        input("Press Enter to Exit...")                 #O(1)
        break                                           #O(1)

#Total Kompleksitas Algoritma untuk keseluruhan program adalah T(n) = (E*V + V^2 log V) + O(E*V + V^2 log V) + (n log n) atau (n * c) = O((E*V + V^2 log V) + (n log n) atau (n * c)
#Total Kompleksitas Ruang untuk keseluruhan program adalah T(n) = (V + E) + n = O(V + E)