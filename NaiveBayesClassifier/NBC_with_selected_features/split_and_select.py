import numpy
import pandas
import matplotlib.pyplot as plt
import sys

input_file = 'data.csv'
output_train_file = 'train.csv'
output_test_file = 'test.csv'

#global variable

data_type = [] #data categories
data_contents = [] #contents for each participants
convert_type_to_index = {}


if __name__ == '__main__':

	#firstly, read the data file
	df = pandas.read_csv (input_file, sep=',')
	df = df.drop('FinelineNumber',1)

	test = df.sample(frac=0.2, random_state=47)

	train = df.drop(test.index)


	pandas.DataFrame(train).to_csv(output_train_file, index=None)
	pandas.DataFrame(test).to_csv(output_test_file, index=None)