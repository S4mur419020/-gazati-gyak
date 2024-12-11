def A():
    anev = input("Autó neve: ")
    gyev = int(input("Gyártási dátum: "))
    return anev, gyev

def B(anev, gyev):
    if gyev == 2024:
        print(f"Ez az {anev} friss gyártás.")
    elif gyev < 2000:
        print(f"Ez az {anev} öreg autó.")
    else:
        print(f"Ez az {anev} átlagos korú.")