# Retire un monstre en trop au hasard (sans butin), $mnc fois
execute unless score $mnc mg.st matches 1.. run return 0
tp @e[tag=mg.mob,tag=!mg.mb0,sort=random,limit=1] ~ -100 ~
kill @e[tag=mg.mob,tag=!mg.mb0,sort=random,limit=1,y=-200,dy=150]
scoreboard players remove $mnc mg.st 1
function mg:mobarena/scale_cull
