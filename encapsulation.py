# # Python program to
# # demonstrate private methods

# # Creating a Base class
# class cmp:

# 	# Declaring public method
# 	def fun(self):
# 		print("Public method")

# 	# Declaring private method
# 	def __fun(self):
# 		print("Private method")

# # Creating a derived class
# class emp(cmp):
# 	def __init__(self):
		
# 		# Calling constructor of
# 		# Base class
# 		cmp.__init__(self)
		
# 	def call_public(self):
		
# 		# Calling public method of base class
# 		print("\nInside derived class")
# 		self.fun()
		
# 	def call_private(self):
		
# 		# Calling private method of base class
# 		self.__fun()

# # Driver code
# obj1 = cmp()

# # Calling public method
# obj1.fun()

# obj2 = emp()
# obj2.call_public()
































