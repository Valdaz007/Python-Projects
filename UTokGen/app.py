import csv
import random

line1 = []
line2 = []
line3 = []
line4 = []

def randomNum():
	return random.randrange(0, 18, 1)

def get_data():
	with open("utokgen.csv", "r") as file:
		reader = csv.DictReader(file)
		
		for row in reader:
			line1.append(row["line1"])
			line2.append(row["line2"])
			line3.append(row["line3"])
			line4.append(row["line4"])

def utokgen():
	print(line1[randomNum()], line2[randomNum()], line3[randomNum()], line4[randomNum()], sep=" ")

def main():
	get_data()
	utokgen()


if __name__ == "__main__":
	main()
