# Achat (@s, macro n = objectif de l'objet, p = prix, t = nom)
$execute unless score @s mg.mpm matches $(p).. run return run tellraw @s [{"text":"Pas assez de pièces ($(p) nécessaires).","color":"red"}]
$scoreboard players remove @s mg.mpm $(p)
$scoreboard players add @s mg.$(n) 1
$tellraw @a[tag=mg.mpp] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" achète $(t)","color":"gray"}]
execute at @s run playsound minecraft:entity.villager.yes master @s ~ ~ ~ 1 1
function mg:party/shop_close
