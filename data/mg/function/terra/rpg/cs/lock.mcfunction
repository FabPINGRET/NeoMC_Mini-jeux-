tag @s add mg.trcsme
execute as @e[type=minecraft:item_display,tag=mg.trcam] if score @s mg.tvo = $own mg.st run spectate @s @a[tag=mg.trcsme,limit=1]
tag @s remove mg.trcsme
