# @s : leurre frappé à la main
execute on attacker if entity @s[tag=mg.cms] run tag @s add mg.cmhunt
data remove entity @s attack
execute if entity @a[tag=mg.cmhunt] at @s run function mg:cham/decoy_pop
tag @a remove mg.cmhunt
