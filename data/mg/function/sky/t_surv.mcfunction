# Mode 3 : plateforme, zone, joueurs, colonnes de vent, fusées, fin
execute if score $skt mg.st matches 140 run title @a[tag=mg.play] actionbar [{"text":"⚠ La plateforme s'effondre dans 3 s !","color":"red","bold":true}]
execute if score $skt mg.st matches 200 run function mg:sky/pad3_off
# Rayon de la zone (dixièmes de bloc) : 700 → 150 en 3 minutes
execute if score $skt mg.st matches ..3600 run function mg:sky/s_zone
scoreboard players operation $skp5 mg.st = $skt mg.st
scoreboard players operation $skp5 mg.st %= #5 mg.st
scoreboard players operation $skfw mg.st = $skt mg.st
scoreboard players operation $skfw mg.st %= #160 mg.st
scoreboard players set $skfs mg.st 160
scoreboard players operation $skfs mg.st -= $skfw mg.st
scoreboard players operation $skfs mg.st /= #20 mg.st
scoreboard players operation $skzr mg.st = $skz mg.st
scoreboard players operation $skzr mg.st /= #10 mg.st
execute store result score $skn mg.st if entity @a[tag=mg.play]
# Colonnes de vent (actives pendant les 3 premières minutes)
scoreboard players remove @a[scores={mg.skl=1..}] mg.skl 1
execute as @a[scores={mg.skl=100}] run function mg:sky/lift_end
execute if score $skt mg.st matches ..3599 run function mg:sky/s_cols
execute as @a[tag=mg.play] at @s run function mg:sky/s_player
execute if score $skp5 mg.st matches 0 as @a[tag=mg.play] at @s positioned 0.5 ~ 29000.5 run function mg:sky/zone_chk with storage mg:sky z
execute if score $skp5 mg.st matches 0 as @a[tag=mg.play] at @s positioned 0.5 ~ 29000.5 run function mg:sky/zone_draw with storage mg:sky z
execute if score $skp5 mg.st matches 0 as @a[tag=mg.out] at @s positioned 0.5 ~ 29000.5 run function mg:sky/zone_draw with storage mg:sky z
# Une fusée toutes les 8 s (jusqu'à la mort subite)
execute if score $skt mg.st matches ..3599 if score $skfw mg.st matches 0 run function mg:sky/s_rocket
execute if score $skt mg.st matches 3600 run tellraw @a[tag=!mg.surv] [{"text":"🌪 MORT SUBITE : ","color":"red","bold":true},{"text":"zone au minimum, plus de fusées ni de colonnes de vent !","color":"gray","bold":false}]
execute if score $skt mg.st matches 3600 as @a[tag=!mg.surv] at @s run playsound minecraft:entity.wither.spawn master @s ~ ~ ~ 0.5 1.5
# Survivants : une seconde de plus
scoreboard players operation $skq mg.st = $skt mg.st
scoreboard players operation $skq mg.st %= #20 mg.st
execute if score $skq mg.st matches 0 run scoreboard players add @a[tag=mg.play] mg.sks 1
# Fin
execute store result score $skn mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $n0 mg.st matches 2.. if score $skn mg.st matches 1 as @a[tag=mg.play,limit=1] run function mg:sky/s_win
execute if score $state mg.st matches 2 if score $skt mg.st matches 6000.. run function mg:sky/s_timeout
execute if score $state mg.st matches 2 unless entity @a[tag=mg.play] run function mg:core/draw
