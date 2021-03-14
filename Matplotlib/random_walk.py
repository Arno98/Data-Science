from random import choice

class RandomWalk():
	
	def __init__(self, number_points=3000):
		self.number_points = number_points
		self.x_value = [0]
		self.y_value = [0]
		
	def get_step(self):
		direction = choice([1, -1])
		distance = choice([1, 2, 3, 4, 5])
		step = direction * distance
		return step
		
	def walk(self):
		while len(self.x_value) < self.number_points:
			x_step = self.get_step()
			y_step = self.get_step()
				
			next_step_x = self.x_value[-1] + x_step
			next_step_y = self.y_value[-1] + y_step
			
			self.x_value.append(next_step_x)
			self.y_value.append(next_step_y)
