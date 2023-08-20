def game():
    print("\t\t\t VANGA VELAYADALAM")
    print("\t\t\t ================")
    print("\t\t\t SOLRATHA KELUNGA")
    print("\t\t\t=================")
    print("1 LA IRUNTHU 10 VARAILUM ETHUNA ONNA NENACHITU , KEKURATHUKU PATHILA SOLLUNGA")
    print("=============================================================================\n")
    correct = ['yes','y','YES','Y','AMA','ama','amam','AMAM']
    wrong = ['no','n','NO','N','ILA','ila','illai','ILLAI']
    i = 1
    while (i<11):
        ip = input(f"NINGA NENACHA ENN {i} AAA?   ")
        if ip in correct:
            print(f'\nNINGAL NINAITHA ENN  {i} NA GAME LA VERTI ADANCHITEN :)\n')
            break
        elif ip in wrong:
            i+=1
            continue
        elif ip not in (correct,wrong):
            print("\nOLUNGA PATHILA SOLLU DA\n")
            print("\nPODA POI FIRST KELVIYA OLUNGA PADI DA\n")
game()
