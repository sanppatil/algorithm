
def power(num, pwr):
    if pwr == 0:
        return 1
    else:
        return num * power(num, pwr-1)

print ("{} to power of {} is {}.".format(10,3, power(10,3)))