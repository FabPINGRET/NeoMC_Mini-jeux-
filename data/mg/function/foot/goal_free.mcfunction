# But sans équipe sur le terrain : +1 buts libres au dernier toucheur ($ftg : total, stats admin) ; chacun ne voit que SON score
scoreboard players add $ftg mg.ft 1
scoreboard players add @a[tag=mg.ftlt] mg.ft 1
title @a[x=-17,y=46,z=-41,dx=38,dy=8,dz=27] subtitle [{"text":"tes buts libres : ","color":"gray"},{"score":{"name":"*","objective":"mg.ft"},"color":"yellow"}]
title @a[x=-17,y=46,z=-41,dx=38,dy=8,dz=27] title {"text":"⚽ But !","color":"gold","bold":true}
tag @a remove mg.ftlt
function mg:foot/goal_fx
