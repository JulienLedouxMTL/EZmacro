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

is_updating = False

def calcul(event=None):
    global is_updating
    ''' Fonction pour effectuer le calcul de conversion de masse '''
    if is_updating:
        return
    is_updating = True
    mesurei = mesure_initiale.get()

    if mesurei == "":
        mesurei = "0"

    # Vérification de la validité de l'entrée (accepte les chiffres, decimales anglais et francais)
    if not re.match(r'^-?\d*[,.]?\d*$', mesurei) or mesurei in ["-", ".", ","]:
        messagebox.showerror("Erreur", "Veuillez entrer une valeur numérique valide.")
        mesure_initiale.delete(0, tk.END)
        is_updating = False
        return
    
    mesurei = mesurei.replace(",", ".")
    mesurei = float(mesurei)

    unite = variable_menu.get()
    if unite == "Milligramme (mg)":
        mesurei = mesurei / 1000
    elif unite == "Kilogramme (kg)":
        mesurei = mesurei * 1000
    elif unite == "Once (oz)":
        mesurei = mesurei * 28.3495
    elif unite == "Livre (lb)":
        mesurei = mesurei * 453.592

    resultat.delete(0, tk.END)
    resultat.insert(0, f"{mesurei:.2f}")
    is_updating = False

def calcul_inverse(event=None):
    global is_updating
    ''' Fonction pour effectuer le calcul de conversion de masse '''
    if is_updating:
        return
    is_updating = True
    result = resultat.get()

    if result == "":
        result = "0"

    if not re.match(r'^-?\d*[,.]?\d*$', result) or result in ["-", ".", ","]:
        messagebox.showerror("Erreur", "Veuillez entrer une valeur numérique valide.")
        resultat.delete(0, tk.END)
        is_updating = False
        return
    
    result = result.replace(",", ".")
    result = float(result)

    unite = variable_menu.get()
    if unite == "Milligramme (mg)":
        result = result * 1000
    elif unite == "Kilogramme (kg)":
        result = result / 1000
    elif unite == "Once (oz)":
        result = result / 28.3495
    elif unite == "Livre (lb)":
        result = result / 453.592

    mesure_initiale.delete(0, tk.END)
    mesure_initiale.insert(0, f"{result:.2f}")
    is_updating = False


# Champs pour mesure initiale
mesure_initiale = tk.Entry(frame, width=10, bg="#D9D9D9")
mesure_initiale.pack()

# Variable liée au menu déroulant
variable_menu = tk.StringVar(frame)
variable_menu.set("Milligramme (mg)")  # valeur par défaut

# Menu déroulant de sélection de l'unité de mesure
options = ["Milligramme (mg)", "Kilogramme (kg)", "Once (oz)", "Livre (lb)"]
Unite_initiale = tk.OptionMenu(frame, variable_menu, *options)
Unite_initiale.pack(padx=20, pady=20)

# Résultat
resultat = tk.Entry(frame, width=10, bg="#D9D9D9")
resultat.pack(pady=(0, 5))

resultat_label = tk.Label(frame, text="Résultat (g)")
resultat_label.pack(pady=(0, 40))

# Bouton de calcul (bind)
mesure_initiale.bind("<KeyRelease>", calcul)
resultat.bind("<KeyRelease>", calcul_inverse)
Unite_initiale.bind("<ButtonRelease-1>", calcul)


#TIPS
def tips():
    messagebox.showinfo("Volumes en masse",
                        "Pour ce qui est des volumes, malheureusement, il est impossible de convertir les ml en g de façon consistante, car chaque ingrédient a une"
                        "masse volumique différente. Voici donc une liste d’ingrédients avec leur conversion de 1 c. à soupe en grammes:\n"
                        "\n"
                        " ▪ 1 c. à soupe de beurre = 14 g\n"
                        " ▪ 1 c. à soupe de sucre = 12 g\n"
                        " ▪ 1 c. à soupe de farine = 8 g\n"
                        " ▪ 1 c. à soupe de lait = 15 g\n"
                        " ▪ 1 c. à soupe d’eau = 15 g\n"
                        " ▪ 1 c. à soupe de miel = 21 g\n"
                        " ▪ 1 c. à soupe de crème = 15 g\n"
                        " ▪ 1 c. à soupe de vinaigre = 15 g\n"
                        " ▪ 1 c. à soupe de sauce soja = 15 g\n"
                        " ▪ 1 c. à soupe d’huile = 14 g\n"
                        " ▪ 1 c. à soupe de moutarde = 15 g\n"
                        " ▪ 1 c. à soupe de ketchup = 15 g\n"
                        " ▪ 1 c. à soupe de mayonnaise = 15 g\n"
                        " ▪ 1 c. à soupe de sauce barbecue = 15 g\n"
                        " ▪ 1 c. à soupe de beurre d'arachide = 16 g\n")

tips = tk.Button(frame, text="Tips", command=tips)
tips.pack(padx=20, pady=(0, 10))


# Dark mode/Light mode
def set_theme(bg_color, fg_color, entry_bg):
    calc.config(bg=bg_color)
    frame.config(bg=bg_color)
    mesure_initiale.config(bg=entry_bg, fg=fg_color)
    Unite_initiale.config(bg=bg_color, fg=fg_color)
    resultat_label.config(bg=bg_color, fg=fg_color)
    dark.config(bg=bg_color, fg=fg_color)
    light.config(bg=bg_color, fg=fg_color)
    resultat.config(bg=entry_bg, fg=fg_color)
    tips.config(bg=bg_color, fg=fg_color)

def dark_mode():
    set_theme("#505050", "white", "#505050")

def light_mode():
    set_theme("white", "black", "#D9D9D9")

dark = tk.Button(frame, text="Dark Mode", command=dark_mode)
dark.pack(padx=20, pady=(0, 10))

light = tk.Button(frame, text="Light Mode", command=light_mode)
light.pack(padx=20, pady=(0, 10))



# Lancement de la fenêtre
calc.mainloop()