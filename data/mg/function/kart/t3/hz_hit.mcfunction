scoreboard players operation $ko mg.st = @s mg.ri
execute as @a[tag=mg.play] if score @s mg.ri = $ko mg.st unless score @s mg.khi matches 1.. run function mg:kart/hit
