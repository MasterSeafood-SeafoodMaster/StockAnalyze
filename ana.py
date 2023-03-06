import Stock as s
import yfinance as yf
import csv

with open('StockIdList.csv', newline='', encoding='utf_8_sig') as csvfile:
	rows = csv.reader(csvfile)
	for row in rows:

		#print(row)
		result = s.Analyze(row[1], row[0]+".TW", "2y")
		if result=="dont":
			pass
		elif result=="nodata":
			print(result)
		elif result[0]=="very high":
			with open("df_High.txt", "a", encoding='utf_8_sig') as myfile:
				print(row[0], row[1])
				print(result[0])
				for i in range(1, len(result)):
					myfile.write(str(result[i]))
					myfile.write(',')
				myfile.write(str( round((result[3] - result[5])/result[3], 4) ))
				myfile.write("\n")
		elif result[0]=="very low":
			with open("df_Low.txt", "a", encoding='utf_8_sig') as myfile:
				print(row[0], row[1])
				print(result[0])
				for i in range(1, len(result)):
					myfile.write(str(result[i]))
					myfile.write(',')
				myfile.write(str( round((result[3] - result[5])/result[3], 4) ))
				myfile.write("\n")



			

