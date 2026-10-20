# Pic du Nid : salle 2 / 3 nettoyée
scoreboard players set $trds1 mg.st 4
execute positioned 228 91 24 as @a[tag=mg.tvw,gamemode=adventure,distance=..48] run function mg:terra/rpg/xp {n:200}
execute positioned 228 91 24 run title @a[tag=mg.tvw,distance=..48] times 5 40 10
execute positioned 228 91 24 run title @a[tag=mg.tvw,distance=..48] title {"text":"Salle nettoyée 2/3","color":"gold","bold":true}
execute positioned 228 91 24 run title @a[tag=mg.tvw,distance=..48] subtitle {"text":"+200 XP","color":"yellow"}
execute positioned 228 91 24 run playsound minecraft:entity.player.levelup player @a[tag=mg.tvw,distance=..48] ~ ~ ~ 0.8 1.2
