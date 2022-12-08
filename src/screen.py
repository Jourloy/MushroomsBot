import numpy as np
import pyautogui
import imutils
import cv2
from imutils.object_detection import non_max_suppression


class Screen():
	def __init__(self) -> None:
		pass

	def getScreen(self, color=cv2.COLOR_RGB2BGR):
		'''
		Return screenshot
		'''
		image = pyautogui.screenshot(region=(0, 30, 485, 270))
		image = cv2.cvtColor(np.array(image), color)
		return image

	def findStart(self, threshold=.8):
		'''
		Find "In Battle" on a screen
		'''
		image = self.getScreen()
		template = cv2.imread('images/inBattle.png')
		result = self.findTemplate(image, template, threshold)
		return result

	def findCategory(self, threshold=.8):
		'''
		Find "Category" on a screen
		'''
		image = self.getScreen()
		template = cv2.imread('images/category.png')
		result = self.findTemplate(image, template, threshold)
		return result

	def findAd(self, threshold=.8):
		'''
		Find "AD" on a screen
		'''
		image = self.getScreen()
		template = cv2.imread('images/closeAd.png')
		result = self.findTemplate(image, template, threshold)
		return result

	def findLeave(self, threshold=.8):
		'''
		Find "Leave button" on a screen
		'''
		image = self.getScreen()
		template = cv2.imread('images/leave.png')
		result = self.findTemplate(image, template, threshold)
		return result

	def findFinish(self, threshold=.8):
		'''
		Find "Finish button" on a screen
		'''
		image = self.getScreen()
		template = cv2.imread('images/finish.png')
		result = self.findTemplate(image, template, threshold)
		return result

	def findLastFinish(self, threshold=.8):
		'''
		Find "Last finish button" on a screen
		'''
		image = self.getScreen()
		template = cv2.imread('images/lastFinish.png')
		result = self.findTemplate(image, template, threshold)
		return result

	def findBattle(self, threshold=.8):
		'''
		Find "Battle button" on a screen
		'''
		image = self.getScreen()
		template = cv2.imread('images/battle.png')
		result = self.findTemplate(image, template, threshold)
		return result

	def findTemplate(self, image, template, threshold):
		'''
		Find template on a image
		'''
		res = cv2.matchTemplate(image, template, cv2.TM_CCOEFF_NORMED)
		loc = np.where(res >= threshold)
		result = None
		for pt in zip(*loc[::-1]):
			result = pt
		return result

	def takeRatingShot(self, color=cv2.COLOR_RGB2BGR):
		image = pyautogui.screenshot(region=(250, 185, 60, 20))
		image = cv2.cvtColor(np.array(image), color)
		return image