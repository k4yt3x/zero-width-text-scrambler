#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Name: Zero-Width Text Scrambler
Author: K4YT3X
Date Created: September 22, 2020
Last Modified: September 22, 2020

Licensed under the GNU General Public License Version 3 (GNU GPL v3),
    available at: https://www.gnu.org/licenses/gpl-3.0.txt
(C) 2020 K4YT3X
"""

from tkinter import *
import random

# zero-width characters
ZWC = {
    # '\u200B',  # zero-width space
    '\u200C',  # zero-width non-joiner
    '\u200D',  # zero-width joiner
    '\u2060',  # word joiner
    '\uFEFF',  # zero-width no-break space
}


def scramble():
    scrambled_text = ''
    for character in input_text.get()[:-1]:
        scrambled_text += character
        for _ in range(random.randint(1, max_separators.get())):
            scrambled_text += random.choice(tuple(ZWC))
    output_text.set(scrambled_text + input_text.get()[-1])
    print(str((scrambled_text + input_text.get()[-1]).encode('unicode-escape')))


if __name__ == "__main__":
    gui = Tk()
    gui.configure(background='white')
    gui.title('零宽文字混淆器')

    input_text = StringVar()
    input_text_label = StringVar()
    input_text_label.set('输入文字: ')
    input_text_label = Label(gui, textvariable=input_text_label, relief=RIDGE, width=15)
    input_text_label.grid(row=0, column=0)

    input_text_field = Entry(gui, textvariable=input_text)
    input_text_field.grid(row=0, column=1)

    output_text = StringVar()
    output_text_label = StringVar()
    output_text_label.set('输出文字: ')
    output_text_label = Label(gui, textvariable=output_text_label, relief=RIDGE, width=15)
    output_text_label.grid(row=1, column=0)

    output_text_field = Entry(gui, textvariable=output_text)
    output_text_field.grid(row=1, column=1)

    max_separators = IntVar()
    max_separators_label = StringVar()
    max_separators_label.set('最大分隔字符数量: ')
    max_separators_label = Label(gui, textvariable=max_separators_label, relief=RIDGE, width=15)
    max_separators_label.grid(row=2, column=0)

    max_separators_field = Entry(gui, textvariable=max_separators)
    max_separators.set(5)
    max_separators_field.grid(row=2, column=1)

    convert = Button(gui, text='混淆', command=scramble, height=1, width=30)
    convert.grid(row=3, column=0, columnspan=2)

    gui.mainloop()
