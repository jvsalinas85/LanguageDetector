'''En este proyecto utilizarás el módulo "langdetect" para ayudarnos a identificar el idioma que 
se ha ingresado. Esto puede ser realmente útil si no estás seguro de qué idioma estás 
tratando.
Puedes crear también una GUI sencilla para interactuar con el usuario. Después puedes 
recopilar el texto del campo de entrada y procesarlo con "langdetect" para determinar qué 
idioma se ingresó. Finalmente, puedes imprimir este resultado en la GUI para informar al 
usuario sobre el resultado.
Ten en cuenta que los resultados devueltos por "langdetect" son códigos abreviados de 
idioma. Por ejemplo, si ingresamos texto en inglés, veremos 'en' como el valor de retorno'''


import tkinter as tk #to build UI
from langdetect import detect #to detect language
from tkinter.messagebox import showinfo

#global variable
text =''

def get_text():
    '''Function to detect language'''
    global text
    text = text_entry.get("1.0", "end-1c") #get the field text

    #Get the language code
    language_detected = detect_language()


    
    #display the detected language
    showinfo("Language detected", f"The language detected is {language_detected}")
    

def detect_language():
    '''Function to detect the language from text variable'''
    global text
    language = detect(text)
    return language




if __name__ == "__main__":
    main_window = tk.Tk()
    
    #settint the screen dimensions
    window_width = 800
    window_height = 600

    # get the screen dimension
    screen_width = main_window.winfo_screenwidth()
    screen_height = main_window.winfo_screenheight()

    # find the center point
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)

    # set the position of the window to the center of the screen
    main_window.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
    main_window.resizable(0,0)

    #setting customization
    main_window.title("Language Detector by Jesus Valencia")
    
    #Label for instructions
    instructions_label = tk.Label(main_window, text="Welcome to the Language Detector.\n Please enter your text in the field and click Detect! to start.", font="Verdana")
    instructions_label.pack()

    #Entry
    text_entry = tk.Text(main_window, width=50, height=10)
    text_entry.pack()
    text_entry.focus() #focus on the entry

    #Button for detection
    detection_button = tk.Button(main_window, text="Detect!", command = get_text)
    detection_button.pack()

    

    #start app
    main_window.mainloop()