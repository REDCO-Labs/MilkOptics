[TOC]

Ce document a été originalement soumis au FRQNT dans un programme de partenariat.  le projet que je propose maintenant inclus plutôt une composante sur la verification des tuyaux lors du nettoyage, mais les techniques se ressemble (et pourrait éventuellement être combinées).

Daniel Cotobre 2018



# Projet analyse du bilan de masse

## Description

Grâce à une production québécoise de plus de 3 milliards de litres de lait brut, l’industrie de la transformation du lait et du fromage génère une activité économique de plus de 3.6 milliards de dollars au Québec seulement. Cette transformation laitière est faite par les grands groupes laitiers canadiens, les PMEs et des coopératives, typiquement avec un nombre modeste d’employés (dizaine) et des chiffres d’affaires variant de 150k$ à 1.5M$, à l’aide d’une infrastructure qui permet de transformer le lait qu'on sépare en trois grands groupes: Le lait de consommation, le lait de produits fermentés, le lait de fromage. Chacun exerce une transformation par l'écrémage, la pasteurisation pour le lait de consommation. La gestion d'ingrédients, la pasteurisation,  la fermentation pour les yogourts, et finalement la maturation, le moulage, l'égouttage, l'affinage, le saumurage pour les fromages. Dans ces transformations, le lait cru est d’abord reçu par camion citerne et séparé en ses composantes (liquide, gras). Il est par la suite mélangé à nouveau dans les proportions demandées, par exemple pour du lait de consommation à taux de gras constant (0, 1, 2 et 3.25%) ou pour des fromages (à taux de gras et de protéines fixes pour chaque type de fromage). À tout moment, la quantité nécessaire (à l’intérieur des tolérances de l’industrie) doit être utilisée en évitant de gaspiller l’excès. Le contrôle serré de ces procédés, en particulier le bilan de masse (qui correspond à la connaissance de la concentration de gras et protéine dans le liquide) permet d’assurer la qualité du produit et de maximiser les revenus du transformateurs. Cependant, il est généralement difficile de suivre la quantité exacte de protéines et de matières grasses à travers les différents processus impliqués dans la fabrication du lait et du fromage. En effet, la mesure de protéines ou de taux de gras se fait généralement par la prise d’échantillons suivi d’une analyse hors-ligne. Le temps entre la prise d’échantillon et le résultat de l’analyse (qui peut par exemple indiquer un taux de gras hors de la tolérance de +- 0.1% du lait de consommation) rend impossible l’action rapide pour rectifier le processus, et rend difficile l’optimisation du processus.  Ceci se traduit soit par une variabilité de la qualité du produit ou une perte de produit, dépendamment de l’action prise.  Certains systèmes d’analyse en-ligne existent (tel le ProFoss in-line NIR Analyzer), mais sont très coûteux (au delà de 100k$ pour l’implantation de base) et donnent plus d’information qu’il n’est nécessaire. Une solution intermédiaire, à coût moindre et permettant de mesurer le bilan de masse (gras et solides) en temps réel est proposée ici pour permettre aux petites et moyennes entreprises de transformation d’avoir accès au suivi continu pour l’optimisation du bilan de masse en temps réel et ainsi augmenter la qualité de leur produit et leurs profits.

**Objectif global du projet:** Nous proposons donc de concevoir et valider la performance d’un système rapide de mesure en-ligne de la quantité de protéines et de gras pour permettre l’optimisation du bilan de masse en temps réel par les petits et moyens producteurs. Ce système s’intégrera aux systèmes de transformation du lait conçus par la compagnie Qualtech (Québec).

**Objectif spécifique 1:** Démontrer la faisabilité de mesures du taux de gras d’un fluide en mouvement par la diffusion de la lumière avec une précision de <1%

