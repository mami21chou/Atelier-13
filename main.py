def menu():
                 
            print(":::::Bienvenue sur le programme de fidelite d'orange Money:::::::")
            print(f"1-Consulter le Solde")
            print(f"2-acheter du crédit")
            print(f"3-effectuer un transfert")
            print(f"4-Quitter")
            print(":::::::::::::::::::::::::::::::::::::::::::::::")
        



def Consutation():
     print("Vous avez 1000f dans votre compte")
     print(f"1-Retour au menu")
     print(f"2-Pour les Details")
     print(":::::::::::::::::::::::::::::::::::::::::::::::")
def Choix_Consultation():
    
    menuchoixConsultation=int(input())
    if menuchoixConsultation==1:
        menu()
    elif menuchoixConsultation==2:
        print(f"Dernier recharge 500f le 28 mars 2025 a 12h20")
        menu() 
    else:
        print(f"Inconnu")      
        print(":::::::::::::::::::::::::::::::::::::::::::::::")
def Achat():
     print(f"Je souhaite acheter du credit telephonique")
     print(f"1-Pour mon numero")
     print(f"2-Pour  un autre numero")
     print(f"3-Retour au menu")
     print("::::::::::::::::::::::::::::::::::::::::::::::::::::")
def Choix_Achat():
     choixAchat= input()
     if choixAchat==1:
          print(f"Donnez le montant")
     elif choixAchat==2:
          print(f"Saississez le numero du destinataire")
     elif choixAchat==3:
          menu()
     else:
          print("Inconnu")
          print(":::::::::::::::::::::::::::::::::::::::::::::::") 
                 
def Transfert():
     print(f"Pour un numero national")
     print(f"Pour un numero international")
     print(f"Retour au menu")
     print(":::::::::::::::::::::::::::::::::::::::::::::::")

def Choix_Transfert():
    choixTransfert=input()
    if choixTransfert==1:
          print(f"Donnez le numero +221-") 
    elif choixTransfert==2:
         print(f"Donnez l'indicatif du pays et le numero()")      
    elif choixTransfert==3:
         menu() 
    else:
         print("Inconnu")
         print(":::::::::::::::::::::::::::::::::::::::::::::::")
              

               
     
     


def principal():
        entree="#144#"
        choix_menu=input()
        while True:
            if entree==choix_menu:
                menu()
                choix=int(input())

                if choix==1:
                    Consutation()
                    Choix_Consultation()
                    continue
                
                elif choix ==2:
                     Achat()
                     Choix_Achat()
                     continue   

                elif choix==3:
                     Transfert()
                     Choix_Transfert()
                     continue      
                     
                elif choix==4:
                    print("A la prochaine")
                    break        
            else:
                 print("Choix invalide")
                 print("essayer a nouveau")
                 choix_menu=input() 
                 print(":::::::::::::::::::::::::::::::::::::::::::::::")


              
principal()                

