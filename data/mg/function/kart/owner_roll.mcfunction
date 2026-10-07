scoreboard players operation $ko mg.st = @s mg.ri
execute as @a[tag=mg.play,scores={mg.kit=0}] if score @s mg.ri = $ko mg.st unless score @s mg.krl matches 1.. run scoreboard players set @s mg.krl 20
