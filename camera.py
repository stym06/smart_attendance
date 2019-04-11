import numpy as np
import cv2
import os

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)

def take_groupie():
	cam = cv2.VideoCapture(0)
	cv2.namedWindow("test")
	img_counter=0

	while True:
		ret,frame = cam.read()
		cv2.imshow("test",frame)
		if not ret:
			break
		k = cv2.waitKey(1)

		if k%256==27:
			#ESC pressed
			print("Esc hit. Closing!")
			break
		elif k%256==32:
			#SPACE pressed
			img_name = "test-data/Group photo.jpg"
			cv2.imwrite(img_name,frame)
			img_counter += 1

	cam.release()
	cv2.destroyAllWindows()


def detect_face(img):
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

	faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors=6)

	if(len(faces)==0):
		return None

	return faces


def prepare_training_data(data_folder_path):
	dirs = os.listdir(data_folder_path)

	faces = []
	labels = []

	for dir_name in dirs:
		if not dir_name.startswith('s'):
			continue

		label = int(dir_name.replace('s',''))
		subject_dir_path = os.path.join(data_folder_path, dir_name)
	
		subject_image_names = os.listdir(subject_dir_path)
		
		for image_name in subject_image_names:
			if image_name.startswith('.'):	#ignore system files like .DS_Store
				continue

			image_path = os.path.join(subject_dir_path,image_name)
			# print(image_path)

			image = cv2.imread(image_path)

			# cv2.imshow('Training on image...', image)
			# cv2.waitKey(10)

			facess = detect_face(image)
			# print(len(facess))
			if facess is None:
				continue
			gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
			(x,y,w,h) = facess[0]
			face = gray[y:y+w, x:x+h]

			if face is not None:
				faces.append(face)
				labels.append(label)
	print("Images trained!!!!")		
	cv2.destroyAllWindows()
	cv2.waitKey(1)
	cv2.destroyAllWindows()

	return faces, labels

def predict(test_img):
	img = test_img.copy()
	faces = detect_face(img)
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	face_list=[]

	for i in range(len(faces)):
		rect = faces[i]
		(x,y,w,h) = rect
		face = gray[y:y+w, x:x+h]

		label, confidence = face_recognizer.predict(face)
		# print(label)
		face_list.append(label)

	return face_list


def make_dataset(num):
	cap = cv2.VideoCapture(0)
	samples=0
	while(True):
		ret,img = cap.read(0)
		# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
		harcascadePath = "haarcascade_frontalface_default.xml"
		detector=cv2.CascadeClassifier(harcascadePath)
		cv2.imshow('frame',img)
		
		
		faces = detector.detectMultiScale(img, 1.3, 5)
		samples = samples+1
		createFolder('training-data/s'+str(num))
		#saving the captured face in the dataset folder TrainingImage
		dest = "training-data/s"+str(num)+"/"+str(samples)+".jpg"
		cv2.imwrite(dest, img)
		#display the frame
		cv2.imshow('frame',img) 
	                

		if samples>12:
			print("Images saved")
			break

		if cv2.waitKey(1) & 0xFF == ord('q'):
			break

	cap.release()
	cv2.destroyAllWindows()

subjects = ["","Satyam","Yash","Karan"]

# faces, labels = prepare_training_data('training-data')
# face_recognizer = cv2.face.LBPHFaceRecognizer_create()
# face_recognizer.train(faces, np.array(labels))

#The below will be the classroom photograph
# test_img1 = cv2.imread("test-data/4.jpg")
# predicted_img1 = predict(test_img1)

#predicted_img1 consists of an array of labels that are present in the classroom photo
#we need to mark them present
# print(predicted_img1)

# for i in predicted_img1:
# 	print(subjects[i])

# make_dataset(7)
