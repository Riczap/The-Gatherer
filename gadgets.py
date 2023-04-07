import customtkinter as ctk
import tkinter

def if_empty(value, default):
    if(value == ""):
        value = float(default)
    else:
        pass
    return value


class SwitchesFrame(ctk.CTkFrame):
    def __init__(self, *args, header_name="TestFrame", name, text1, text2, command_name1, command_name2 , **kwargs):
        super().__init__(*args, **kwargs)


        # Add a label to the new entry frame
        self.label1 = ctk.CTkLabel(self, text=name, anchor="center")
        self.label1.grid(row=0, column=0, columnspan=1, pady=(10, 0), padx=10, sticky="n")

        # Add two entries to the new entry frame
        self.switch_var1 = ctk.StringVar(value="off")
        self.switch1 = ctk.CTkSwitch(self, text=text1, variable=self.switch_var1, onvalue="on", offvalue="off", command=command_name1)
        self.switch1.grid(row=1, column=0, pady=12, padx=10)

        self.switch_var2 = ctk.StringVar(value="off")
        self.switch2 = ctk.CTkSwitch(self, text=text2, variable=self.switch_var2, onvalue="on", offvalue="off", command=command_name2)
        self.switch2.grid(row=2, column=0, pady=12, padx=10)


    def get_state1(self):
        """ returns on or off"""
        return self.switch_var1.get()

    def get_state2(self):
        """ returns on or off"""
        return self.switch_var2.get()

    def reset_values(self):
        self.switch1.deselect()
        self.switch2.deselect()



class DoubleEntryFrame(ctk.CTkFrame):
    def __init__(self, *args, header_name="TestFrame", name, text1, text2, default1, default2, **kwargs):
        super().__init__(*args, **kwargs)

        self.default1 = default1
        self.default2 = default2

        # Add a label to the new entry frame
        self.label1 = ctk.CTkLabel(self, text=name, anchor="center")
        self.label1.grid(row=0, column=0, columnspan=2, pady=(10, 0), padx=10, sticky="n")

        # Define the validation function to allow only integers
        validate_int = (self.register(self._validate_int), '%P')

        # Add two entries to the new entry frame
        self.entry1 = ctk.CTkEntry(self, width=50, placeholder_text=text1, validate="key", validatecommand=validate_int)
        self.entry1.grid(row=1, column=0, pady=12, padx=1)

        self.entry2 = ctk.CTkEntry(self, width=50, placeholder_text=text2, validate="key", validatecommand=validate_int)
        self.entry2.grid(row=1, column=1, pady=12, padx=10)

    def _validate_int(self, value):
        """Validate that the input value is an integer."""
        if not value:
            return True

        try:
            int(value)
            return True
        except ValueError:
            return False

    def get_value1(self):
        """ returns selected value as a string, returns an empty string if nothing selected """
        self.value1 = if_empty(self.entry1.get(), self.default1)
        return self.value1

    def get_value2(self):
        """ returns selected value as a string, returns an empty string if nothing selected """

        self.value2 = if_empty(self.entry2.get(), self.default2)
        return self.value2


class SingleEntryFrame(ctk.CTkFrame):
    def __init__(self, *args, header_name="TestFrame", name, text, default, **kwargs):
        super().__init__(*args, **kwargs)
        self.default = default
        # Add a label to the new entry frame
        self.label1 = ctk.CTkLabel(self, text=name, anchor="center")
        self.label1.grid(row=0, column=0, columnspan=2, pady=(10, 0), padx=10, sticky="n")

        # Define the validation function to allow only integers
        validate_int = (self.register(self._validate_int), '%P')

        # Add a single entry to the new entry frame
        self.entry = ctk.CTkEntry(self, width=50, placeholder_text=text, validate="key", validatecommand=validate_int)
        self.entry.grid(row=1, column=0, pady=12, padx=1)

    def _validate_int(self, value):
        """Validate that the input value is an integer."""
        if not value:
            return True

        try:
            float(value)
            return True
        except ValueError:
            return False

    def get_value(self):
        """ returns selected value as a string, returns an empty string if nothing selected """
        self.value = if_empty(self.entry.get(), self.default)
        return self.value


class DropdownFrame(ctk.CTkFrame):
    def __init__(self, *args, header_name="TestFrame", name, text, default, options, **kwargs):
        super().__init__(*args, **kwargs)


        # Add a label to the new entry frame
        self.label1 = ctk.CTkLabel(self, text=name, anchor="center")
        self.label1.grid(row=0, column=0, columnspan=1, pady=(10, 0), padx=10, sticky="n")

        self.combobox_var = ctk.StringVar(value=text)  # set initial value
        self.option = ""
        self.default = default

        def combobox_callback(choice):
            #print(f"{text}:", choice)
            self.option = choice


        #["800 x 600", "1024 x 768", "1280 x 720", "1280 x 1024", "1366 x 768", "1600 x 900", "1680 x 1050", "1920 x 1080"]

        self.combobox = ctk.CTkComboBox(self, values=options, command=combobox_callback, variable=self.combobox_var)
        self.combobox.grid(row=1, column=0, pady=12, padx=10)


    def get_option(self):
        if self.option == "":
            self.option = self.default
        return self.option
