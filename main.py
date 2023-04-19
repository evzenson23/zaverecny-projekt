
from pojistenec import Pojistenec
import databaze


print("=======================================")
print("        EVIDENCE POJIŠTĚNÝCH           ")
print("=======================================")
go_on = "ano"

while go_on == "ano":
      print("\n"
            "1  -  Přidat nového pojištěného\n"
            "2  -  Vypsat všechny pojištěné\n"
            "3  -  Vyhledat pojištěného dle jména\n"
            "4  -  Ukončit aplikaci\n")

      action = input("Vyberte si akci, která se má provést:\n")
      result=None

      if action == "1":
            added_name = input("Zadejte jméno: ")
            added_surname = input("Zadejte příjmení: ")
            added_age = int(input("Zadejte věk: "))
            added_cell = input("Zadejte telefonní číslo: ")
            databaze.database.append(Pojistenec(added_name, added_surname, added_age, added_cell))
            print("\nVámi zadané údaje byly uloženy do databáze pojištěnců.")
      elif action == "2":
            for item in databaze.database:
                  print(item)
      elif action == "3":
            name_to_find = input("Zadejte jméno: ")
            surname_to_find = input("Zadejte příjmení: ")
            for item in databaze.database:
                  if name_to_find == item.name and surname_to_find == item.surname:
                        result = item
                        print(result)

            if result == None:
                  print("\nVámi zadaná kombinace jména a příjmení neodpovídá žádnému pojištěnci v databázi.")

      elif action == "4":
            print("\nKonec aplikace.")
            go_on = False
            exit()
      else:
            print("\nZadal jste špatnou akci, zkuste to znovu!")
      go_on = input("\nPřejete si pokračovat?\nPro pokračování napište ano a potvrďte klávesou enter. \nPro ukončení aplikace stiskněte libovolnou klávesu a potvrďte enterem.  ")
      go_on = go_on.lower()



