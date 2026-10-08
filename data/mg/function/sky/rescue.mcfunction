# Remise en selle (@s) : au-dessus du dernier anneau franchi, orienté vers le suivant (généré)
execute if score @s mg.skr matches 0 run tp @s 0.5 236 27640.5 facing 0.5 226.5 27700.5
execute if score @s mg.skr matches 1 run tp @s 0.5 233 27700.5 facing 35.5 219.5 27745.5
execute if score @s mg.skr matches 2 run tp @s 35.5 225 27745.5 facing 85.5 213.5 27775.5
execute if score @s mg.skr matches 3 run tp @s 85.5 219 27775.5 facing 135.5 205.5 27815.5
execute if score @s mg.skr matches 4 run tp @s 135.5 212 27815.5 facing 150.5 198.5 27880.5
execute if score @s mg.skr matches 5 run tp @s 150.5 204 27880.5 facing 110.5 193.5 27930.5
execute if score @s mg.skr matches 6 run tp @s 110.5 199 27930.5 facing 55.5 188.5 27955.5
execute if score @s mg.skr matches 7 run tp @s 55.5 195 27955.5 facing -4.5 182.5 27975.5
execute if score @s mg.skr matches 8 run tp @s -4.5 188 27975.5 facing -69.5 176.5 27990.5
execute if score @s mg.skr matches 9 run tp @s -69.5 183 27990.5 facing -129.5 169.5 28030.5
execute if score @s mg.skr matches 10 run tp @s -129.5 175 28030.5 facing -154.5 163.5 28090.5
execute if score @s mg.skr matches 11 run tp @s -154.5 169 28090.5 facing -119.5 157.5 28140.5
execute if score @s mg.skr matches 12 run tp @s -119.5 164 28140.5 facing -59.5 151.5 28160.5
execute if score @s mg.skr matches 13 run tp @s -59.5 157 28160.5 facing 0.5 145.5 28175.5
execute if score @s mg.skr matches 14 run tp @s 0.5 152 28175.5 facing 60.5 139.5 28190.5
execute if score @s mg.skr matches 15 run tp @s 60.5 145 28190.5 facing 120.5 132.5 28220.5
execute if score @s mg.skr matches 16 run tp @s 120.5 138 28220.5 facing 150.5 126.5 28280.5
execute if score @s mg.skr matches 17 run tp @s 150.5 133 28280.5 facing 115.5 120.5 28335.5
execute if score @s mg.skr matches 18 run tp @s 115.5 127 28335.5 facing 55.5 114.5 28360.5
execute if score @s mg.skr matches 19 run tp @s 55.5 120 28360.5 facing -9.5 108.5 28350.5
execute if entity @s[tag=mg.skstun] run function mg:sky/unstun
effect give @s minecraft:slow_falling 2 0 true
scoreboard players set @s mg.skg -40
title @s subtitle [{"text":"Appuie sur Espace pour replaner !","color":"yellow"}]
title @s title [{"text":"↺","color":"aqua","bold":true}]
playsound minecraft:entity.enderman.teleport master @s ~ ~ ~ 0.7 1.3
