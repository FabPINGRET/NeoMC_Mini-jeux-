# @s : zone touchable frappée à la main
execute on attacker if entity @s[tag=mg.cms] run tag @s add mg.cmhunt
data remove entity @s attack
execute if entity @a[tag=mg.cmhunt] run function mg:cham/shot_hit
tag @a remove mg.cmhunt
