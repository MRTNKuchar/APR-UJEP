#Silné heslo = jedno písmeno velké, jedno malé, jeden speciální znak a musí mít aspoň alespoň 8 znaků
#Zadáme input pro uživatele na zadání hesla
passw = input("Zadej silné heslo:")

#zadáme si počáteční hodnoty pro podmínky silného hesla
hasSpace = False
hasSpec = False 
hasUpper = False
hasLower = False
hasDigit = False

isLongenough = 8 <= len(passw)

#vytvoříme cyklus který nám zjistí zda zadané heslo od uživatele splňuje podmínky silného hesla
for char in passw:
    if char.isupper():
     hasUpper = True
    elif char.islower():
        hasLower = True
    elif char.isdigit():
       hasDigit = True
    elif char.isspace():
       hasSpace = True
    else:
       hasSpec = True

#proměnná pro zjištění zda heslo obsahuje podmínky
isValid = isLongenough and hasUpper and hasLower and not hasSpace and hasDigit and hasSpec 

print("Heslo je platné" if isValid else "Heslo je neplatné")

#napsání podmínek které nebyly splněny
if not hasUpper:
   print("Heslo musí mít alespoň jedno velké písmeno")

if not hasLower:
   print("Heslo musí mít alespoň jedno malé písmeno")

if not hasDigit:
   print("Heslo musí obsahovat alespoň jedno číslo")

if not isLongenough:
   print("Heslo musí být alespoň 8 znaků dlouhé")

if hasSpace:
   print("Heslo nesmí obsahovat mezery")

if not hasSpec:
   print("Heslo musí obsahovat speciální znak")
