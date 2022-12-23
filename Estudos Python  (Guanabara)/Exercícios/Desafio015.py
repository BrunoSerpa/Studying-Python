KmTraveled = float(input("insert the number of Km traveled:\n"))
DaysAlugadde = int(input("insert how days it will is rented the car:\n"))
Payable = DaysAlugadde * 60 + KmTraveled * 0.15
print('To rent a car for {} days with {:.2f} km traveled you will pay ${}'.format(DaysAlugadde, KmTraveled,Payable))