soldeinitial=1000
nouveausolde=0
codesecret="Adji2025"

def menu():
                 
            print(":::::Bienvenue sur le programme de fidelite d'orange Money:::::::")
            print(f"1-Consulter le Solde")
            print(f"2-acheter du crédit")
            print(f"3-effectuer un transfert")
            print(f"4-Acheter un forfait")
            print(f"0-Quitter")
            print(":::::::::::::::::::::::::::::::::::::::::::::::")
        
def Consutation():
     
     print(f"Vous avez {soldeinitial} dans votre compte")
     print(f"1-Retour au menu")
     print(f"2-Pour les Details")
     print(":::::::::::::::::::::::::::::::::::::::::::::::")

def Choix_Consultation():
    
    choixConsultation=int(input())
    if choixConsultation==1:
        menu()
    elif choixConsultation==2:
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
     choixAchat= int(input())
     if choixAchat==1:
          print(f"Donnez le montant")
          Choix1_Achat()
     elif choixAchat==2:
          print(f"Saississez le numero du destinataire")
          choix2_Achat()
     elif choixAchat==3:
          menu()
     else:
          print("Inconnu")
          print(":::::::::::::::::::::::::::::::::::::::::::::::") 

def Choix1_Achat():
     global soldeinitial
     # print(f"Donnez le montant")
     montantcredit=int(input())
     print(f"Vous voulez recharger votre numero de {montantcredit} FcFa en credit telephonique.\nVeuillez saisir votre code secret pour valider")
     nouveausolde=soldeinitial-montantcredit
     soldeinitial=nouveausolde
     code=input()
     while True:
          if codesecret!=code:
               print(f"Entrez le bon Code secret")
               code=input()
          else:
               if montantcredit > soldeinitial:
                    print(f"Solde insuffisant")
               else:     
                    print(f"Vous avez recu {montantcredit}FcFa.Nouveau solde{nouveausolde}CFA")
                    print(":::::::::::::::::::::::::::::::::::::::::::::::") 
                    break

def choix2_Achat():
     global soldeinitial

     numero=input()
     while True:
           if not numero.startswith(("77","78","70","76"))or len(numero)< 9 or not numero.isnumeric():
                print(f"le numero{numero} est invalivalide.Donnez un bon numero")          
                numero=input()
                break
               #  numero=int(numero)
                
           else:
                print(f"Donnez le montant")
                montantcredit=int(input())
                print(f"Vous voulez achete {montantcredit}Fcfa de credit pour le{numero}  .\nVeuillez saisir votre code secret pour valider")
                nouveausolde=soldeinitial-montantcredit
                soldeinitial=nouveausolde
                code=input()
                while True:
                    if codesecret!=code:
                         print(f"Entrez le bon Code secret")
                         code=input()
                         break
                    else:
                         if montantcredit > soldeinitial:
                              print(f"Solde insuffisant")
                              break
                         else:     
                              print(f"Vous avez recu {montantcredit}FcFa.Nouveau solde{nouveausolde}CFA")
                              print(":::::::::::::::::::::::::::::::::::::::::::::::")          
                              break
                break

def Transfert():
     print(f"1-Pour un numero national")
     print(f"2-Pour un numero international")
     print(f"3-Retour au menu")
     print(":::::::::::::::::::::::::::::::::::::::::::::::")

def Choix_Transfert():
    choixTransfert=int(input())
    if choixTransfert==1:
          
          print(f"Donnez le numero +221-")
          Choix1_Transfert() 
    elif choixTransfert==2:
         print(f"Donnez l'indicatif du pays et le numero()")      
    elif choixTransfert==3:
         menu() 
    else:
         print("Inconnu")
         print(":::::::::::::::::::::::::::::::::::::::::::::::")
              
