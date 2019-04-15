#from main import *
def presentreg(ending, stem):
    if ending == "ar":
        form = raw_input("Form: ")
        if form == "yo":
            print(form + " " + stem + "o")
        elif form == "tu":
            print(form + " " + stem + "as")
        elif form == "el" or form == "ella" or form == "ud":
            print(form + " " + stem + "a")
        elif form == "nosotros" or form == "nosotras":
            print(form + " " + stem + "amos")
        elif form == "vosotros" or form == "vosotras":
            print(form + " " + stem + "ais")
        elif form == "ellos" or form == "ellas" or form == "uds":
            print(form + " " + stem + "an")
    elif ending == "er":
        form = raw_input("Form: ")
        if form == "yo":
            print(form + " " + stem + "o")
        elif form == "tu":
            print(form + " " + stem + "es")
        elif form == "usted" or "ud." or "ud" or "el" or "ella":
            print(form +" " + stem + "e")
        elif form == "nosotros" or "nosotras":
            print(form + " " + stem + "emos")
        elif form == "vosotros" or "vosotras":
            print(form + " " + stem + "eis")
        elif form == "ellos" or "ellas" or "uds." or "ustedes" or "ud":
            print(form + " " + stem + "en")
    elif ending == "ir":
        form = raw_input("Form: ")
        if form == "yo":
            print(form + " " + stem + "o")
        elif form == "tu":
            print(form + " " + stem + "es")
        elif form == "usted" or "ud." or "ud" or "el" or "ella":
            print(form +" " + stem + "e")
        elif form == "nosotros" or "nosotras":
            print(form + " " + stem + "imos")
        elif form == "vosotros" or "vosotras":
            print(form + " " + stem + "is")
        elif form == "ellos" or "ellas" or "uds." or "ustedes" or "ud":
            print(form + " " + stem + "en")

def presentref(refend, stem):
    if refend == "ar":
        form = raw_input("Form: ")
        if form == "yo":
            print(form + " me " + stem + "o")
        elif form == "tu":
            print(form + " te " + stem + "as")
        elif form == "el" or form == "ella" or form == "ud":
            print(form + " se " + stem + "a")
        elif form == "nosotros" or form == "nosotras":
            print(form + " nos " + stem + "amos")
        elif form == "vosotros" or form == "vosotras":
            print(form + " os " + stem + "ais")
        elif form == "ellos" or form == "ellas" or form == "uds":
            print(form + " se " + stem + "an")
    elif refend == "er":
        form = raw_input("Form: ")
        if form == "yo":
            print(form + " me " + stem + "o")
        elif form == "tu":
            print(form + " te " + stem + "es")
        elif form == "usted" or "ud." or "ud" or "el" or "ella":
            print(form + " se " + stem + "e")
        elif form == "nosotros" or "nosotras":
            print(form + " nos " + stem + "emos")
        elif form == "vosotros" or "vosotras":
            print(form + " os " + stem + "eis")
        elif form == "ellos" or "ellas" or "uds." or "ustedes" or "ud":
            print(form + " se " + stem + "en")
    elif refend == "ir":
        form = raw_input("Form: ")
        if form == "yo":
            print(form + " me " + stem + "o")
        elif form == "tu":
            print(form + " te " + stem + "es")
        elif form == "usted" or "ud." or "ud" or "el" or "ella":
            print(form + " se " + stem + "e")
        elif form == "nosotros" or "nosotras":
            print(form + " nos " + stem + "imos")
        elif form == "vosotros" or "vosotras":
            print(form + " os " + stem + "is")
        elif form == "ellos" or "ellas" or "uds." or "ustedes" or "ud":
            print(form + " se " + stem + "en")
            
def ir():
    form = raw_input("Form: ")
    if form == "yo":
        print("voy")
    elif form == "tu":
        print("vas")
    elif form == "el" or form == "ella" or form == "ud":
        print("va")
    elif form == "nosotros" or "nosotras":
        print("vamos")
    elif form == "vosotros" or "vosotras":
        print("vais")
    elif form == "ellos" or "ellas" or "uds." or "ustedes" or "ud":
        print("van")

def haber():
    form = raw_input("Form: ")
    if form == "yo":
        print("he")
    elif form == "tu":
        print("has")
    elif form == "el" or form == "ella" or form == "ud":
        print("ha")
    elif form == "nosotros" or "nosotras":
        print("hemos")
    elif form == "vosotros" or "vosotras":
        print("habeis")
    elif form == "ellos" or "ellas" or "uds." or "ustedes" or "ud":
        print("han")
        
def ser():
    form = raw_input("Form: ")
    if form == "yo":
        print("soy")
    elif form == "tu":
        print("eres")
    elif form == "el" or form == "ella" or form == "ud":
        print("es")
    elif form == "nosotros" or "nosotras":
        print("somos")
    elif form == "vosotros" or "vosotras":
        print("sois")
    elif form == "ellos" or "ellas" or "uds." or "ustedes" or "ud":
        print("son")
        
def estar():
    form = raw_input("Form: ")
    if form == "yo":
        print("estoy")
    elif form == "tu":
        print("estas")
    elif form == "el" or form == "ella" or form == "ud":
        print("esta")
    elif form == "nosotros" or "nosotras":
        print("estamos")
    elif form == "vosotros" or "vosotras":
        print("estais")
    elif form == "ellos" or "ellas" or "uds." or "ustedes" or "ud":
        print("estan")
