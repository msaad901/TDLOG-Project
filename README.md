# TDLOG-Project

Welcome everyone

Ce projet a pour objectif de concevoir un simulateur de bataille navale, pour cela nous allons implémenter des classes python pour représenter les différents vaisseaux de la marine ainsi que leurs armes.
Pour simplifier, chaque vaisseau possède un seul type d’arme et peut se déplacer selon les coordonnées x, y, z dans un espace de 3 dimensions, z = 0 étant le niveau de la mer.

L'équipe de travail est :
- Ayoub Ouaja (Product Owner)
- Mouad Khaznaoui (Scrum Master)
- Mohamed Saad L'hamdi (Développeur)
- Yasser Kamal (Développeur)
- Berkegui Hermione Rosange Lafia (Développeuse)

___
## **Énoncé du TP 1 :**

### **A- Les armes :**  

Écrire la super classe (classe mère) qui représente une arme de manière générale :

![image](https://user-images.githubusercontent.com/109675898/199854162-2db38cad-9677-4796-a2e4-c3bdf908e682.png)

A partir de cette classe implémenter les armes suivantes :

![image](https://user-images.githubusercontent.com/109675898/199854322-a593e5d6-ba99-42d4-870e-69ea2cb1ffbc.png)

Chaque arme implémente fire_at(x, y, z) en respectant les règles suivantes :

           • Contrôler la réserve de munitions, si = 0 remonter une exception (NoAmmunitionError)

           • Contrôler la validité des coordonnées de la cible x, y, z selon le type d'arme, si la règle n'est pas respectée remonter une exception (OutOfRangeError) et retirer 1 des munitions
               
    o Missile antisurface : z = 0)
    
    o Missile anti-air : z > 0
    
    o Torpille : z <= 0
    
Écrire les tests unitaires qui valident ces règles avant leurs implémentations (Tests Driven Development)


## **Énoncé du TP 2 :**

### A- Les vaisseaux :

Écrire la super classe (classe mère) qui représente un vaisseau de manière générale :

![image](https://user-images.githubusercontent.com/109675898/199855732-1112f4f1-1acb-4c8f-ade1-d0ab8e1480c0.png)

A partir de cette classe implémenter les vaisseaux suivants en spécifiant le type d’arme :

![image](https://user-images.githubusercontent.com/109675898/199855826-ac084025-9993-476f-b32d-04d96d0fd89a.png)

Implémenter la méthode go_to(x, y, z) en contrôlant la validité des coordonnées de déplacement de chaque vaisseau en écrivant les tests unitaires d’abord.

Implémenter la méthode fire_at(x, y, z) de chaque vaisseau en respectant les règles suivantes :

            • Un vaisseau avec max_hits = 0 est un vaisseau détruit et donc ne peut ni tirer ni se déplacer, il faut remonter une erreur DestroyedError

            • Si la cible est à une distance supérieure au rayon d’action de l’arme remonter une erreur (OutOfRangeError) et retirer 1 des munitions
            
### B- Le champ de la bataille :
Dans cette bataille 2 joueurs vont s’affronter, ils doivent définir chacun un espace avec la liste de leurs vaisseaux, un joueur gagne la partie s’il détruit tous les vaisseaux de son adversaire ou si son adversaire n’a plus de munitions.

Créez l’espace dans lequel évoluent vos vaisseaux, imaginez une classe qui représente un espace à 3 dimensions avec : x, y ∈ [0, 100] et z ∈ {-1, 0, 1} et qui contient une liste de vaisseaux :

Pour ajouter un vaisseau à votre espace, vérifier qu’il n’y a pas de vaisseau déjà positionné à cet endroit, et que Σ(max_hits) <= 22.

Dans cette classe, créer une méthode qui permet "recevoir" un coup aux coordonnées x, y, z à un champs de bataille, cette méthode renvoie un boolean vrai ou faux selon s’il y a un vaisseau est positionné à cet endroit.

