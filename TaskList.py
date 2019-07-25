activityName = []
startTime = []
endTime = []
TASKLIST = ['work,0650,0730',
          'read,1100,1115',
          'play,1210,1250',
          'read,1515,1530',
          'eat,1130,1430',
          'run,1750,1930',
          'eat,2000,2100',
          'play,1800,2100']


# stores each element of TASKLIST into categorized list
def store():
    for i in range(len(TASKLIST)):
        temp = (TASKLIST[i].split(","))
        activityName.append(temp[0])
        startTime.append(temp[1])
        endTime.append(temp[2])


def print_activity_name():
    name_list = []
    for i in range(len(activityName)):
        name_list.append(activityName[i])
    print(name_list)


def print_unique_list():
    unique = []
    for x in activityName:
        if x not in unique:
            unique.append(x)
    print(unique)


def calculate_duration():
    duration_list = []
    for i in range(len(startTime)):
        # splits the startTime and endTime in half to create hours and minutes
        start_hour = startTime[i][0:len(startTime[i]) // 2]
        start_min = startTime[i][len(startTime[i]) // 2:len(startTime[i])]
        end_hour = endTime[i][0:len(endTime[i]) // 2]
        end_min = endTime[i][len(endTime[i]) // 2:len(startTime[i])]
        # checks for difference in minutes, without having to convert hours to minutes
        if int(end_min) - int(start_min) > 0:
            # stores time in minutes only if there is no difference in hours
            if int(end_hour)-int(start_hour) == 0:
                duration_list.append(str(int(end_min)-int(start_min))+" Minutes")
            else:
                # stores time difference
                duration_list.append(str(int(end_hour)-int(start_hour))+" Hour "
                                     + str(int(end_min)-int(start_min))+" Minutes")
        # Must convert an hour to minutes, by subtracting one hour
        else:
            # if no difference in minutes, just print difference in hours
            if int(end_min) - int(start_min) == 0:
                duration_list.append(str(int(end_hour) - int(start_hour))+" Hours")
            else:
                # Subtracts one hour and adds sixty minutes
                if int(end_hour) - 1 - int(start_hour) == 0:
                    duration_list.append(str((int(end_min)+60) - int(start_min))+" Minutes")
                else:
                    duration_list.append(str(((int(end_hour) - 1) - int(start_hour)))+" Hour "
                                         + str((int(end_min)+60) - int(start_min))+" Minutes")
    print(duration_list)


def find_overlap():
    over_lap_list = []
    for i in range(len(activityName)):
        start_time1 = startTime[i]
        end_time1 = endTime[i]

        for j in range(len(activityName)):
            # prevents comparison against itself
            if i == j:
                    continue
            else:
                start_time2 = startTime[j]
                end_time2 = endTime[j]

        # if initial task time is contained within the second task time
            if int(start_time1) <= int(start_time2) & int(start_time2) <= int(end_time1):
                over_lap_list.append(str(TASKLIST[i])+" overlaps with "+TASKLIST[j])

        # Considers the case if time over laps EG [walk,2100,0100] and [jog, 2300,0200]
        # or [walk,2100,0100] and [jog, 0005,0200]
            if (int(end_time1) - int(start_time1)) < 0:
                if 2400 >= int(start_time2) >= int(start_time1):
                    over_lap_list.append(str(TASKLIST[i]) + " overlaps with " + TASKLIST[j])
                if 0000 <= int(start_time2) <= int(end_time1):
                    over_lap_list.append(str(TASKLIST[i]) + " overlaps with " + TASKLIST[j])
    print(over_lap_list)


if __name__ == '__main__':
    store()
    print_activity_name()
    print_unique_list()
    calculate_duration()
    find_overlap()

