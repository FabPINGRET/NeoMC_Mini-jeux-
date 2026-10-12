# @s : son arc tombe à ses pieds
clear @s minecraft:bow
clear @s minecraft:arrow
execute at @s run summon minecraft:item ~ ~1 ~ {Tags:["mg.mmb","mg.keep"],PickupDelay:40s,Age:-32768s,Glowing:1b,Invulnerable:1b,Item:{id:"minecraft:bow",count:1,components:{"minecraft:unbreakable":{},"minecraft:custom_data":{mg_mm:1b},"minecraft:custom_name":{"text":"🏹 Arc du détective","color":"aqua","italic":false}}}}
function mg:mm/bow_news
