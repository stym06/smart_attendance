Flow:

		1) Registration of each student
			a) Student enters their registration number
			b) Student sits in front of camera, 60 photos are clicked

		2) Recognition of students from the class photograph

		3) Update of attendance of each student identified

System flow:
		
		"Prompt for Registration/Attendance"
		
		[REGISTRATION]

		* Prompt for registration number
		* Camera opens and captures 60 images of the face (assumed that a single face is present)
		* Each person's image is saved in the folder `training-data/s{number}`

		** After all the students have been registered, System is trained using the images in the folders

		[ATTENDANCE MARKING]

		* Teacher logs in
		* Select branch and subject code: EC/CS/EE and 205,306,etc
		* Take a class photograph
		* System shows the name of faces recognized in the class photo
		* Teacher clicks "Mark Attendance"
		* An excel file is created with the name as today's date and the contents as "NAME -> Present/Absent"
		* Teacher can make changes if there is an error.