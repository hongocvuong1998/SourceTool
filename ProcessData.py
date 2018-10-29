import os
import numpy as np
from shutil import copy, move
def CreateTrainingEvaluation(folder):
	'''
	Input folder contain image data 
	Data:
		-0
		-1
		-2
	'''
	Eva=folder+'\\Evaluation'
	Train=folder+'\\Training'
	if not os.path.exists(Eva):
		os.makedirs(Eva)
	k=0
	print('Create Evaluation')
	for root, dirs , files in os.walk(folder):
		if k==0 or ('Evaluation' in root):
			k=1
			continue
		root_=root.split('\\')
		pathdst=Eva+'\\'+str(root[-1:])
		if not os.path.exists(pathdst):
			os.makedirs(pathdst)
		# print(pathdst)

		listfiles = os.listdir(root)
		i = 0
		while  i <= len(listfiles)-5 :
			src=root +'\\' + listfiles[i]
			dst=pathdst+'\\' + listfiles[i]
			move(src, dst)
			i+=5
	print('Create Training')
	k=0
	for root, dirs , files in os.walk(folder):
		if k==0 or ('Evaluation' in root) or ('Training' in root):
			k=1
			continue
		root_=root.split('\\')
		# pathdst=Train+'\\'+str(root[-1:])
		pathdst=Train
		if not os.path.exists(pathdst):
			os.makedirs(pathdst)
		move(root, pathdst)
def CreateCSV(folder):
	'''
	Data contain Training and Evaluation
	Data:
		-Training:
			0
			1
			2
		Evaluation:
			0
			1
			2
	'''
	for root, dirs , files in os.walk(folder):
                for file in files:
                    EvaluationDataSet=open(folder+'\\Evaluation.csv','a')
                    TrainingDataSet=open(folder+'\\Training.csv', 'a')
                    
                    path=os.path.join(root, file)
                    
                    k=path.split('\\')
                    string = path +' '+str(k[-2])
                    print(string)
                    if 'Evaluation' in string:
                        EvaluationDataSet.write(string)
                        EvaluationDataSet.write('\n')
                        EvaluationDataSet.close()
                    if 'Training' in string:
                        TrainingDataSet.write(string)
                        TrainingDataSet.write('\n')
                        TrainingDataSet.close()

# CreateTrainingEvaluation(folder)
CreateCSV(folder)