La mesure du taux de gras se base sur la diffusion de la lumière par le gras. En effet, le gras est l’élément du lait qui lui donne sa couleur blanche et opaque.  Ainsi, une mesure de la quantité de lumière rétrodiffusée par le lait permet d’obtenir le taux de gras si des modèles simples de diffusion de la lumière sont utilisés. L’illumination à l’aide d’une fibre optique multimode et la collection pour un ensemble de fibres multimodes placées sur une sonde linéaire sera utilisée pour obtenir suffisamment de lumière. Une source de lumière stable (<1% bruit RMS) permettra la caractérisation avec une précision supérieure à 1 partie dans 100 en un temps court (<1s). Grâce aux avancées dans le domaine des diodes électroluminescentes (DELs), des sources à large bandes avec une stabilité suffisante pour les besoins du projet peuvent maintenant être obtenues.  Leurs faibles coûts d’acquisition et de maintenance couplés à leur très longue durée de vie sont idéales pour les projets industriels. Le Prof. Côté utilise ces techniques depuis plus d’une décennie pour la caractérisation des tissus biologiques et transférera directement les techniques en place dans son laboratoire pour la caractérisation des propriétés du lait. En particulier, le groupe du professeur Côté a développé dans les dernières années des systèmes à base de fibre optique pour les applications cliniques qui maximisent l’efficacité de collection de la lumière par l’utilisation de micro-optique fibrée qui seront utilisés ici. La difficulté de cet objectif vient de la précision demandée (<1%) et du temps très court (1s).  La complétion de cet objectif permettra de valider la technique de quantification par rétrodiffusion pour un prototype.

**Objectif specifique 2:** Démontrer la faisabilité de mesures du taux de protéines (<1%) par spectroscopie UV à base de fibre optique d’un fluide en mouvement

Le taux de protéines sera mesuré optiquement par la fluorescence dans la gamme spectrale de l’ultraviolet (UV). En effet, l’ensemble des acides aminés composant les protéines (en particulier le tryptophane, présent dans le lait) émet une fluorescence caractéristique identifiable à l’aide d’un spectromètre dans la bande de 200 à 350 nm. Cette technique est utilisée dans les systèmes commerciaux de laboratoires pour la caractérisation des échantillons depuis plusieurs décennies, mais n’est pas testé pour les fluides en mouvement et pour une précision élevée tel que demandée ici. L’existence de spectromètres UV OEM abordables (Ocean Optics, <2500\$), et de fibres optiques UV de plus en plus performantes (par exemple, Thorlabs-UM22-100 de 180 nm à 1200 nm, 12\$/mètre) permet de concevoir un système fiable à très faible coût avec une performante suffisante pour caractériser le taux de protéine dans le lait. La difficulté de cet objectif vient de la précision demandée (1%) et du temps très court (1s). Ceci demandera un efficacité de collection importante. Encore une fois, les systèmes qui maximisent l’efficacité de collection de la lumière par l’utilisation de micro-optique fibrée seront utilisés ici.  La complétion de cet objectif permettra de valider la technique de mesure des protéines pour un prototype.

## Retombées attendues

**Des économies substantielles**: L’optimisation du bilan de masse pourra améliorer le rendement entre 0.1 et 0.5%. Avec le traitement de 10 millions de litres de lait par année dont 10% en fromage, ceci correspond à une augmentation des revenus entre 7000$ et 35000$ à 7$/kg. De plus, l’optimisation du bilan de masse en temps réel permet de faire des économies additionnelles mais plus difficilement quantifiables.

**Une qualité constante**: En maintenant une boucle de rétroaction rapide sur l’injection des protéines et du gras, une qualité plus constante sera maintenu pour les produits.

**Une innovation 100% québécoise**: Le système de contrôle qui pourrait être mis en vente par Qualtech permettra de positionner Qualtech comme un innovateur dans le domaine de la transformation laitière, en plus de la reconnaissance dont elle jouit déjà dans le marché.

