from sys import argv

#ranks = [33,3538,8332,226,503,2834,3175,3641,4130,2832,6861,8728,7178,68,6120,3604,308,830,4395,240,8424,9998,3655,8832,1528]
#oprRanks:
ranks = [226,1528,33,503,6120,3641,2834,240,9998,8728,3655,8332,4395,830,68]


schedule = "8832 3604 8424 9998 6120 503\n\
33 1528 226 8728 8332 3655\n\
240 2834 3641 4395 68 830\n\
3538 3175 1528 226 503 4130\n\
68 9998 2834 8728 33 830\n\
8832 240 4130 3655 3175 3641\n\
4395 3538 8424 8332 3604 6120\n\
8832 1528 3175 33 503 3655\n\
68 3538 226 3604 3641 4395\n\
8424 8728 9998 4130 830 6120\n\
2834 8332 8832 240 3538 3604\n\
3175 8728 4395 6120 3641 33\n\
830 3655 68 8332 503 2834\n\
240 226 8424 1528 4130 9998\n\
3641 68 8728 3538 3655 8332\n\
503 8832 1528 240 4395 9998\n\
8424 226 3175 2834 4130 33\n\
830 8832 3604 6120 1528 4395\n\
9998 3641 8332 3655 2834 8424\n\
3175 68 503 6120 226 3538\n\
4130 33 3604 8728 830 240\n\
9998 2834 3538 226 4395 3655\n\
33 3175 240 8424 68 1528\n\
4130 6120 8332 503 3604 8728\n\
3641 3538 8832 830 1528 2834\n\
33 8424 240 503 4395 3655\n\
830 8332 226 8832 8728 6120\n\
3641 4130 3175 3604 9998 68\n\
8424 830 503 3538 8728 2834\n\
226 3655 6120 3641 240 1528\n\
68 8332 4130 4395 8832 33\n\
3175 9998 830 1528 3655 3604\n\
226 8832 3641 4130 8424 8728\n\
9998 33 68 3604 503 3538\n\
2834 6120 3175 8332 4395 240\n\
3538 830 33 3655 9998 8832\n\
8332 8424 3641 3604 3175 503\n\
8728 2834 226 6120 240 68\n\
1528 33 8332 4395 4130 3538\n\
503 3641 830 3175 226 9998\n\
68 6120 8832 3655 240 4130\n\
1528 8424 8728 2834 3604 4395"

def getRank(teamNumber: int):
    try:
        return ranks.index(teamNumber)
    except ValueError:
        return 20

schedule = schedule.split("\n")
argv = argv[1:]

if len(argv) > 0:
    matchNumber = int(argv[0])-1
else:
    for matchNumber in range(len(schedule)):
        red = schedule[matchNumber].split(" ")[0:3]
        for i in range(len(red)):
            red[i] = int(red[i])
        blue = schedule[matchNumber].split(" ")[3:6]
        for i in range(len(blue)):
            blue[i] = int(blue[i])

        total = 0

        for i in red:
            total += getRank(i)

        redScore = total/len(red)
        #print("Red Score: " + str(redScore))

        total = 0

        for i in blue:
            total += getRank(i)

        blueScore = total/len(blue)
        #print("Blue Score: " + str(blueScore))

        if blueScore < redScore:
            #print("Winners: \033[0;34m" + str(blue) + "\033[39m")
            print("Blue Win")
        elif redScore < blueScore:
            #print("Winners: \033[0;31m" + str(red) + "\033[39m")
            print("Red Win")
        elif redScore == blueScore:
            print("Tie")
            #print("It's a tie")

