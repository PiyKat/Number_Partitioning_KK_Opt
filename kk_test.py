# CS124, Programming Assignment 3
# Dino Rodriguez & Colton Gyulay


### Tests

# libraries
import kk_library as KK
import kk as Main
import csv
import time
import progressbar
import timeit


# test differencing approach (maintaining order)
def diffKKTest():
    A = [10, 8, 7, 6, 5]
    residue = KK.diffKK(A, not Main.flag)
    assert(residue == 2)

# test prepartition conversion then differencing approach
def prepartitionTest():
    A = [10, 8, 7, 6, 5]
    P = [1, 2, 2, 4, 5]
    residue = KK.prepartitionResidue(A, P)
    assert(residue == 4)

# confirm that residuals of both methods given equivalent solutions line up
def residualsTest():
    A = KK.randomSet(10, not Main.flag)
    S = KK.randomStandardRep(A)
    P = KK.transformStandard(S)
    assert(KK.standardResidue(A, S) == KK.prepartitionResidue(A, P))

# function to get numerical data over multiple runs
def algoTest():

    max_iter = 25000 # use 25000 for actual trials
    row = ["KK", "SRep_Rand_No_Part", "Hill_Climb_No_Part", "Annealing_No_Part",
           "Rep_Rand_Part", "Hill_Climb_Part", "Annealing_Part"]

    print("\n\nEach trial uses the same array and initialization\n\n");
    print("Trial & KK & Rep_Rand_No_Part & Hill_Climb_No_Part & Annealing_No_Part & Rep_Rand_Part & Hill_Climb_Part & Annealing_Part \\\\ \n");
    with open("data.csv", "wt") as csv_file:
        # build csv writer and progress bar
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(row)
        bar = progressbar.ProgressBar()

        for i in range(100): # switch to 100 for actual trials
            # show progressbar
            time.sleep(0.02)

            # get row
            A = KK.randomSet(100, not Main.flag) # generate random A
            row[0] = KK.diffKK(A, not Main.flag) # run KK
            row[1] = KK.repRandom(A, max_iter, 's', not Main.flag)

            row[2] = KK.hillClimb(A, max_iter, 's', not Main.flag)
            row[3] = KK.simAnneal(A, max_iter, 's', not Main.flag)
            row[4] = KK.repRandom(A, max_iter, 'p', not Main.flag)
            row[5] = KK.hillClimb(A, max_iter, 'p', not Main.flag)
            row[6] = KK.simAnneal(A, max_iter, 'p', not Main.flag)

            # insert into data list
            writer.writerow(row)
            print("%d & %d & %d & %d & %d & %d & %d & %d \\\\ " % (i + 1, row[0], row[1],row[2],row[3],row[4],row[5],row[6]))


# function to get timing data over multiple runs
def timingTest():
    max_iter = 25000 # use 25000 for actual trials
    row = ["KK", "SRep_Rand_No_Part", "Hill_Climb_No_Part", "Annealing_No_Part",
           "Rep_Rand_Part", "Hill_Climb_Part", "Annealing_Part"]


    with open("timing.csv", "wt") as csv_file:

        writer = csv.writer(csv_file, delimiter=',')
        writer.writerow(row)
        bar = progressbar.ProgressBar()
        print(
            "Trial & KK & Rep_Rand_No_Part & Hill_Climb_No_Part & Annealing_No_Part & Rep_Rand_Part & Hill_Climb_Part & Annealing_Part \\\\ \n");
        for i in range(100):

                # show progressbar
                time.sleep(0.02)

                # get row
                A = KK.randomSet(100, not Main.flag) # generate random A

                start = time.time()
                KK.diffKK(A, not Main.flag) # run KK
                end = time.time()
                row[0] = (end - start)

                
                start = time.time()
                KK.repRandom(A, max_iter, 's', not Main.flag)
                end = time.time()
                row[1] = (end - start)

                start = time.time()
                KK.hillClimb(A, max_iter, 's', not Main.flag)
                end = time.time()
                row[2] = (end - start)

                start = time.time()
                KK.simAnneal(A, max_iter, 's', not Main.flag)
                end = time.time()
                row[3] = (end - start)

                start = time.time()
                KK.repRandom(A, max_iter, 'p', not Main.flag)
                end = time.time()
                row[4] = (end - start)

                start = time.time()
                KK.hillClimb(A, max_iter, 'p', not Main.flag)
                end = time.time()
                row[5] = (end - start)

                start = time.time()
                KK.simAnneal(A, max_iter, 'p', not Main.flag)
                end = time.time()
                row[6] = (end - start)


                # insert into data list
                writer.writerow(row)
                print("%d & %d & %d & %d & %d & %d & %d & %d \\\\ " % (
                i + 1, row[0], row[1], row[2], row[3], row[4], row[5], row[6]) )

### Running Tests

#diffKKTest()
#prepartitionTest()
#residualsTest()
algoTest()
timingTest()
