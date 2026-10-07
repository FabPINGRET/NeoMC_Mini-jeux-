# Place les objets en orbite / en file du pilote @s autour de son kart (mg.kk)
scoreboard players operation $kob mg.st = $ktime mg.st
scoreboard players operation $kob mg.st *= #k12 mg.st
execute as @e[type=minecraft:item_display,tag=mg.korb] if score @s mg.ri = $me mg.st run function mg:kart/orb_place
