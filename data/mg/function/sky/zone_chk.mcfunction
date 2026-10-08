# Dans la zone ? (@s, positionné au centre à sa hauteur) — macro {r}
$execute if entity @s[distance=..$(r)] run return run scoreboard players set @s mg.sko 0
execute if score @s mg.sko matches 0 run title @s subtitle [{"text":"Hors de la zone : 3 s pour revenir !","color":"red"}]
execute if score @s mg.sko matches 0 run title @s title [{"text":"⚠","color":"red","bold":true}]
execute if score @s mg.sko matches 0 run playsound minecraft:block.note_block.bass master @s ~ ~ ~ 1 0.6
scoreboard players add @s mg.sko 5
