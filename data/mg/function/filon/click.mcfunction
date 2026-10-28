# @s = interaction cliquée sur l'île
execute on target run tag @s add mg.fnby
data remove entity @s interaction
execute if entity @s[tag=mg.fni_sell] as @a[tag=mg.fnby,tag=mg.fnw] run function mg:filon/sell
execute if entity @s[tag=mg.fni_shop] as @a[tag=mg.fnby,tag=mg.fnw] run function mg:filon/shop
execute if entity @s[tag=mg.fni_mkt] as @a[tag=mg.fnby,tag=mg.fnw] run function mg:filon/market_show
execute if entity @s[tag=mg.fni_exit] as @a[tag=mg.fnby,tag=mg.fnw] run function mg:filon/leave
tag @a remove mg.fnby
