# 🎳 Départ
scoreboard players set $bt mg.st 0
scoreboard objectives setdisplay sidebar mg.bsc
effect give @a[tag=mg.play] minecraft:saturation infinite 0 true
effect give @a[tag=mg.play] minecraft:resistance infinite 4 true
execute as @a[tag=mg.bwl] run function mg:bowl/name
execute as @a[tag=mg.bwl] run function mg:bowl/to_aim
tellraw @a[tag=mg.play] [{"text":"🎳 BOWLING : ","color":"light_purple","bold":true},{"text":"5 frames, chacun sur sa piste. Place-toi derrière la ligne rouge, vise du regard, et fais clic droit avec la boule quand la jauge de puissance est au bon niveau. Accroupi en lançant = effet. Strike = 10 + les 2 lancers suivants, spare = 10 + le suivant.","color":"gray"}]
execute as @a[tag=!mg.surv,tag=mg.play] at @s run playsound minecraft:music_disc.cat record @s ~ ~ ~ 0.25 1
