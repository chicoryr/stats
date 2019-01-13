def both():
    done0 = False
    kills = 0
    errors = 0
    attempts = 0
    zeros = 0
    ones = 0
    twos = 0
    threes = 0
    total_passes = 0
    while not done0:
        current = input("Enter k for a kill, e for an error, a for an attempt. Stat passing as you go."
                        " Type done when finished: ")
        if current == "k":
            kills += 1
            attempts += 1
        if current == "e":
            errors += 1
            attempts += 1
        if current == "a":
            attempts += 1
        if current == "0":
            zeros += 1
        if current == "1":
            ones += 1
            total_passes += 1
        if current == "2":
            twos += 1
            total_passes += 2
        if current == "3":
            threes += 1
            total_passes += 3
        if current == "done":
            done0 = True
            print("\n")
            print("\n")
            if attempts > 0:
                hit_perc = (round(((kills - errors) / attempts) * 1000) / 10)
                if hit_perc < 60:
                    print("Do better, " + str(name) + ". You got " + str(kills) + " kills, " + str(
                        errors) + " errors in " + str(attempts) + " attempts, for a hitting percentage of "
                          + str(hit_perc))
                else:
                    print("Good job, " + name + "! You got " + str(kills) + " kills, " + str(errors) + " errors in "
                          + str(
                        attempts) + " attempts, for a hitting percentage of " + str(hit_perc))
            if attempts == 0:
                print("Why didn't you get set, " + name + "?")
            if (zeros + ones + twos + threes) > 0:
                pass_avg = ((round(total_passes / (zeros + ones + twos + threes) * 100)) / 100)
                if pass_avg > 2:
                    print("Good job, " + name + ", you passed a " + str(pass_avg))
                if pass_avg < 2:
                    if pass_avg > 1.5:
                        print("Almost, " + name + ", you passed a " + str(pass_avg))
                if pass_avg < 1.5:
                    print("Not good, " + name + ", you passed a " + str(pass_avg))
            if (zeros + ones + twos + threes) == 0:
                print("Did they not serve you?")


def hitting():
    done1 = False
    kills = 0
    errors = 0
    attempts = 0
    while not done1:
        current = input("Enter k for a kill, e for an error, a for an attempt, type done when finished: ")
        if current == "k":
            kills += 1
            attempts += 1
        if current == "e":
            errors += 1
            attempts += 1
        if current == "a":
            attempts += 1
        if current == "done":
            done1 = True
            hit_perc = (round(((kills - errors) / attempts) * 1000) / 10)
            print("\n")
            if hit_perc < 60:
                print("Do better, " + str(name) + ". You got " + str(kills) + " kills, " + str(
                    errors) + " errors in " + str(attempts) + " attempts, for a hitting percentage of " + str(hit_perc))
            else:
                print("Good job, " + name + "! You got " + str(kills) + " kills, " + str(errors) + " errors in " + str(
                    attempts) + " attempts, for a hitting percentage of " + str(hit_perc))


def passing():
    done2 = False
    zeros = 0
    ones = 0
    twos = 0
    threes = 0
    total_passes = 0
    while not done2:

        current = input("Stat each pass as you go, type done when finished: ")
        if current == "0":
            zeros += 1
        if current == "1":
            ones += 1
            total_passes += 1
        if current == "2":
            twos += 1
            total_passes += 2
        if current == "3":
            threes += 1
            total_passes += 3
        if current == "done":
            done2 = True
            pass_avg: float = ((round(total_passes / (zeros + ones + twos + threes) * 100)) / 100)
            print("\n")
            if pass_avg > 2:
                print("Good job, " + name + ", you passed a " + str(pass_avg))
            if 2 > pass_avg > 1.5:
                print("Almost, " + name + ", you passed a " + str(pass_avg))
            if pass_avg < 1.5:
                print("Not good, " + name + ", you passed a " + str(pass_avg))


def stat1() -> object:
    repeat = False
    while not repeat:
        stat = input("Are you statting hitting, passing or both? ")
        if stat == "hitting":
            hitting()
            repeat = True
        if stat == "passing":
            passing()
            repeat = True
        if stat == "both":
            both()
            repeat = True


name = input("Enter player name: ")

stat1()
