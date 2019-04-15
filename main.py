
print("Welcome to Spanish Verb Conjugator")
verb = raw_input("Enter the verb: ")
length = len(verb)

r1 = length - 1
v1 = length - 2
g1 = length - 3
gg1 = length - 4

guir = str(verb[gg1]+verb[g1]+verb[v1]+verb[r1])
ger = str(verb[g1]+verb[v1]+verb[r1])

v = verb[v1]
r = verb[r1]
end = str(v+r)
stem = verb[0:v1]

tense = raw_input("Choose your tense: ")
# turn ar er ir into else irregulars into elif/if

'''
if tense == "present":
    import presentstem
    import present
    if verb == presentstem.ei:
        print("pass")
    #elif end == "ar" or end == "er" or end == "ir":
        #present.presentreg(end,stem)
    elif end == "se":
        s1 = length - 3
        e1 = length - 4
        s = verb[s1]
        e = verb[e1]
        refend = str(e + s)
        refstem = verb[0:e1]
        present.presentref(refend, refstem)
        
    elif verb == "ir":
        present.ir()
    elif verb == "ser":
        present.ser()
    elif verb == "estar":
        present.estar()
'''
'''
if verb in ei:
    if form == "yo" or form == "tu" or form == "el" or form == "ella" or form == "ud" or form == "uds" or form == "ellos" or form == "ellas":
'''     
