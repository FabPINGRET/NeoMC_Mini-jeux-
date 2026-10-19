# @s = zone de banc avec un clic enregistré ; pas celui du joueur mg.lbc : on la laisse
execute on target unless entity @s[tag=mg.lbc] run return 0
# on target lit le champ interaction : appeler bench_click avant de le vider ; « at @s » avant « on target » : @s devient le joueur, la position reste celle du banc
execute at @s on target run function mg:lobby/sit/bench_click
data remove entity @s interaction
