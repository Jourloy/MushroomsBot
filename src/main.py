from screen import Screen
from tools import Tools
import pyautogui

screen = Screen()
tools = Tools()

class Main():
	def __init__(self) -> None:
		self.state = 'start'

	def stateStart(self):
		inBattle = screen.findStart()
		
		if (inBattle != None):
			tools.timer(3)

		ad = screen.findAd()

		if (ad != None):
			pyautogui.click(ad[0], ad[1]+30)
			print('Закрыл рекламу')
			tools.timer()

		if (inBattle != None):
			pyautogui.click(inBattle[0], inBattle[1]+30)
			self.state = 'waiting'
			print('Запустил матч')
		else:
			print('Кнопка запуска не найдена')
			tools.timer()

	def stateWaiting(self):
		battle = screen.findBattle()

		if (battle != None):
			self.state = 'inBattle'
			print('Бой запущен')
		else:
			print('Ожидание начала боя')

	def stateInBattle(self):
		pyautogui.press('esc')
		tools.timer(2)

		leave = screen.findLeave()

		if (leave != None):
			pyautogui.click(leave[0], leave[1]+30)
			self.state = 'leaving'
			print('Бой завершен')
		else:
			print('Кнопка выходна не найдена')

	def stateLeaving(self):
		finish = screen.findFinish()

		if (finish != None):
			pyautogui.click(finish[0], finish[1]+30)
			self.state = 'finish'
			print('Выхожу в результаты')
		else:
			print('Ожидаю выхода из боя')

	def stateFinish(self):
		lastFinish = screen.findLastFinish()

		if (lastFinish != None):
			pyautogui.click(lastFinish[0], lastFinish[1]+30)
			self.state = 'start'
			print('Выхожу в меню')
		else:
			print('Ожидаю результатов')
	
	def run(self):
		while 1:
			print(f'Состояние:{self.state}')

			if (self.state == 'start'):
				self.stateStart()
			
			if (self.state == 'waiting'):
				self.stateWaiting()

			if (self.state == 'inBattle'):
				self.stateInBattle()

			if (self.state == 'leaving'):
				self.stateLeaving()
				
			if (self.state == 'finish'):
				self.stateFinish()

main = Main()
main.run()