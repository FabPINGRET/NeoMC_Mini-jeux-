# Tube de lave : alpha vaincu
scoreboard players set $trda3 mg.st 0
scoreboard players set $trds3 mg.st 0
scoreboard players set $trdc3 mg.st 180
bossbar set mg:trdg3 players
execute positioned -23.5 90 186.5 as @a[tag=mg.tvw,gamemode=adventure,distance=..48] run function mg:terra/rpg/dg/tube_rw
