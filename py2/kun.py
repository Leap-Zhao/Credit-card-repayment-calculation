#coding=utf-8
from Tkinter import *
import random

# 简单登录案例
def divide_number_into_n_parts(number, n):
	parts_result = []
	while n != 1:
		max_number = number//2
		random_number = random.randint(0,max_number)
		parts_result.append(random_number)
		number = number - random_number
		print(random_number,max_number,number)
		n -= 1
	parts_result.append(number)
	return parts_result

def calcu_event(event):
	global entry_total_number
	global entry_count
	global label_result_message
	global label_result_check
	number = int(entry_total_number.get())
	n = int(entry_count.get())
	parts_result = []
	while n != 1:
		max_number = number//2
		random_number = random.randint(1,max_number)
		parts_result.append(random_number)
		number = number - random_number
		# print(random_number,max_number,number)
		n -= 1
	parts_result.append(number)
	label_result_message['text'] = "结果: %s" % str(parts_result)

	check_result = 0
	for item in parts_result:
		check_result += item
	label_result_check['text'] = "校验和: %d" % check_result
	# return parts_result


root = Tk()
label_total_number = Label(root, text="总数: ")
label_count = Label(root, text="总份数: ")
entry_total_number = Entry(root)
entry_count = Entry(root)
calcu_button = Button(root, text="计算")
calcu_button.bind("<Button-1>", calcu_event)
label_result_message = Label(root,text="")
label_result_check = Label(root, text="")


label_total_number.grid(row = 0, column = 0, sticky = W)
entry_total_number.grid(row=0,column=1, sticky=E)
label_count.grid(row = 1, column = 0, sticky = W)
entry_count.grid(row=1,column=1, sticky=E)
calcu_button.grid(row=2,column=0, sticky=E)
label_result_message.grid(row=3,column=1, sticky=W)
label_result_check.grid(row=4,column=1,sticky=W)

root.mainloop()
