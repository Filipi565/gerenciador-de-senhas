from tkinter import *

class PEntry(Entry):
    'Tkinter Entry with a placeholder option'
    def __init__(self, master=None, placeholder='', color='grey', **kwargs):
        'Tkinter Entry with a placeholder option'
        super().__init__(master, **kwargs)

        self._placeholder = placeholder
        self._placeholder_color = color
        self._default_fg_color = self['fg']

        self.bind("<FocusIn>", self.__foc_in)
        self.bind("<FocusOut>", self.__foc_out)

        self.__put_placeholder()

    def __put_placeholder(self):
        self.insert(0, self._placeholder)
        self['fg'] = self._placeholder_color

    def __foc_in(self, *args):
        if self['fg'] == self._placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self._default_fg_color

    def __foc_out(self, *args):
        if not self.get():
            self.__put_placeholder()