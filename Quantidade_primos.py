def n_primos (x):
    cont_primo = 0
    fator = 2
    while x >= 1 and fator <= x:
        while x % fator != 0:
            fator =  fator + 1
            if fator == x:
                cont_primo = cont_primo + 1
                x =  x - 1
                fator  = 2

        x =  x - 1
        fator  = 2
    cont_primo = cont_primo + 1
    return cont_primo
