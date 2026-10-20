# Pic du Nid : alpha vaincu
scoreboard players set $trda1 mg.st 0
scoreboard players set $trds1 mg.st 0
scoreboard players set $trdc1 mg.st 180
bossbar set mg:trdg1 players
execute positioned 228.5 114 24.5 as @a[tag=mg.tvw,gamemode=adventure,distance=..48] run function mg:terra/rpg/dg/pic_rw
