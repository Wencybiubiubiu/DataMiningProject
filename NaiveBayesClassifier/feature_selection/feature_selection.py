import numpy
import pandas
import matplotlib.pyplot as plt
import itertools

#global variable
raw_data_file = 'data.csv'
train_data_file = 'train.csv'
test_data_file = 'test.csv'
data_type = [] #data categories
#input_data = [] #contents for each participants
convert_type_to_index = {}

#unchanged parameters
chosen_fraction = 1
chosen_random_state = 47

class_label = 'TripType'

def get_random_sample_from_training_set(t_frac):

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

	#print(possible_values_frequency_dict, len(possible_values_frequency_dict))

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
	
	#print(possible_values_frequency_dict, len(possible_values_frequency_dict))

	return possible_values, possible_values_frequency_dict

def calculate_probability_for_labels(label_list,label_list_count, total_length):
	prob_label = {}
	for cur_label in label_list:
		prob_label[cur_label] = label_list_count[cur_label]/total_length
	return prob_label

def nbc(t_frac):

	input_data = get_random_sample_from_training_set(t_frac)
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
		#print(input_data)
		#print(i)
		real_label = input_data[i][convert_type_to_index[class_label]]
		predict_label = infer_single_label(input_data[i],label_list,label_probability_dict, probability_table)
		#print(real_label,predict_label)
		if(real_label == predict_label):
			correct += 1
		else:
			incorrect += 1
	
	return float(correct/(correct+incorrect))

if __name__ == '__main__':


	#firstly, read the data file
	df = pandas.read_csv (raw_data_file, sep=',')
	#data_type = list(df.head())
	data_features = list(df.head())[1:]
	
	combinations_of_features = []
	for L in range(0, len(data_features)+1):
		for subset in itertools.combinations(data_features, L):
			if(len(subset) !=0 and len(subset) != len(data_features) != len(subset)):
				combinations_of_features.append(subset)
	#exit()

	chosen_data = df.sample(frac=0.1, random_state=47)

	#============================#

	all_training_accuracy = []
	all_test_accuracy = []

	for cur_drop_features in combinations_of_features:

		print("Features dropped: " + str(cur_drop_features))

		convert_type_to_index = {}
		data_after_dropping = None
		for each_drop_feature in cur_drop_features:
			data_after_dropping = chosen_data.drop(each_drop_feature,1)

		test = data_after_dropping.sample(frac=0.2, random_state=47)
		train = data_after_dropping.drop(test.index)


		pandas.DataFrame(train).to_csv(train_data_file, index=None)
		pandas.DataFrame(test).to_csv(test_data_file, index=None)

		#===========================#
		#below is model and prediction part#

		#firstly, read the data file
		df = pandas.read_csv (train_data_file, sep=',',header=None)
		#df = pandas.read_csv ('data/data-binned.csv', sep=',',header=None)

		data_type = df.values[0]

		#match each type with corresponding index
		for i in range(len(data_type)):
			convert_type_to_index[data_type[i]] = i


		print(convert_type_to_index)

		label_list,label_probability_dict, probability_table = nbc(chosen_fraction)
		#print(probability_table)
		train_data = pandas.read_csv (train_data_file, sep=',')#.values
		train_data = train_data.sample(frac=1, random_state=47).values[1:]

		#print(train_data)
		train_accuracy = infer_label(train_data,label_list,label_probability_dict, probability_table)
		#train_accuracy = round(train_accuracy,2)
		all_training_accuracy.append(train_accuracy)
		print("Training Accuracy: "+str(train_accuracy))

		test_data = pandas.read_csv (test_data_file, sep=',')#.values
		test_data = test_data.sample(frac=1, random_state=47).values[1:]
		#print(test_data)
		test_accuracy = infer_label(test_data,label_list,label_probability_dict, probability_table)
		#test_accuracy = round(test_accuracy,2)
		all_test_accuracy.append(test_accuracy)
		print("Testing Accuracy: "+str(test_accuracy))
		print("")


		temp = numpy.full(len(all_test_accuracy),0)
		for i in range(len(all_test_accuracy)):
			temp[i] = i
		p1 = plt.plot(temp, all_training_accuracy, color='red')
		p2 = plt.plot(temp, all_test_accuracy, color='green')
		plt.title('train/test accuracy for dropping different combinations of features')
		plt.legend((p1[0], p2[0]), ('train accuracy', 'test accuracy')) 
		plt.savefig('combinations/combinations_at_iter_'+str(len(temp))+'.png') 
		plt.close()

	print("If we want to have maximum training accuracy, we need to drop: " + str(combinations_of_features[numpy.argmax(all_training_accuracy)]) + " with accuracy " + str(numpy.max(all_training_accuracy)))
	print("If we want to have maximum test accuracy, we need to drop: " + str(combinations_of_features[numpy.argmax(all_test_accuracy)]) + " with accuracy " + str(numpy.max(all_test_accuracy)))





