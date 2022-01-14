from statistics import mean

print('Swallow Speed Analysis: Version 1.0')
#conversion = 1.60934


def swallow_speed():
    '''Function to find the maximum speed, minimum speed and mean speeds of the swallows in the UK and in Europe. '''

    reading = input("Enter the Next Reading: ")

    list_readings = list()

    if reading == "":
        print('No readings entered. Nothing to do.')
        exit()
    else:
        list_readings.append(reading)
        while True:
            print('Reading saved.')
            reading = input("Enter the Next Reading: ")

            if reading == "":
                break
            list_readings.append(reading)

        print('\nResults Summary')
        No_Of_Reading = len(list_readings)
        if (No_Of_Reading == 1):
            print(f'{No_Of_Reading} Reading Analysed.')

        elif (No_Of_Reading > 1):
            print(f'{No_Of_Reading} Readings Analysed.')

        mph_list = []
        for i in list_readings:
            i = i.upper()
            speed1 = i.startswith('E')
            speed2 = i.startswith('U')

            if (speed1 == True):
                U_mph = float(i[1:])/conversion
                mph_list.append(U_mph)

            elif (speed2 == True):
                U_mph = float(i[1:])
                mph_list.append(U_mph)

        if (mph_list != []):
            max_value = max(mph_list)
            print(
                f"Max speed:{max_value:.1f} MPH, {(max_value*conversion):.1f} KPH")
            min_value = min(mph_list)
            print(
                f"Min speed:{min_value:.1f} MPH, {(min_value*conversion):.1f} KPH")
            ave_value = mean(mph_list)
            print(
                f"Avg speed:{ave_value:.1f} MPH, {(ave_value*conversion):.1f} KPH")


swallow_speed()
