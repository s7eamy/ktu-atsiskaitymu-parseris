class Assignment:
	def __init__(self, name, assign_date, due_date):
		self.name = name
		self.assign_date = assign_date
		self.due_date = due_date

	def __str__(self):
		return f"{self.name} assigned on week {self.assign_date}, due on week {self.due_date}"