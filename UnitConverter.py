#This program converts:
#Kilometers to Miles
#Inches to Centimeters
#Pounds to Kilograms
#Each section uses a separate input field and button.
#The result is shown in a label right next to the input.
#This Program is based on our Kilometer Converter

import tkinter

class UnitConverterGUI:
    def __init__(self):
        #Create the main window
        self.main_window = tkinter.Tk()
        self.main_window.title("Unit Converter")

        #Create frames to organize widgets for each section
        self.mile_frame = tkinter.Frame()
        self.inch_frame = tkinter.Frame()
        self.pound_frame = tkinter.Frame()
        self.quit_frame = tkinter.Frame()

        #Miles to Kilometers
        self.mile_label = tkinter.Label(self.mile_frame,
                                        text='Enter a distance in miles:')
        self.mile_entry = tkinter.Entry(self.mile_frame, width=10)

        #StringVar to hold the result
        self.mile_result_var = tkinter.StringVar()
        self.mile_result_label = tkinter.Label(self.mile_frame,
                                               textvariable=self.mile_result_var)

        #Button to trigger conversion
        self.mile_button = tkinter.Button(self.mile_frame,
                                          text='Convert to Km',
                                          command=self.convert_miles)

        #Pack Miles widgets into frame
        self.mile_label.pack(side='left')
        self.mile_entry.pack(side='left')
        self.mile_button.pack(side='left', padx=2)
        self.mile_result_label.pack(side='left')
        self.mile_frame.pack(pady=5)

        #Inches (height) to Centimeters
        self.inch_label = tkinter.Label(self.inch_frame,
                                        text='Enter height (e.g. 5\'4"):')
        self.inch_entry = tkinter.Entry(self.inch_frame, width=10)

        #StringVar to hold the result (centimeters)
        self.inch_result_var = tkinter.StringVar()
        self.inch_result_label = tkinter.Label(self.inch_frame,
                                               textvariable=self.inch_result_var)

        #Button to convert height to cm
        self.inch_button = tkinter.Button(self.inch_frame,
                                          text='Convert to Cm',
                                          command=self.convert_height)

        #Pack inch widgets into frame
        self.inch_label.pack(side='left')
        self.inch_entry.pack(side='left')
        self.inch_button.pack(side='left', padx=2)
        self.inch_result_label.pack(side='left')
        self.inch_frame.pack(pady=5)

        #Pounds to Kilograms
        self.pound_label = tkinter.Label(self.pound_frame,
                                         text='Enter weight in pounds:')
        self.pound_entry = tkinter.Entry(self.pound_frame, width=10)

        #StringVar to hold the result (kilograms)
        self.pound_result_var = tkinter.StringVar()
        self.pound_result_label = tkinter.Label(self.pound_frame,
                                                textvariable=self.pound_result_var)

        #Button to convert to kilograms
        self.pound_button = tkinter.Button(self.pound_frame,
                                           text='Convert to Kg',
                                           command=self.convert_pounds)

        # Pack pound widgets into frame
        self.pound_label.pack(side='left')
        self.pound_entry.pack(side='left')
        self.pound_button.pack(side='left', padx=2)
        self.pound_result_label.pack(side='left')
        self.pound_frame.pack(pady=5)

        #Quit Button
        self.quit_button = tkinter.Button(self.quit_frame,
                                          text='Quit',
                                          command=self.main_window.destroy)
        self.quit_button.pack()
        self.quit_frame.pack(pady=15)

        #Start the tkinter GUI loop
        tkinter.mainloop()

    #Convert miles to kilometers
    def convert_miles(self):
        try:
            miles = float(self.mile_entry.get())
            km = miles * 1.60934  # 1 mile = 1.60934 km
            self.mile_result_var.set(f"{km:.2f} km")
        except ValueError:
            self.mile_result_var.set("Invalid input")

    #Convert height input like 5'4" to centimeters
    def convert_height(self):
        try:
            user_input = self.inch_entry.get().strip().replace('"', '')
            if "'" in user_input:
                feet, inches = user_input.split("'")
                total_inches = int(feet) * 12 + int(inches)
            else:
                total_inches = float(user_input)
            cm = total_inches * 2.54
            self.inch_result_var.set(f"{cm:.2f} cm")
        except:
            self.inch_result_var.set("Invalid input")

    #Convert pounds to kilograms
    def convert_pounds(self):
        try:
            pounds = float(self.pound_entry.get())
            kg = pounds * 0.453592
            self.pound_result_var.set(f"{kg:.2f} kg")
        except ValueError:
            self.pound_result_var.set("Invalid input")

#Run the program
if __name__ == '__main__':
    UnitConverterGUI()
