import customtkinter
from tkinter import *

class Create:
	def create_buttons(self, 
					button_count: int =4, 
					button_font: int =30, 
					word_font: int =40, 
					button_pady: int = 10,
					word_pady: int =50,
					frame_pady: int =30) -> dict:
		
		self.radio_var = IntVar(self, 0)
		button_list = []
				

		frame = customtkinter.CTkFrame(master=self, width=400, height=300, fg_color="transparent")

		score = customtkinter.CTkLabel(master=self, font=(None, 20), text="0/0")
		label = customtkinter.CTkLabel(master=frame, font=(None, word_font), text="")
		
		for i in range(0, button_count):
			button_list.append(customtkinter.CTkRadioButton(master=frame, 
													text="", 
													command=self.radiobutton_event, 
													variable=self.radio_var, value=i,
													radiobutton_height=0,
													radiobutton_width=0,
													font=(None, button_font)))

		for i in range(len(button_list)):
			button_list[i].grid(row=i+1, column=0, pady=button_pady)
		label.grid(row=0, column=0, pady=word_pady)
		score.pack(anchor=NW, padx=10, pady=5)
		frame.pack(anchor=CENTER, pady=frame_pady, side=TOP)
		
		exit_btn = customtkinter.CTkButton(master=self, fg_color="#E30000", corner_radius=0,
									 text="Завершити тестування", font=(None, button_font), 
									 hover_color="#A60000", width=self._current_width,
									 command=self.end_test)
		exit_btn.pack(anchor=S, side=BOTTOM)

		return {
			"buttons": button_list,
			"frame": frame,
			"word": label,
			"score": score,
			"exit_btn": exit_btn
		  }