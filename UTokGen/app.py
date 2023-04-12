import random as rd
import pandas as pd

def rdNum() -> int:
	return rd.randrange(0, 18)

def get_data():
	df = pd.read_csv('utokgen.csv')

def utokgen():
	print(df['line1'][rdNum()], df['line2'][rdNum()], df['line3'][rdNum()], df['line4'][rdNum()], sep=" ")

def main():
	get_data()
	utokgen()

if __name__ == "__main__":
	main()
