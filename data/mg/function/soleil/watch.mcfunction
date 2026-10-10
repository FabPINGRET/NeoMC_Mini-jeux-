# La poupée regarde : positions notées, toute la durée du feu rouge
scoreboard players set $sqp mg.st 2
execute store result score $sqt mg.st run random value 40..80
execute as @e[tag=mg.sqeye] run data merge entity @s {block_state:{Name:"minecraft:redstone_block"}}
execute as @a[tag=mg.play,tag=!mg.sqf] run function mg:soleil/mark
