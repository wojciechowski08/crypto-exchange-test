import random


def getNewRate(currentRate, fluctuation) -> float:
    tempPreviousRate: int = currentRate
    newRate: int = currentRate
    for minute in range(60):
        for second in range(60):
            if newRate >= tempPreviousRate:
                if random.randint(0, 1000) < 607:
                    tempPreviousRate = newRate
                    newRate = newRate * (1 + fluctuation)
                    # print("o")
                else:
                    tempPreviousRate = newRate
                    newRate = newRate * (1 - fluctuation)
                    # print("oo")
            else:
                if random.randint(0, 100) > 60:
                    tempPreviousRate = newRate
                    newRate = newRate * (1 + fluctuation)
                    # print("ooo")
                else:
                    tempPreviousRate = newRate
                    newRate = newRate * (1 - fluctuation)
                    # print("oooo")

            chance = random.randint(1, 100000000)
            if chance < 1 * 5:
                tempPreviousRate = newRate
                if random.randint(0, 100) < 50:
                    newRate = newRate * (1 + fluctuation * 50000)
                    print("BIG STONKS")
                else:
                    newRate = newRate * (1 - fluctuation * 50000)
                    print("SAY SIKE RN")
            elif chance < 10 * 5:
                tempPreviousRate = newRate
                if random.randint(0, 100) < 50:
                    newRate = newRate * (1 + fluctuation * 10000)
                    print("STONKS")
                else:
                    newRate = newRate * (1 - fluctuation * 10000)
                    print("YIKES")
            elif chance < 1000 * 3:
                tempPreviousRate = newRate
                if random.randint(0, 100) < 50:
                    newRate = newRate * (1 + fluctuation * 100)
                else:
                    newRate = newRate * (1 - fluctuation * 100)
                # print("FUNKY!")

        # print(str(minute) + ": " + str(newRate))
    return newRate


def timePassage(hours: int, cr, f):
    day = 0
    riseCount = 0
    fallCount = 0
    lastDayRate = cr
    for hour in range(hours):
        lastRate = cr
        cr = getNewRate(cr, f)


        # print(str(hour) + ": " + str(cr))
        # if hour % 24 == 0:
        #     tempString = "--- Day " + str(day) + ": " + str(cr) + " ---"
        #     day += 1
        #     if cr > lastDayRate:
        #         tempString += "\033[92m {}\033[00m".format("RISE")
        #         riseCount += 1
        #     else:
        #         tempString += "\033[91m {}\033[00m".format("FALL")
        #         fallCount += 1
        #     lastDayRate = cr
        #     print(tempString)


        tempString = "--- Hour " + str(hour) + ": " + str(cr) + " ---"
        day += 1
        if cr >= lastRate:
            tempString += "\033[92m {}\033[00m".format("RISE")
            riseCount += 1
        else:
            tempString += "\033[91m {}\033[00m".format("FALL")
            fallCount += 1
        print(tempString)

    print("UPS: " + str(riseCount))
    print("DOWNS: " + str(fallCount))
    print(riseCount / fallCount)




def main():
    # getNewRate(28948.0548, 0.0002757120362432‬)
    # getNewRate(29000, 0.00001)
    rate = 29000
    fluctuation = 0.00001
    timePassage(24 * 30, rate, fluctuation)


main()
