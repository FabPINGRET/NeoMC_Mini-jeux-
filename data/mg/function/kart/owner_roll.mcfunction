scoreboard players operation $ko mg.st = @s mg.ri
execute as @a[tag=mg.play,scores={mg.kit=0}] if score @s mg.ri = $ko mg.st run function mg:kart/item_roll
