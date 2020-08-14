import sqlite3
import time

conn = sqlite3.connect('produse.db')
c = conn.cursor()

def creare_tabel_alimente():
    c.execute("CREATE TABLE IF NOT EXISTS alimente(nume TEXT, kcal REAL, proteine REAL, grasimi REAL, carbohidrati REAL)")

def creare_tabel_memorare():
    c.execute("CREATE TABLE IF NOT EXISTS stocate(nume TEXT, kcal REAL, proteine REAL, grasimi REAL, carbohidrati REAL)")

def introducere_date():
    denumire = input('Introduceti numele produsului: ')
    cal = input('Introduceti numarul de calorii: ')
    prot = input('Introduceti numarul de proteine: ')
    fat = input('Introduceti numarul de grasimi: ')
    carbo = input('Introduceti numarul de carbohidrati: ')
    c.execute("INSERT INTO alimente (nume, kcal, proteine, grasimi, carbohidrati) VALUES (?, ?, ?, ?, ?)", (denumire, cal, prot, fat, carbo))
    conn.commit()
    
def actualizare_calorii():
    NumeProdus = input('Introduceti numele produsului pe care vreti sa-l modificati: ')
    ModificareCalorii= input ('Introduceti valoarea: ')
    c.execute('SELECT * FROM alimente')
    c.execute('UPDATE alimente SET kcal=(?) WHERE nume=(?)', (ModificareCalorii, NumeProdus))
    conn.commit()

def actualizare_proteine():
    NumeProdus = input('Introduceti numele produsului pe care vreti sa-l modificati: ')
    ModificareProteine= input ('Introduceti valoarea: ')
    c.execute('SELECT * FROM alimente')
    c.execute('UPDATE alimente SET proteine=(?) WHERE nume=(?)', (ModificareProteine, NumeProdus))
    conn.commit()

def actualizare_grasimi():
    NumeProdus = input('Introduceti numele produsului pe care vreti sa-l modificati: ')
    ModificareGrasimi= input ('Introduceti valoarea: ')
    c.execute('SELECT * FROM alimente')
    c.execute('UPDATE alimente SET grasimi=(?) WHERE nume=(?)', (ModificareGrasimi, NumeProdus))
    conn.commit()

def actualizare_carbohidrati():
    NumeProdus = input('Introduceti numele produsului pe care vreti sa-l modificati: ')
    ModificareCarbohidrati= input ('Introduceti valoarea: ')
    c.execute('SELECT * FROM alimente')
    c.execute('UPDATE alimente SET carbohidrati=(?) WHERE nume=(?)', (ModificareCarbohidrati, NumeProdus))
    conn.commit()

def interogare_actualizare_macronutrienti():
    ActualizareMacronutrient = input('Ce valoare nutritiva doriti sa modificati? ')
    if ActualizareMacronutrient == "calorii":
        actualizare_calorii()
    elif ActualizareMacronutrient == "proteine":
        actualizare_proteine()
    elif ActualizareMacronutrient == "grasimi":
        actualizare_grasimi()
    elif ActualizareMacronutrient == "carbohidrati":
        actualizare_carbohidrati()
    else:
        print('Ati introdus un nume gresit! ')

def stergere_produs():
    sterge=input('Introduceti numele produsului pe care doriti sa-l stergeti: ')
    c.execute('SELECT * FROM alimente ')
    c.execute('DELETE  FROM alimente WHERE nume=(?)',(sterge,))
    conn.commit()

def afisare_alimente():
    c.execute('SELECT * FROM alimente')
    for row in c.fetchall():
        print(row)  
    
   
#creare_tabel_alimente()
creare_tabel_memorare()
introducere_date()
afisare_alimente()
interogare_actualizare_macronutrienti()
afisare_alimente()
stergere_produs()
afisare_alimente()





