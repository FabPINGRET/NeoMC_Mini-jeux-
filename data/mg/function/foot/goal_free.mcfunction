# But sans équipe sur le terrain : compteur de buts libres
scoreboard players add $ftg mg.ft 1
title @a[x=-17,y=46,z=-41,dx=38,dy=17,dz=27] subtitle [{"text":"buts libres : ","color":"gray"},{"score":{"name":"$ftg","objective":"mg.ft"},"color":"yellow"}]
title @a[x=-17,y=46,z=-41,dx=38,dy=17,dz=27] title {"text":"⚽ But !","color":"gold","bold":true}
function mg:foot/goal_fx
