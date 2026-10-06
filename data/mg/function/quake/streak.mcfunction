# Quakecraft — série de kills (@s = tueur) : +1 puis annonce aux paliers
scoreboard players add @s mg.ks 1
execute if score @s mg.ks matches 3 run tellraw @a[tag=mg.play] [{"text":"⚡ ","color":"aqua"},{"selector":"@s","color":"white","bold":true},{"text":" : ","color":"gray"},{"text":"KILLING SPREE","color":"yellow","bold":true},{"text":"  (3 kills d'affilée)","color":"gray"}]
execute if score @s mg.ks matches 3 run title @s title [{"text":"KILLING SPREE","color":"yellow","bold":true}]
execute if score @s mg.ks matches 3 run title @s subtitle [{"text":"3 kills d'affilée","color":"gray"}]
execute if score @s mg.ks matches 3 at @s run playsound minecraft:entity.ender_dragon.growl master @a ~ ~ ~ 0.6 1.4
execute if score @s mg.ks matches 5 run tellraw @a[tag=mg.play] [{"text":"⚡ ","color":"aqua"},{"selector":"@s","color":"white","bold":true},{"text":" : ","color":"gray"},{"text":"RAMPAGE","color":"gold","bold":true},{"text":"  (5 kills d'affilée)","color":"gray"}]
execute if score @s mg.ks matches 5 run title @s title [{"text":"RAMPAGE","color":"gold","bold":true}]
execute if score @s mg.ks matches 5 run title @s subtitle [{"text":"5 kills d'affilée","color":"gray"}]
execute if score @s mg.ks matches 5 at @s run playsound minecraft:entity.ender_dragon.growl master @a ~ ~ ~ 0.6 1.2
execute if score @s mg.ks matches 7 run tellraw @a[tag=mg.play] [{"text":"⚡ ","color":"aqua"},{"selector":"@s","color":"white","bold":true},{"text":" : ","color":"gray"},{"text":"DOMINATING","color":"red","bold":true},{"text":"  (7 kills d'affilée)","color":"gray"}]
execute if score @s mg.ks matches 7 run title @s title [{"text":"DOMINATING","color":"red","bold":true}]
execute if score @s mg.ks matches 7 run title @s subtitle [{"text":"7 kills d'affilée","color":"gray"}]
execute if score @s mg.ks matches 7 at @s run playsound minecraft:entity.ender_dragon.growl master @a ~ ~ ~ 0.6 1
execute if score @s mg.ks matches 10 run tellraw @a[tag=mg.play] [{"text":"⚡ ","color":"aqua"},{"selector":"@s","color":"white","bold":true},{"text":" : ","color":"gray"},{"text":"UNSTOPPABLE","color":"dark_red","bold":true},{"text":"  (10 kills d'affilée)","color":"gray"}]
execute if score @s mg.ks matches 10 run title @s title [{"text":"UNSTOPPABLE","color":"dark_red","bold":true}]
execute if score @s mg.ks matches 10 run title @s subtitle [{"text":"10 kills d'affilée","color":"gray"}]
execute if score @s mg.ks matches 10 at @s run playsound minecraft:entity.ender_dragon.growl master @a ~ ~ ~ 0.6 0.8
execute if score @s mg.ks matches 15 run tellraw @a[tag=mg.play] [{"text":"⚡ ","color":"aqua"},{"selector":"@s","color":"white","bold":true},{"text":" : ","color":"gray"},{"text":"GODLIKE","color":"light_purple","bold":true},{"text":"  (15 kills d'affilée)","color":"gray"}]
execute if score @s mg.ks matches 15 run title @s title [{"text":"GODLIKE","color":"light_purple","bold":true}]
execute if score @s mg.ks matches 15 run title @s subtitle [{"text":"15 kills d'affilée","color":"gray"}]
execute if score @s mg.ks matches 15 at @s run playsound minecraft:entity.ender_dragon.growl master @a ~ ~ ~ 0.6 0.6
