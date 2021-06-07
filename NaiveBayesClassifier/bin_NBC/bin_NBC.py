import numpy
import pandas
import matplotlib.pyplot as plt

#global variable

raw_data_file = 'data.csv'
train_data_file = 'train.csv'
test_data_file = 'test.csv'

data_type = [] #data categories
data_contents = [] #contents for each participants
convert_type_to_index = {}

#unchanged parameters
chosen_fraction = 1
chosen_random_state = 47

class_label = 'TripType'

lower_limit = 0
upper_limit = 1
number_of_bins = [2,3,4,5,6,10]

range_dict = {}

continuous_variables = ['ScanCount']
variable_range = [0,0]


#other variables are all falling in range of [0,10]

def find_matching_bins(range_array,input_value,input_value_of_numBins):
	index = input_value_of_numBins-1
	#if(input_value == range_array[len(range_array)-1]):
	#	return index
	if(input_value == range_array[0]):
		return 0

	for i in range(1,len(range_array)):
		if(input_value > range_array[i-1] and input_value <= range_array[i]):
			index = i-1
	return index
	
def find_matching_bins_for_all_rows(range_array,process_type, input_value_of_numBins):
	count_array = numpy.full(input_value_of_numBins,0)#[0,0,0,0,0]
	#temp = 0
	#print(len(data_contents))
	for each_row in range(len(data_contents)):
		#temp += 1
		cur_item = float(data_contents[each_row][convert_type_to_index[process_type]])

		match_index = find_matching_bins(range_array,cur_item,input_value_of_numBins)
		#if(process_type == 'age' and match_index == 3):
		#	print(temp)
		data_contents[each_row][convert_type_to_index[process_type]] = match_index

		count_array[match_index] += 1
	#print(numpy.sum(count_array))
	return count_array


def get_random_sample_from_training_set(t_frac,train):

	df = pandas.read_csv (train_data_file, sep=',')

	random_sample = df.sample(frac=t_frac, random_state=chosen_random_state)

	return random_sample.values

def get_possible_values_for_each_label(process_type, input_data):

	possible_values = []
	possible_values_frequency_dict = {}

	#print(input_data, len(input_data))
	for each_row in range(len(input_data)):
		cur_item = input_data[each_row][convert_type_to_index[process_type]]
		if cur_item not in possible_values:
			possible_values.append(cur_item)
			possible_values_frequency_dict[cur_item] = 0

	for each_row in range(len(input_data)):
		cur_item = input_data[each_row][convert_type_to_index[process_type]]
		#print(cur_item)
		possible_values_frequency_dict[cur_item] += 1
	#print(possible_values)
	return possible_values, possible_values_frequency_dict

def get_probability_table_for_each_label(process_type, input_data, label_list, label_list_count):

	#count_check = 0
	possible_values = []
	possible_values_frequency_dict = {}
	#separate to different dicts corresponding to different class labels
	for each_possible_value in label_list:
		possible_values_frequency_dict[each_possible_value] = {}

	#print(input_data, len(input_data))
	for each_row in range(len(input_data)):
		cur_item = input_data[each_row][convert_type_to_index[process_type]]
		if cur_item not in possible_values:
			possible_values.append(cur_item)
			for each_possible_value in label_list:
				possible_values_frequency_dict[each_possible_value][cur_item] = 0

	for each_row in range(len(input_data)):
		cur_item = input_data[each_row][convert_type_to_index[process_type]]
		cur_label = input_data[each_row][convert_type_to_index[class_label]]
		#print(cur_item)
		possible_values_frequency_dict[cur_label][cur_item] += 1
		#count_check += 1
	#print(possible_values)
	#print(count_check)

	for each_label_value in label_list:
		for each_possible_value in possible_values:
			cur_count = possible_values_frequency_dict[each_label_value][each_possible_value]
			if(cur_count == 0):
				possible_values_frequency_dict[each_label_value][each_possible_value] = float(1/len(possible_values))
				#possible_values_frequency_dict[each_label_value][each_possible_value] = float(cur_count/label_list_count[each_label_value])
			else:
				possible_values_frequency_dict[each_label_value][each_possible_value] = float((cur_count+1)/(label_list_count[each_label_value]+len(possible_values)))
	return possible_values, possible_values_frequency_dict

def calculate_probability_for_labels(label_list,label_list_count, total_length):
	prob_label = {}
	for cur_label in label_list:
		prob_label[cur_label] = label_list_count[cur_label]/total_length
	return prob_label

def nbc(t_frac,train):

	input_data = get_random_sample_from_training_set(t_frac,train)
	label_list, label_list_count = get_possible_values_for_each_label(class_label, input_data)
	#print(label_list, label_list_count)

	#initialize probability table for each feature and class
	probability_table = {}
	for each_possible_value in label_list:
		probability_table[each_possible_value] = {}
	#separate to different dicts corresponding to different class labels
	for each_type in data_type:
		if(each_type != class_label):
			possible_values_for_cur_type, possible_values_count_for_cur_type = get_probability_table_for_each_label(each_type, 
					input_data, label_list, label_list_count)
			for each_possible_value in label_list:
				#probability_table[each_possible_value] = {}
				probability_table[each_possible_value][each_type] = possible_values_count_for_cur_type[each_possible_value]

	#print(probability_table)

	#get P(y) for each possible value of y
	label_probability_dict = calculate_probability_for_labels(label_list,label_list_count, len(input_data))

	#print(label_probability_dict)

	return label_list,label_probability_dict, probability_table


