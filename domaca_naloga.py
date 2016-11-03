skrito_st = 33

print("Pozdravljeni! To je igra 'Ugani skrito stevilo'. Izberi stevilo od 1 do 100")

while True:
    ugibano_st = raw_input("Vpisi svoje stevilo! ")
    ugibano_st = int(ugibano_st)
    if ugibano_st == skrito_st:
        break
    else:
        print("Zal, nisi uganil. Poskusi ponovno!")

print("Bravo, uganil si stevilo.")
   
    
