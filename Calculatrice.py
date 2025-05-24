import tkinter as tk
from tkinter import messagebox
import re

calc = tk.Tk()
calc.title("Calculatrice de masse")
calc.geometry("300x400") 
calc.resizable(False, False)

# Frame centrée
frame = tk.Frame(calc)
frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

def calcul():
    ''' Fonction pour effectuer le calcul de conversion de masse '''
    mesurei = Mesure_initiale.get()

    if mesurei == "":
        mesurei = "0"
    if not re.match(r'^\d+(\.\d+)?$', mesurei):
        messagebox.showerror("Erreur", "Veuillez entrer une valeur numérique valide.")
        Mesure_initiale.delete(0, tk.END)
        return
    mesurei = float(mesurei)

    unite = variable.get()
    if unite == "Milligramme (mg)":
        mesurei = mesurei / 1000
    elif unite == "Kilogramme (kg)":
        mesurei = mesurei * 1000
    elif unite == "Once (oz)":
        mesurei = mesurei * 28.3495
    elif unite == "Livre (lb)":
        mesurei = mesurei * 453.592

    resultat.config(text=f"Résultat : {mesurei:.2f} grammes (g)")


# Champs pour mesure initiale
Mesure_initiale = tk.Entry(frame, width=10)
Mesure_initiale.pack()



# Variable liée au menu déroulant
variable = tk.StringVar(frame)
variable.set("Milligramme (mg)")  # valeur par défaut

# Menu déroulant de sélection de l'unité de mesure
options = ["Milligramme (mg)", "Kilogramme (kg)", "Once (oz)", "Livre (lb)"]
Unite_initiale = tk.OptionMenu(frame, variable, *options)
Unite_initiale.pack(padx=20, pady=20)

calculer = tk.Button(frame, text="Calculer", command=calcul)
calculer.pack()

# Résultat
resultat = tk.Label(frame, text="Résultat : ", fg="#006400")
resultat.pack(pady=(0, 40))



#TIPS
def tips():
    pass

tips = tk.Button(frame, text="Tips", command=tips)
tips.pack(padx=20, pady=(0, 10))


# Dark mode/Light mode
def set_theme(bg_color, fg_color, result_fg):
    calc.config(bg=bg_color)
    frame.config(bg=bg_color)
    Mesure_initiale.config(bg=bg_color, fg=fg_color)
    Unite_initiale.config(bg=bg_color, fg=fg_color)
    calculer.config(bg=bg_color, fg=fg_color)
    dark.config(bg=bg_color, fg=fg_color)
    light.config(bg=bg_color, fg=fg_color)
    resultat.config(bg=bg_color, fg=result_fg)
    tips.config(bg=bg_color, fg=fg_color)

def dark_mode():
    set_theme("#505050", "white", "#90EE90")

def light_mode():
    set_theme("white", "black", "#006400")

dark = tk.Button(frame, text="Dark Mode", command=dark_mode)
dark.pack(padx=20, pady=(0, 10))

light = tk.Button(frame, text="Light Mode", command=light_mode)
light.pack(padx=20, pady=(0, 10))



# Lancement de la fenêtre
calc.mainloop()