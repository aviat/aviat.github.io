---
title: "LEGO FIRST Robotic competition - week 3"
description: "Semaine 3 : montage et programmation d'un premier robot"
---

Cette semaine nous avons construit un premier robot simple, dont les instructions sont fournies dans l'application Spike. Nous avons réussi à le programmer pour suivre un parcours pré-déterminé :
<style> 
  iframe { 
    display: block; 
    margin: 0 auto; 
  } 
</style> 
<iframe width="560" height="315" src="https://www.youtube.com/embed/jJKjfuBVTCk?si=g-qoZON-ykOvobUf" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Le robot se compose de 2 roues, chacune sur un moteur. L'équilibre se fait non pas avec des roues supplémentaires mais avec une bille. L'utilisation d'une bille permet au robot de tourner plus librement dans tous les axes, alors que des roues opposeraient plus de frottement.

Chaque moteur est commandé par un port différent, ils peuvent dont être commandés indépendemment. Les ordres doivent donc :
 - commander à chaque moteur de tourner en même temps pour faire avancer le robot
 - commander à chaque moteur de tourner en inverse pour faire pivoter le robot sur lui-même

De plus en mesurant la taille des roues (17.5 cm) nous pouvons indiquer qu'une rotation de moteur est égale à 17.5 cm parcourus. Cela permet simplement de programmer des centimètres pour faire avancer le robot.

Pour tourner, il y a deux options. Les enfants ont trouvé par essai et erreur la valeur qui tournait le robot d'un angle droit. Les papa ont utilisé un capteur, le gyroscope, qui permet de calculer l'angle selon lequel le robot se déplace. Cette méthode demande plus d'instructions et... n'est pas beaucoup plus précise. 

![Capture d'écran du parcours du robot par les enfants](/assets/img/lego_seance_3_enfants.jpeg)


![Capture d'écran du parcours du robot par les papas](/assets/img/lego_seance_3_papas.jpeg)


