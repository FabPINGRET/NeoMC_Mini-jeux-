# Cœur de l'Arbre-Mère : salle 3 / 3 nettoyée
scoreboard players set $trds0 mg.st 6
execute positioned 54 89 -178 as @a[tag=mg.tvw,gamemode=adventure,distance=..48] run function mg:terra/rpg/xp {n:300}
execute positioned 54 89 -178 run title @a[tag=mg.tvw,distance=..48] times 5 40 10
execute positioned 54 89 -178 run title @a[tag=mg.tvw,distance=..48] title {"text":"Salle nettoyée 3/3","color":"gold","bold":true}
execute positioned 54 89 -178 run title @a[tag=mg.tvw,distance=..48] subtitle {"text":"+300 XP : l'alpha t'attend","color":"yellow"}
execute positioned 54 89 -178 run playsound minecraft:entity.player.levelup player @a[tag=mg.tvw,distance=..48] ~ ~ ~ 0.8 1.2
