# Zone déchargée pendant la construction (partie annulée ?) : on reconstruira à la prochaine partie
setblock 300 55 34602 minecraft:air
tellraw @a[tag=mg.admin] {"text":"[Mini-Jeux] Golf : construction interrompue (zone déchargée).","color":"red"}
