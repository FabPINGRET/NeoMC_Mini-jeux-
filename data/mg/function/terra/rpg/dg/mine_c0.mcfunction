# Mine abandonnée : salle 1 / 3 nettoyée
scoreboard players set $trds2 mg.st 2
execute positioned -207 66 -55 as @a[tag=mg.tvw,gamemode=adventure,distance=..48] run function mg:terra/rpg/xp {n:100}
execute positioned -207 66 -55 run title @a[tag=mg.tvw,distance=..48] times 5 40 10
execute positioned -207 66 -55 run title @a[tag=mg.tvw,distance=..48] title {"text":"Salle nettoyée 1/3","color":"gold","bold":true}
execute positioned -207 66 -55 run title @a[tag=mg.tvw,distance=..48] subtitle {"text":"+100 XP","color":"yellow"}
execute positioned -207 66 -55 run playsound minecraft:entity.player.levelup player @a[tag=mg.tvw,distance=..48] ~ ~ ~ 0.8 1.2
