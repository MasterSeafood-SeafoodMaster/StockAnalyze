import Stock as s
import yfinance as yf
import csv

with open('StockIdList.csv', newline='') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:

		#print(row)
		result = s.Analyze(row[0]+".TW", "2y")
		if result=="dont":
			pass
		elif result=="nodata":
			print(result)
		else:
			with open("df.txt", "a") as myfile:
				print(result[0])
				for i in range(1, len(result)):
					myfile.write(str(result[i]))
					myfile.write(',')
				myfile.write(str( round((result[2] - result[4])/result[2], 4) ))
				myfile.write("\n")



			