**Des débouchés supplémentaires pour les ingénieurs**: Le domaine de la photonique industrielle demande à être exploité à son maximum, pour compléter l’offre en télécommunication ou en biophotonique. Les expertises développés ici pourront s’adapter à de nouvelles applications dans le domaine industriels et agro-alimentaire.  Ce personnel hautement qualifié (PHQ) pourra devenir un atout important pour les compagnies qui décident de se doter d’une branche de développement et innovation.

## Financement complémentaire fédéral

Le financement fédéral CRSNG du programme de Subventions de recherche et développement coopérative (RDC) permettra de construire un prototype grâce au partenariat avec Qualtech. Le programme RDC sera utilisé comme levier financier supplémentaire pour payer entre autres un étudiant à la maîtrise additionnel (génie industriel) ainsi que les coûts des composantes pour le prototype du système UV ou DLS. Qualtech contribuera en espèce (10 000$ ou 15 000$ ) et en nature (15 000$) soit le temps de l’ingénieur qui concevra le réceptacle en acier inoxydable et  le temps d’un machiniste et technicien-soudeur pour le construire.  Ce dispositif contiendra la sonde optique et s’intégrera aux systèmes vendus par Qualtech.

## Échéancier, sur 2 ans. 

Mois 2: 	Sélection des composantes et validation

Mois 4: 	Validation des modèles de diffusion pour le lait

Mois 8: 	Construction du système de mesure pour le taux de gras

Mois 12: 	Validation des mesures sur du lait commercial

Mois 16: 	Construction du système de mesures des protéines

Mois 20: 	Validation des mesures sur du lait commercial

Mois 22:	Construction d’un prototype d’appareil

Mois 24: 	Mesures sur place chez un client de Qualtech



## Priorités du programme

Le présent projet s’intègre parfaitement dans les [priorités](http://www.frqnt.gouv.qc.ca/partenariatsInnovation/pdf/2015/lait-vii/Guide-appel-propositions-lait-VII.pdf) du “Programme de recherche en partenariat pour l’innovation en production et en transformation laitières-VII (Volet génomique, protéomique et métabolomique)”, en particulier l’axe 3 intitulé “Maitriser et valoriser les propriétés physico-chimiques du lait et des matrices laitières”, qui lui-même cible les deux domaines suivants: 

- optimiser l’efficacité des procédés de transformation, faciliter le contrôle en continu de la qualité des produits laitiers et leur conservation;
- élaborer des indicateurs de qualité physico-chimique et technologique, adapter les technologies disponibles pour le suivi en temps réel et la modélisation au cours des processus de conditionnement et de transformation;

Ce projet sur l’analyse du bilan de masse en temps réel pour l’optimisation des procédés est tout indiqué pour ce programme.

## Innovation et Technology Readiness Level (TRL)

L’utilisation d’outils optiques innovateurs pour les mesures en protéomique est à la base même de ce projet.  Le niveau de Technology Readiness de ce projet de type “Preuve de concept” se situe au niveau 3 comme requis par le programme, où “Une recherche et développement active est initiée. Ceci inclut des études analytiques et des études en laboratoire afin de valider physiquement les prévisions analytiques des éléments séparés de la technologie”. Ainsi, les deux objectifs du présent projet permettront de valider le concept avant d’aller de l’avant avec un prototype, si les performances suffisantes sont obtenues.

## Livrable

Le présent projet répond à un besoin exprimé par les clients de Qualtech, ce qui a amené la direction de la compagnie a approcher le professeur Côté.  Il s’agit donc d’abord et avant tout d’un projet qui répond aux besoins d’une industrie grâce à une technologie optique, et non une technologie optique qui cherche une application. De plus, les capacités de manufacture de Qualtech et leur position enviable dans le marché (présent chez 80% des producteurs Québécois) assurera un transfert rapide vers le marché. 

## Contact

Le président André Giguère et le vice-président Nicolas Giguère sont directement impliqués dans le développement de ce projet et ont initié les discussions avec le professeur Côté. Tel qu’il sera démontré dans l’application complète, une contribution en espèces (10 000$ à 15 000$) et en nature montre bien l’importance stratégique de ce projet pour Qualtech.