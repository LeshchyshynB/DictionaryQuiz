import json
from tkinter import *
import customtkinter
import random
import time


from create_widgets import Create


class App(customtkinter.CTk, Create):
	def __init__(self):
		super().__init__()
		self.geometry("1000x500")
		self.title("English Quiz")
		self.resizable(False, False)

		self.FRAME = self.create_buttons()

		with open("dictionary.json", "r", encoding="utf-8") as f:
			self.data = json.load(f)
			
		self.score = 0
		self.incorrect = 0
		self.count = len(list(self.data.items()))

		self.update(self.FRAME)

	def update(self, frame):
		self.dictionary = {}
		if len(list(self.data.items())) > 3:
			data_list = list(self.data.items())
			self._stop = 0
		else:
			data_list = list(self.data.items())
			for i in range(0, 4-len(list(self.data.items()))):
				data_list.append((i, ''))
			
			self._stop += 1
			print(self._stop)
			if self._stop >= 4:
				self.end_quiz()
				return

		for i in range(0, len(frame["buttons"])):
			key, value = data_list.pop(random.randint(0, len(data_list)-1))
			self.dictionary[key] = value
			answer = list(self.dictionary.values())[i]
			frame["buttons"][i].configure(text=answer, bg_color="transparent", command=self.radiobutton_event)

		while True:
			self.word_quiz, self.answer_quiz = random.choice(list(self.dictionary.items()))
			if type(self.word_quiz) is str:
				break
		frame["word"].configure(text=self.word_quiz)
		
		

	def radiobutton_event(self):
		button = self.FRAME["buttons"][self.radio_var.get()]

		if button._text == self.answer_quiz:
			self.score += 1
			self.FRAME["score"].configure(
				text=f"{self.score} / {self.incorrect} ({self.count}) Rate: {round((self.score*100)/(self.score+self.incorrect), 1)}%")
			self.count -= 1
			self.data.pop(self.word_quiz)
			self.update(self.FRAME)
		else:
			button.configure(bg_color="#D41A1A", command=None)
			self.incorrect += 1
			self.FRAME["score"].configure(
				text=f"{self.score} / {self.incorrect} ({self.count}) Rate: {round((self.score*100)/(self.score+self.incorrect), 1)}%")

	def end_quiz(self):
		for i in range(0, len(self.FRAME["buttons"])):
			self.FRAME["buttons"][i].configure(text="", bg_color="transparent")
		self.FRAME["word"].configure(
				text=f"Congratulations!!!\nYou passed the test with score:\nCorrect: {self.score}\nIncorrect: {self.incorrect}\nTotal tasks: {self.count}\nRate: {round((self.score*100)/(self.score+self.incorrect), 1)}%")


	def end_test(self):
		exit()

if __name__ == "__main__":
	app = App()
	app.mainloop()
