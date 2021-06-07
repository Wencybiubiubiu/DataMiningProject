import numpy as np
import pandas
import sys
import random
import os
from matplotlib import pyplot as plt
from sklearn.neighbors import KNeighborsClassifier 
from sklearn.model_selection import train_test_split 

trainingDataFilenameInitial = 'preprocessed_data/all_' #'preprocessed_data.csv' #str(sys.argv[1])
#K = int(sys.argv[2])
bin_range = [0,2,5,10,20]
distance_metric = ['euclidean','manhattan','chebyshev','minkowski']


if __name__ == '__main__':
	np.random.seed(0)
	#firstly, read the data file
	result_folder = 'image/'
	neighbors = [1,2,3,5,10,20,30,50,100]

	

	test_accuracy = [0.5808731155778895,0.5539677554438861,0.5549099664991625,0.5808731155778895]
	train_accuracy = [0.629796367062765,0.6033999895304403,0.6266816730356488,0.629796367062765]
	temp = [1,2,3,4]
	i = 0


	plt.plot(temp, test_accuracy, label = 'Testing dataset Accuracy') 
	plt.plot(temp, train_accuracy, label = 'Training dataset Accuracy') 
	  
	plt.legend() 
	plt.xlabel('distance metric') 
	plt.ylabel('Accuracy')
	title = result_folder + 'accuracy_for_diff_metric.png'
	plt.savefig(title) 
	plt.close()

	exit()
	for cur_metric in distance_metric:
		temp.append(i)

		file_name = trainingDataFilenameInitial + str(bin_range[0]) + '.csv'
		df = pandas.read_csv (file_name, sep=',')#.sample(frac=0.01, random_state=47)

		label_column = df['TripType']

		features = df.drop('TripType',1)

		X_train, X_test, y_train, y_test = train_test_split( 
				 features, label_column, test_size = 0.2, random_state=42) 
		  
		#neighbors = np.arange(1, 9) 
		  
		# Loop over K values 
		k = 8

		print("neighbors:", k)

		knn = KNeighborsClassifier(n_neighbors=k,metric=cur_metric) 
		knn.fit(X_train, y_train) 
		  
		# Compute traning and test data accuracy 
		train_accuracy.append(knn.score(X_train, y_train) )
		test_accuracy.append(knn.score(X_test, y_test) )
		print("distance_metric",cur_metric)
		print("train_accuracy",train_accuracy[i])
		print("test_accuracy",test_accuracy[i])
		i += 1

	# Generate plot 
	plt.plot(temp, test_accuracy, label = 'Testing dataset Accuracy') 
	plt.plot(temp, train_accuracy, label = 'Training dataset Accuracy') 
	  
	plt.legend() 
	plt.xlabel('distance metric') 
	plt.ylabel('Accuracy')
	title = result_folder + 'accuracy_for_diff_metric.png'
	plt.savefig(title) 
	plt.close()


