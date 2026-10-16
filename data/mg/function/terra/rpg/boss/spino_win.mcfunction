# La reine du marais est vaincue
scoreboard players set $trspa mg.st 0
scoreboard players set $trspc mg.st 120
bossbar set mg:trspino players
execute positioned 10 65 -196 as @a[tag=mg.tvw,distance=..64] run function mg:terra/rpg/boss/spino_reward
execute positioned 10 65 -196 run title @a[tag=mg.tvw,distance=..64] title {"text":"VICTOIRE","color":"gold","bold":true}
execute positioned 10 65 -196 run title @a[tag=mg.tvw,distance=..64] subtitle {"text":"La reine du marais est tombée","color":"gray"}
