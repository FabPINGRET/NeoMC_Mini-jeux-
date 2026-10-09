# @s : placé 1,3 bloc derrière sa balle, face au trou, regard baissé vers la balle
tag @s add mg.gfme
execute as @e[tag=mg.gfmy,limit=1] at @s facing entity @e[tag=mg.gftg,limit=1] feet rotated ~ 0 run function mg:golf/place_b
tag @s remove mg.gfme
