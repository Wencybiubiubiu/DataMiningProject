import numpy
import pandas
import sys

#input_file = str(sys.argv[1])
#output_file = str(sys.argv[2])

#global variable

data_type = [] #data categories
data_contents = [] #contents for each participants
convert_type_to_index = {}


#delete quote for specific type of data
def process_quote(process_type):

	for each_row in range(len(data_contents)):
		cur_item = data_contents[each_row][convert_type_to_index[process_type]]
		cur_item = str(cur_item)
		data_contents[each_row][convert_type_to_index[process_type]] = cur_item
	return 

#Use label encoding to convert the categorical values in columns gender, race, race o and field 
#to numeric values start from 0.
def encoding(process_type):
	category = []
	category_encoding_dict = {}
	for each_row in range(len(data_contents)):
		cur_item = data_contents[each_row][convert_type_to_index[process_type]]
		if cur_item not in category:
			category.append(cur_item)

	category = sorted(category)
	for i in range(len(category)):
		category_encoding_dict[category[i]] = i

	for each_row in range(len(data_contents)):
		cur_item = data_contents[each_row][convert_type_to_index[process_type]]
		matching_label = category_encoding_dict[cur_item]
		data_contents[each_row][convert_type_to_index[process_type]] = matching_label
	#print(category_encoding_dict)
	return category_encoding_dict



if __name__ == '__main__':

	#firstly, read the data file
	df = pandas.read_csv ('data.csv', sep=',',header=None)

	data_type = df.values[0]
	data_contents=df.values[1:]
	preprocessed_data = df.values

	#match each type with corresponding index
	for i in range(len(data_type)):
		convert_type_to_index[data_type[i]] = i

	#Processing data question 3: encoding
	for each_type in data_type:
		if(each_type != 'TripType' and each_type != 'ScanCount'):
			print(each_type)
			process_quote(each_type)
			encoding(each_type)

	preprocessed_data[1:] = data_contents

	pandas.DataFrame(preprocessed_data).to_csv('preprocessed_data.csv', header=None, index=None)
















