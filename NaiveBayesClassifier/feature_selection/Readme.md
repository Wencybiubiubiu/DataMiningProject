Running command: python3 feature_selection.py

#################
Features dropped: ('VisitNumber',)
{'TripType': 0, 'Weekday': 1, 'Upc': 2, 'ScanCount': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.4348859223769874
Testing Accuracy: 0.33160741885625966

Features dropped: ('Weekday',)
{'TripType': 0, 'VisitNumber': 1, 'Upc': 2, 'ScanCount': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.59869018410834
Testing Accuracy: 0.4203245749613601

Features dropped: ('Upc',)
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'ScanCount': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5479203291926665
Testing Accuracy: 0.43044822256568777

Features dropped: ('ScanCount',)
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5952707532407318
Testing Accuracy: 0.4126738794435858

Features dropped: ('DepartmentDescription',)
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('FinelineNumber',)
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'Weekday')
{'TripType': 0, 'VisitNumber': 1, 'Upc': 2, 'ScanCount': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.59869018410834
Testing Accuracy: 0.4203245749613601

Features dropped: ('VisitNumber', 'Upc')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'ScanCount': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5479203291926665
Testing Accuracy: 0.43044822256568777

Features dropped: ('VisitNumber', 'ScanCount')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5952707532407318
Testing Accuracy: 0.4126738794435858

Features dropped: ('VisitNumber', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('VisitNumber', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('Weekday', 'Upc')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'ScanCount': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5479203291926665
Testing Accuracy: 0.43044822256568777

Features dropped: ('Weekday', 'ScanCount')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5952707532407318
Testing Accuracy: 0.4126738794435858

Features dropped: ('Weekday', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('Weekday', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('Upc', 'ScanCount')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5952707532407318
Testing Accuracy: 0.4126738794435858

Features dropped: ('Upc', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('Upc', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('ScanCount', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('ScanCount', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'Weekday', 'Upc')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'ScanCount': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5479203291926665
Testing Accuracy: 0.43044822256568777

Features dropped: ('VisitNumber', 'Weekday', 'ScanCount')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5952707532407318
Testing Accuracy: 0.4126738794435858

Features dropped: ('VisitNumber', 'Weekday', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('VisitNumber', 'Weekday', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'Upc', 'ScanCount')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5952707532407318
Testing Accuracy: 0.4126738794435858

Features dropped: ('VisitNumber', 'Upc', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('VisitNumber', 'Upc', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'ScanCount', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('VisitNumber', 'ScanCount', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('Weekday', 'Upc', 'ScanCount')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5952707532407318
Testing Accuracy: 0.4126738794435858

Features dropped: ('Weekday', 'Upc', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('Weekday', 'Upc', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('Weekday', 'ScanCount', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('Weekday', 'ScanCount', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('Weekday', 'DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('Upc', 'ScanCount', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('Upc', 'ScanCount', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('Upc', 'DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('ScanCount', 'DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'Weekday', 'Upc', 'ScanCount')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'DepartmentDescription': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5952707532407318
Testing Accuracy: 0.4126738794435858

Features dropped: ('VisitNumber', 'Weekday', 'Upc', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('VisitNumber', 'Weekday', 'Upc', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'Weekday', 'ScanCount', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('VisitNumber', 'Weekday', 'ScanCount', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'Weekday', 'DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'Upc', 'ScanCount', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('VisitNumber', 'Upc', 'ScanCount', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'Upc', 'DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'ScanCount', 'DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('Weekday', 'Upc', 'ScanCount', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('Weekday', 'Upc', 'ScanCount', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('Weekday', 'Upc', 'DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('Weekday', 'ScanCount', 'DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('Upc', 'ScanCount', 'DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'Weekday', 'Upc', 'ScanCount', 'DepartmentDescription')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'FinelineNumber': 5}
Training Accuracy: 0.5731313872843536
Testing Accuracy: 0.3670015455950541

Features dropped: ('VisitNumber', 'Weekday', 'Upc', 'ScanCount', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'Weekday', 'Upc', 'DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'Weekday', 'ScanCount', 'DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('VisitNumber', 'Upc', 'ScanCount', 'DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

Features dropped: ('Weekday', 'Upc', 'ScanCount', 'DepartmentDescription', 'FinelineNumber')
{'TripType': 0, 'VisitNumber': 1, 'Weekday': 2, 'Upc': 3, 'ScanCount': 4, 'DepartmentDescription': 5}
Training Accuracy: 0.6294650619168132
Testing Accuracy: 0.439258114374034

If we want to have maximum training accuracy, we need to drop: ('FinelineNumber',) with accuracy 0.6294650619168132
If we want to have maximum test accuracy, we need to drop: ('FinelineNumber',) with accuracy 0.439258114374034