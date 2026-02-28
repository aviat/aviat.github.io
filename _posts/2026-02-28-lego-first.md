---
title: "FIRST LEGO LEAGUE Robotic competition - week 10"
description: "Semaine 10 : trois épreuves partiellement réussies"
date: 2026-02-28
category: lego
layout: lego
---

Nous avons reçu les pièces qui nous manquaient pour la mission 3 ! C'est une épreuve qui présente un chariot de train. Le robot doit lever les rails pour le faire avancer. Les enfants l'ont monté puis ont immédiatement souhaité résoudre cette épreuve !

Notre premier essai nous a fait réussir par erreur une partie de l'épreuve 1... nous avons donc continué, avant de passer à l'épreuve 2. Une difficulté a été de trouver une vitesse adaptée pour que le robot ne glisse pas et qu'il garde une position similaire entre chaque mouvement, à chaque exécution successive du programme. Et programmer le robot requiert de nombreuses exécutions du programmes ! En ajustant la vitesse nous avons donc réussi, et le robot résout 3 épreuves en une seule exécution !

Une autre difficulté est causée par le placement du bras. Parfois les engrenages patinent (si le bras force trop, par exemple si nous nous trompons de la programmation), ce qui dérègle sa position initiale. Nous avons donc ajouté un système de débraillage, et prenons soin de réinitialiser (si besoin !) le bras en position verticale avant d'exécuter le programme. 

Mais nous avons du ajuster le programme, et avons commencé à jouer avec les **variables**. Une variable `position` enregistre la position du moteur quand le bras est en position verticale (au début du programme), et ensuite tous les ajustements du bras sont faits relativement à cette variable. L'extrait du programme suit :

![Variable position](/assets/img/lego_seance_10_variable.png)

Et voilà le robot qui réussit ces trois missions !

{% include yt.html id="W72CvMTzETQ" title="Missions 1, 2, 3" %}

Et le programme intégral :

![Programme pour les missions 1, 2, 3](/assets/img/lego_seance_10_missions-1-2-3.jpg)

