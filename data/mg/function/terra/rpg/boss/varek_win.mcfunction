# Varek est vaincu
scoreboard players set $trva mg.st 0
scoreboard players set $trvc mg.st 120
bossbar set mg:trvarek players
execute positioned -200 65 4 as @a[tag=mg.tvw,distance=..64] run function mg:terra/rpg/boss/varek_reward
