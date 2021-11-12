#Eduard Brozmann #05.11.2021 #

import math
jahr = 2000


if (jahr % 4 == 0 ) and (jahr % 100 != 0) or (jahr % 400 == 0):     # == vergleicht != ungleich 
     print(jahr, "ist ein schaltjahr")
else:
    print(jahr, "ist kein schaltjahr")


#Erstellen Sie eine Liste mit allen Schaltjahren von 1800 bis 2100. Geben Sie die Liste anschließend aus.


for i in range(1800,2101):
    if (i % 4 == 0 ) and (i % 100 != 0) or (i % 400 == 0):
        print(i,"ist ein schaltjahr")
        
else:
       print(i,"ist kein schaltjahr")
          
    #10

    
     
        
   
        



    
 


