# Bonus de série (@s, macro : n kills, b pièces, t texte)
$scoreboard players add @s mg.pco $(b)
$tellraw @a[tag=mg.pvpc] [{"text":"🔥 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" $(t) ($(n) kills d'affilée) : +$(b) 💰","color":"red"}]
execute as @a[tag=mg.pvpc] at @s run playsound minecraft:entity.blaze.shoot master @s ~ ~ ~ 0.6 1.4
