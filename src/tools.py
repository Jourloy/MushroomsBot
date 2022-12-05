import time

class Tools():
	def __init__(self) -> None:
		pass

	def timer(self, count=5):
		for x in range(count):
			print(f'Таймер: {count - x}')
			time.sleep(1)