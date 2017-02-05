users = {
	'Students': [
		{"first_name": "Michael", "last_name": "Jordan"},
		{"first_name": "John", "last_name": "Rosales"},
		{"first_name": "Mark", "last_name": "Guillen"},
		{"first_name": "KB", "last_name": "Tonel"}
	],

	'Instructors': [
		{"first_name": "Michael", "last_name": "Choi"},
		{"first_name": "Martin", "last_name": "Puryear"}
	]
}

for key, data in users.items():
	count = 0
	for value in data:
		count += 1
		name_count = len(value["first_name"]) + len(value["last_name"])

		print count, value["first_name"], value["last_name"], "-", name_count
