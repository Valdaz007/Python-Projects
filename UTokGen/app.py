import csv, random

dictLine = {1:[], 2:[], 3:[], 4:[]}

def randomNum():
	return random.randrange(0, 18, 1)

def get_data():
	with open("utokgen.csv", "r") as file:
		reader = csv.DictReader(file)
		for row in reader:
			for i in range(1,5):
				dictLine[i].append(row[f"line{i}"])

def utokgen():
	print(dictLine[1][randomNum()], dictLine[2][randomNum()], dictLine[3][randomNum()], dictLine[4][randomNum()], sep=" ")

def main():
	get_data()
	utokgen()

if __name__ == "__main__":
	main()
