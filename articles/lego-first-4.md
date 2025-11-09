---
title: "FIRST LEGO LEAGUE Robotic competition - week 4"
description: "Semaine 4 : découverte du bras et du capteur de distance"
date: 2025-11-08
---

Aujourd’hui, la séance consistait à équiper notre robot d’un bras et d’un capteur de distance.
Nous avons ensuite disposé des briques sur le sol, puis programmé le robot pour qu’il en récupère une, recule, et recommence jusqu’à ramasser toutes les briques.

Pour cela, il fallait utiliser le capteur de distance afin que le robot s’arrête au bon moment, abaisse son bras pour attraper la brique, recule en l'emportant, puis répète l’opération. Cela paraît simple... mais comme souvent le faire effectuer à une machine s'avère plus difficile que prévu.

Pour utiliser un capteur nous avons découvert que lorsque le bras était levé, il interférait parfois avec les distances mesurées ! Nous avons donc décidé de garder le bras baissé tant que le robot avait besoin du capteur pour avancer.

Cela nous a obligés à approcher le robot des briques à l’aide du capteur, puis à relever le bras, avancer de quelques centimètres, et enfin baisser le bras pour “attraper” la brique avant de reculer.

Autre difficulté : le capteur n’est pas efficace au-delà de 25 ou 30 cm. Or, notre placement initial des briques dépassait cette distance.

Exemple d'erreur : le capteur reste trop loin pour détecter le moteur.

<style> 
  iframe { 
    display: block; 
    margin: 0 auto; 
  } 
</style> 
<iframe width="560" height="315" src="https://www.youtube.com/embed/AWErWcHap-Y?si=-cTEEa7_lsPiq035" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

Vite corrigé par les enfants :
<style> 
  iframe { 
    display: block; 
    margin: 0 auto; 
  } 
</style> 
<iframe width="560" height="315" src="https://www.youtube.com/embed/47saVtBzNpw?si=0fiHqIbzh2jqitZ8" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

![Capture d'écran d'un programme de l'application Spike utilisant le capteur de distance](/assets/img/lego-4.jpeg)