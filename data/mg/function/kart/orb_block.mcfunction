# Carapace stoppée par un objet en orbite (@s = orbite la plus proche) : les deux disparaissent, le pilote perd une charge
scoreboard players operation $ko mg.st = @s mg.ri
execute as @a[tag=mg.play] if score @s mg.ri = $ko mg.st run function mg:kart/orb_lost
kill @s
kill @e[type=minecraft:item_display,tag=mg.kcur]
