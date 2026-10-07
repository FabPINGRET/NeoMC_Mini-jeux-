scoreboard players set @s mg.krk 1
scoreboard players operation $me mg.st = @s mg.kpg
tag @s add mg.kme
execute as @a[tag=mg.play] if score @s mg.kpg > $me mg.st run scoreboard players add @a[tag=mg.kme,limit=1] mg.krk 1
tag @s remove mg.kme
