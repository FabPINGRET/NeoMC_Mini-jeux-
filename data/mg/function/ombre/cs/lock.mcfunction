tag @s add mg.olcsme
execute as @e[tag=mg.olcam] if score @s mg.olo = $own mg.st run spectate @s @a[tag=mg.olcsme,limit=1]
tag @s remove mg.olcsme
