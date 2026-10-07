tag @s add mg.kme
execute as @a[tag=mg.play,tag=!mg.kme] run function mg:kart/hit
tag @s remove mg.kme
execute as @a[tag=mg.play] at @s run playsound minecraft:entity.lightning_bolt.thunder master @s ~ ~ ~ 0.6 1.4
tellraw @a[tag=mg.play] [{"text":"★ ","color":"gold"},{"selector":"@s","color":"yellow"},{"text":" foudroie tout le monde ⚡","color":"aqua"}]
