import pandas as pd 
import csv
#script to generate 4D data for jets with kinematic parameters
with open('4d_data.csv', 'w', newline='') as w_file:
    writer = csv.writer(w_file)
    writer.writerow(["Event details", "Object", "E", "pt", "eta", "phi"])

    #monojet_Zp2000.0_DM_50.0_chan3.csv
    with open('monojet_Zp2000.0_DM_50.0_chan3.csv','r') as data:
        reader=csv.reader(data)
        for rows in reader:
            #split first column
            x=rows[0].split(";")
            event=x[0]+";"+x[1]+";"+x[2]+";"+x[3]+";"+x[4]
            obj=x[5]
            include=0
            if(obj=="j"):                   #if event contains jet, we include the event
                include=1
                cols=1
            else:
                for i in range(4,len(rows),4):
                    x=rows[i].split(";")
                    if(x[1]=="j"):
                        include=1
                        cols=i+1
                        obj=x[1]
                        break
            #for other columns
            if(include==1):                         #event contains atleast one jet
                while cols < len(rows):
                    x=rows[cols+3].split(";")
                    if(include==1):                 #including only if jet is present in event
                        writer.writerow([event,obj,rows[cols],rows[cols+1],rows[cols+2],x[0]])
                    obj=x[1]
                    if(obj!="j"):
                        include=0
                    else:
                        include=1
                    cols=cols+4

