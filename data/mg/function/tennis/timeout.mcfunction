# Temps écoulé : sur chaque court en cours, le meilleur (jeux puis points) gagne ; égalité = personne
execute as @e[type=minecraft:marker,tag=mg.tncm,scores={mg.tnph=0..3}] run function mg:tennis/timeout_court
function mg:tennis/finish
