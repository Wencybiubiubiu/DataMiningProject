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
distance_metric = ['euclidean','manhattan','chebyshev','minkowski','wminkowski','seuclidean','mahalanobis']


if __name__ == '__main__':
	np.random.seed(0)
	#firstly, read the data file
	result_folder = 'image/'
	neighbors = [100]#[1,2,3,5,10,20,30,50,100]
	testing_accuracy_for_neighbors = {}
	training_accuracy_for_neighbors = {}
	for cur_neighbor in neighbors:
		testing_accuracy_for_neighbors[cur_neighbor] = []
		training_accuracy_for_neighbors[cur_neighbor] = []

	for num_of_bins in range(len(bin_range)):

		print("num_of_bins",num_of_bins)

		file_name = trainingDataFilenameInitial + str(bin_range[num_of_bins]) + '.csv'
		df = pandas.read_csv (file_name, sep=',')#.sample(frac=0.01, random_state=47)

		label_column = df['TripType']

		features = df.drop('TripType',1)

		X_train, X_test, y_train, y_test = train_test_split( 
				 features, label_column, test_size = 0.2, random_state=42) 
		  
		#neighbors = np.arange(1, 9) 
		train_accuracy = np.empty(len(neighbors)) 
		test_accuracy = np.empty(len(neighbors)) 
		  
		# Loop over K values 
		for i, k in enumerate(neighbors): 

			print("neighbors:", k)

			knn = KNeighborsClassifier(n_neighbors=k) 
			knn.fit(X_train, y_train) 
			  
			# Compute traning and test data accuracy 
			train_accuracy[i] = knn.score(X_train, y_train) 
			test_accuracy[i] = knn.score(X_test, y_test) 
			print("train_accuracy[i]",train_accuracy[i])
			print("test_accuracy[i]",test_accuracy[i])

			training_accuracy_for_neighbors[k].append(train_accuracy[i])
			testing_accuracy_for_neighbors[k].append(test_accuracy[i])
		  
		# Generate plot 
		plt.plot(neighbors, test_accuracy, label = 'Testing dataset Accuracy') 
		plt.plot(neighbors, train_accuracy, label = 'Training dataset Accuracy') 
		  
		plt.legend() 
		plt.xlabel('n_neighbors') 
		plt.ylabel('Accuracy')
		title = result_folder + 'ManyK_accuracy_for_diff_K_with_bin_' + str(bin_range[num_of_bins]) + '.png'
		plt.savefig(title) 
		plt.close()

	for key in training_accuracy_for_neighbors:
		cur_test_accu = testing_accuracy_for_neighbors[key]
		cur_train_accu = training_accuracy_for_neighbors[key]

		plt.plot(bin_range, cur_test_accu, label = 'Testing dataset Accuracy') 
		plt.plot(bin_range, cur_train_accu, label = 'Training dataset Accuracy') 
		  
		plt.legend() 
		plt.xlabel('bin_range') 
		plt.ylabel('Accuracy')
		title = result_folder + 'ManyK_accuracy_for_diff_bins_with_K_' + str(key) + '.png'
		plt.savefig(title) 
		plt.close()


