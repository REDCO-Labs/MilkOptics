# Cahier des charges

### Sous projet 1: Nettoyage des conduits

#### But

Reconnaître la composition du mélange présent à l'intérieur des conduits en temps réel afin de mieux identifier les différentes phases du nettoyage et ainsi optimiser le processus.

#### Remarques

- La caustique est réutilisé pour quelques nettoyages. Il est alors inutile de détecter le degré absolu de salubrité de la caustique, il faut plutôt s'intéresser à la différence entre l'entrée et la sortie des conduits (donc 2 capteurs) afin de voir si la caustique opère toujours.

#### Cahier des charges

$\Delta P_C$: Différence de propreté minimale de la caustique pour considérer un nettoyage actif.  

| CHARGES                                                      | CONTRAINTES         |
| :----------------------------------------------------------- | ------------------- |
| **Déterminer la composition du mélange**                     |                     |
| Précision sur la concentration en caustique (par rapport à l'eau et au lait) | < 1% ?              |
| Précision sur la différence en diffusion de deux spectres de caustique | < $\Delta P_C/2$    |
| **Acquérir les données en temps réel**                       |                     |
| Fréquence d'acquisition                                      | \> 5 Hz             |
| **Contrôler la durée du nettoyage**                          |                     |
| Calcul de l'efficacité du nettoyage                          |                     |
| Communication à la machinerie                                | NA                  |
| Temps de réponse au signal d'arrêt                           | < 5 s               |
| **Respecter les normes de sécurité/salubrité**               |                     |
| Géométrie                                                    | Coins ronds (r > X) |
| Matériaux exposés                                            | Acier inox et verre |

 

### Sous projet 2: Bilan de masse

#### But

Mesurer la quantité de protéines et de gras pour permettre l’optimisation du bilan de masse en temps réel par les producteurs laitiers.

