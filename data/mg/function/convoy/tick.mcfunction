# 🚚 Convoi — tick
scoreboard players add $cvt mg.st 1
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:convoy/respawn
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..74}] run function mg:convoy/respawn
scoreboard players set $cve mg.st 0
scoreboard players set $cvb mg.st 0
execute if score $cvm mg.st matches 1 at @e[type=minecraft:block_display,tag=mg.cvc,limit=1] store result score $cve mg.st if entity @a[tag=mg.play,gamemode=!spectator,distance=..4]
execute if score $cvm mg.st matches 1 at @e[type=minecraft:block_display,tag=mg.cvc,limit=1] store result score $cvb mg.st if entity @e[tag=mg.cvm,distance=..4]
execute if score $cvm mg.st matches 0 if score $cvo mg.st matches 0 at @e[type=minecraft:block_display,tag=mg.cvc,limit=1] store result score $cve mg.st if entity @a[tag=mg.play,team=mg_red,gamemode=!spectator,distance=..4]
execute if score $cvm mg.st matches 0 if score $cvo mg.st matches 0 at @e[type=minecraft:block_display,tag=mg.cvc,limit=1] store result score $cvb mg.st if entity @a[tag=mg.play,team=mg_blue,gamemode=!spectator,distance=..4]
execute if score $cvm mg.st matches 0 if score $cvo mg.st matches 1 at @e[type=minecraft:block_display,tag=mg.cvc,limit=1] store result score $cve mg.st if entity @a[tag=mg.play,team=mg_blue,gamemode=!spectator,distance=..4]
execute if score $cvm mg.st matches 0 if score $cvo mg.st matches 1 at @e[type=minecraft:block_display,tag=mg.cvc,limit=1] store result score $cvb mg.st if entity @a[tag=mg.play,team=mg_red,gamemode=!spectator,distance=..4]
execute if score $cve mg.st matches 1.. if score $cvb mg.st matches 0 as @e[type=minecraft:block_display,tag=mg.cvc,limit=1] at @s run tp @s ~0.06 ~ ~
execute as @e[tag=mg.cvl] at @e[type=minecraft:block_display,tag=mg.cvc,limit=1] run tp @s ~ ~2.2 ~
execute store result score $cvp mg.st run data get entity @e[type=minecraft:block_display,tag=mg.cvc,limit=1] Pos[0]
scoreboard players add $cvp mg.st 60
execute store result bossbar mg:convoy value run scoreboard players get $cvp mg.st
execute if score $cve mg.st matches 1.. if score $cvb mg.st matches 0 run bossbar set mg:convoy color green
execute if score $cvb mg.st matches 1.. run bossbar set mg:convoy color red
execute if score $cve mg.st matches 0 if score $cvb mg.st matches 0 run bossbar set mg:convoy color yellow
execute if score $cve mg.st matches 1.. if score $cvb mg.st matches 0 at @e[type=minecraft:block_display,tag=mg.cvc,limit=1] run particle minecraft:cloud ~ ~0.2 ~ 0.4 0.1 0.4 0 1
scoreboard players operation $cvq mg.st = $cvt mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $cvq mg.st %= #20 mg.st
execute if score $cvq mg.st matches 0 run function mg:convoy/second
execute if score $state mg.st matches 2 if score $cvp mg.st matches 120.. run return run function mg:convoy/arrived
execute if score $state mg.st matches 2 if score $cvm mg.st matches 0 if score $cvt mg.st matches 3600.. run return run function mg:convoy/round_end
execute if score $state mg.st matches 2 if score $cvm mg.st matches 1 if score $cvt mg.st matches 7200.. run return run function mg:convoy/coop_lose
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