def Choix1_Transfert():
     global soldeinitial

     numero=int(input("+221"))
     
     print(f"Veuillez entrez le montant que vous souhaitez transferer")
     montanttransfert=int(input())
     nouveausolde=soldeinitial-montanttransfert
     soldeinitial=nouveausolde
     print(f"Entrez votre code secret")
     code=input()
     while True:
          if codesecret!=code:
               print(f"Donnez le bon code")
               code=input()
          else:
               if montanttransfert > soldeinitial:
                    print("Votre solde est insuffisant") 
                    break
               else:
                    print(f"Votre transfert au numero {numero} a reussi. Nouveau Solde{nouveausolde}")
                    print(":::::::::::::::::::::::::::::::::::::::::::::::") 
                    Choix_transfert_choix_annuler_ou_quitter()
                    
                    # while True:
                    choix=int(input())
                    if choix==1:
                         nouveausolde= soldeinitial + montanttransfert
                         soldeinitial=nouveausolde
                         print(f"Transfert annule. Nouveau solde{nouveausolde}")
                    #    menu()
                         break
                    #    break 
                    elif choix==2:
                         menu()  
                    #    break  
                    else:
                         print("choix invalide")
                         menu()      
                         break
                    # break
def Choix_transfert_choix_annuler_ou_quitter():
     print("1-Annuler le transfert")
     print("2-Retour a l'accueil")






def Achat_forfait():
     print(f"Bienvenue! Achetez votre forfait internet a partir de 500FCFA ")
     print("Vous voulez:")
     print(f"1-pass jour")
     print(f"2-pass semaine")
     print(f"3-pass mois")
     print(":::::::::::::::::::::::::::::::::::::::::::::::")

def Choix_forfait():
     Choix_forfait=int(input())
     if Choix_forfait==1:
          print(f"Choississez votre pass jour")
          print(f"1-Pass 100Mo a 500F valable 24h")
          print(f"2-Pass 500Mo a 1000F valable 24h")
          print(f"3-Pass 1Go a 2000F valable 24h")
          print(":::::::::::::::::::::::::::::::::::::::::::::::")
          Choix_forfait_jour1()
     elif Choix_forfait==2:
          print(f"Pass 100Mo a 500F valable une semaine")
          print(f"Pass 500Mo a 1000F valable une semaine")
          print(f"Pass 1Go a 2000F valable une semaine")
          print(":::::::::::::::::::::::::::::::::::::::::::::::")
     elif Choix_forfait==3:
          print(f"Pass 100Mo a 500F valable un mois")
          print(f"Pass 500Mo a 1000F valable un mois")
          print(f"Pass 1Go a 2000F valable un mois")
          print(":::::::::::::::::::::::::::::::::::::::::::::::")      
          
def Choix_forfait_jour1():
      Choix_forfait_jour1=int(input())
      if Choix_forfait_jour1==1:
           
           print(f"1-Je confirme mon achat d'un pass internet de 100Mo a 500F valable 24h")
           print(f"2-J'annule")
           Choix_forfait_jour1_confirm()
           print("::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::") 

def Choix_forfait_jour1_confirm():
     global soldeinitial
     montantforfait=500
     
     Choix_forfait_jour1_confirm=int(input())
     if Choix_forfait_jour1_confirm==1:
        #   montantforfait=500
          print(f"Entrer votre code pour confirmer")
          code=input()
     while True:
          if codesecret!=code:
               print(f"Entrez le bon Code secret")
               code=input()
          
          elif soldeinitial>=montantforfait: 
                nouveausolde=soldeinitial-montantforfait
                soldeinitial=nouveausolde    
                print(f"Vous avez recu {montantforfait}FcFa.Nouveau solde{nouveausolde}CFA")
                print(":::::::::::::::::::::::::::::::::::::::::::::::") 
                break
       
          else:
               print(f"Solde insuffisant")
               break
     
     








          
          

               
     
     


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
                     Achat_forfait()
                     Choix_forfait()
                     continue     
                elif choix==0:
                    print("A la prochaine")
                    break   
                else:
                     print(f"Choix invalide.Choississez entre 1 et 4")     
            else:
                 print("Choix invalide")
                 print("essayer a nouveau")
                 choix_menu=input() 
                 print(":::::::::::::::::::::::::::::::::::::::::::::::")


              
principal()                

