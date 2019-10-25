
#imprt csv
import csv


with open('data.csv') as csvfile:
        readit = csv.reader(csvfile, delimiter=',')


        colors=[]
        categorys=[]
        data=[]
        for row in readit:
                print(row)

                category = str(row[0])
                data1 = str(row[1])
                data2 = str(row[2])
                data3 = int(row[3])
                data4 = str(row[4])

                color = str(row[4])
                category = row[0]

                colors.append(color)
                categorys.append(category)
                
                data.append([category,data1,data2,data3,data4])
                
        print(data)
        print(colors)
        print(categorys)

        try:
                
                whatcolor = raw_input('What color do You Want..')
                if whatcolor in colors:
                        #use input for python version greater than 3
                        col = colors.index(whatcolor.lower())
                        print(col)
                        print(categorys[col])
                else:
                        print('Color not found,or it is not a color')
                
        except Exception as e:
                print(e)

        print('contuining')
        

	
