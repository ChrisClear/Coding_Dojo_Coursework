#pylint: disable=C0103
def getRandom():
    import random
    random_num = 0
    random_num = random.randint(60, 100)
    return random_num


def scores_and_grades():
    """Assignment: Scores and Grades
    Write a function that generates ten scores between 60 and 100. Each time a score is generated,
    your function should display what the grade is for a particular score. Here is the grade table:

    Score: 60 - 69; Grade - D
    Score: 70 - 79; Grade - C
    Score: 80 - 89; Grade - B
    Score: 90 - 100; Grade - A
    """
    i = 0
    numberofgrades = 20
    while i < numberofgrades:
        grade = int(getRandom())
        if int(grade) >= 60 and int(grade) <= 69:
            print "Score: "+str(grade)+"; Grade - A"
            i += 1
        elif int(grade) >= 70 and int(grade) <= 79:
            print "Score: "+str(grade)+"; Grade - B"
            i += 1
        elif int(grade) >= 80 and int(grade) <= 89:
            print "Score: "+str(grade)+"; Grade - C"
            i += 1
        elif int(grade) >= 90 and int(grade) <= 100:
            print "Score: "+str(grade)+"; Grade - D"
            i += 1
        else:
            pass

    print "End of the program. Bye!"

scores_and_grades()


