while True:
    year = int(input("Enter a year "))

    if year % 4 == 0:
        print ("The year {} is a leap year".format (year))

    else:
        print ("The year {} is not a leap year".format (year))
