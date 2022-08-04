import random

class Triangle:
	def __init__(self, x, y):
		self.base = x 
		self.height = y

	def set_base(self, user_base):
		self.base = user_base
	
	def set_height(self, user_h):
		self.height = user_h

	def get_area(self):
		area = 0.5 * self.base * self.height
		return area

	def print_info(self):
		print("-----------")
		print("Base : %.2f" % self.base)
		print("Height : %.2f" % self.height)
		print("Area : %.2f" % self.get_area() ) 
	
######Loop through and create 100 Triangle() objects. Append them to a List######
list_of_triangles = []
for i in range(100):
	h = random.randint(1,5)
	b = random.randint(1,5)
	list_of_triangles.append( Triangle(b,h) )

######Print info of every third Triangle on the list######
for i in range(0,99,3):
	#list_of_triangles[i].print_info()
	print(list_of_triangles[i])

#tri = Triangle(4,5)
#print(list_of_triangles[5].height)