def infer_single_label(single_data,label_list,label_probability_dict, probability_table):
	probability_for_all_labels = []
	product = 1
	for cur_label in label_list:
		for cur_type in data_type:
			if(cur_type != class_label):
				#print("cur_label",cur_label)
				#print("cur_type",cur_type)
				#print("single_data",single_data)
				#print("convert_type_to_index[cur_type]",convert_type_to_index[cur_type])
				#print("single_data[convert_type_to_index[cur_type]]",single_data[convert_type_to_index[cur_type]])
				multiplier = 0
				#print(cur_type,convert_type_to_index[cur_type])
				#print(single_data[7])
				#print(single_data[convert_type_to_index[cur_type]])
				#print(probability_table[cur_label][cur_type])
				if(single_data[convert_type_to_index[cur_type]] not in probability_table[cur_label][cur_type]):
					multiplier = 1/len(probability_table[cur_label][cur_type])
					#multiplier = 0
				else:
					multiplier = probability_table[cur_label][cur_type][single_data[convert_type_to_index[cur_type]]]
				product = product * multiplier
		product = product * label_probability_dict[cur_label]
		probability_for_all_labels.append(product)
		product = 1
	probability_for_all_labels = probability_for_all_labels/numpy.sum(probability_for_all_labels)
	#print(probability_for_all_labels)
	#exit()
	return label_list[numpy.argmax(probability_for_all_labels)]

def infer_label(input_data,label_list,label_probability_dict, probability_table):
	correct = 0
	incorrect = 0
	for i in range(len(input_data)):
		real_label = input_data[i][convert_type_to_index[class_label]]
		predict_label = infer_single_label(input_data[i],label_list,label_probability_dict, probability_table)
		if(real_label == predict_label):
			correct += 1
		else:
			incorrect += 1
	
	return float(correct/(correct+incorrect))


if __name__ == '__main__':
	#test_count = 0
	#df = pandas.read_csv (raw_data_file, sep=',')
	#new_df = df.sample(frac=0.1, random_state=47)
	#pandas.DataFrame(new_df).to_csv(raw_data_file, index=None)

	train_accu_array = []
	test_accu_array = []

	df = pandas.read_csv (raw_data_file, sep=',')
	ScanCount = numpy.array(df[continuous_variables[0]])
	variable_range = [numpy.min(ScanCount),numpy.max(ScanCount)]
	#firstly, read the data file

	df = pandas.read_csv (raw_data_file, sep=',',header=None)

	data_type = df.values[0]
	data_contents=df.values[1:]
	#print(data_contents[1])
	preprocessed_data = df.values
	for cur_Bin in number_of_bins:

		#match each type with corresponding index
		for i in range(len(data_type)):
			convert_type_to_index[data_type[i]] = i

		for item in data_type:
			if(item in continuous_variables):
				range_dict[item] = variable_range
			else:
				range_dict[item] = 'not continuous'


		input_value_of_numBins = cur_Bin
		print("Bin size: " + str(input_value_of_numBins) + ".")
		for item in data_type:
			if(range_dict[item] != 'not continuous'):
				cur_range = range_dict[item]
				width = float(float(cur_range[upper_limit]-cur_range[lower_limit])/cur_Bin)
				cur_range_array = []
				for i in range(cur_Bin+1):
					cur_range_array.append(cur_range[lower_limit] + width*i)
				#print(cur_range_array)
				cur_count_array = find_matching_bins_for_all_rows(cur_range_array,item,input_value_of_numBins)
				#print("	" + str(item) + ": " + str(cur_count_array))
				#test_count += 1

		#print(data_contents[1])
		#print(test_count)


		preprocessed_data[1:] = data_contents

		df = pandas.DataFrame(data_contents)

		test = df.sample(frac=0.2, random_state=47)

		train = df.drop(test.index)

		pandas.DataFrame(test).to_csv(test_data_file, index=None)
		pandas.DataFrame(train).to_csv(train_data_file, index=None)

		#print(train,test)
		train_data = pandas.read_csv (train_data_file, sep=',').values
		label_list,label_probability_dict, probability_table = nbc(chosen_fraction,train_data)
		#print(probability_table)
		#print(train_data)
		train_accuracy = infer_label(train_data,label_list,label_probability_dict, probability_table)
		train_accuracy = train_accuracy#round(train_accuracy,2)
		train_accu_array.append(train_accuracy)
		print("Training Accuracy: "+str(train_accuracy))

		test_data = pandas.read_csv (test_data_file, sep=',').values
		#print(test_data)
		test_accuracy = infer_label(test_data,label_list,label_probability_dict, probability_table)
		test_accuracy = test_accuracy#round(test_accuracy,2)
		print("Testing Accuracy: "+str(test_accuracy))
		test_accu_array.append(test_accuracy)
		print("")

	p1 = plt.plot(number_of_bins, train_accu_array, color='red')
	p2 = plt.plot(number_of_bins, test_accu_array, color='green')
	plt.title('train/test accuracy for different number of bins')
	plt.legend((p1[0], p2[0]), ('train accuracy', 'test accuracy')) 
	plt.savefig('bin.png') 
	plt.close()


