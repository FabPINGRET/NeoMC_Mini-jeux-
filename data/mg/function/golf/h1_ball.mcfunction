# @s : sa balle au départ du trou 1 (5 emplacements côte à côte)
scoreboard players operation $gfsl mg.st = @s mg.gfi
scoreboard players operation $gfsl mg.st %= #gf5 mg.st
execute if score $gfsl mg.st matches 0 run summon minecraft:item_display -75.5 66 80.5 {Tags:["mg.fx","mg.gfb","mg.gfnew"],item:{id:"minecraft:snowball",count:1},billboard:"center",view_range:4f,Glowing:1b,teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0.12f,0f],scale:[0.45f,0.45f,0.45f]}}
execute if score $gfsl mg.st matches 1 run summon minecraft:item_display -76.5 66 80.5 {Tags:["mg.fx","mg.gfb","mg.gfnew"],item:{id:"minecraft:snowball",count:1},billboard:"center",view_range:4f,Glowing:1b,teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0.12f,0f],scale:[0.45f,0.45f,0.45f]}}
execute if score $gfsl mg.st matches 2 run summon minecraft:item_display -74.5 66 80.5 {Tags:["mg.fx","mg.gfb","mg.gfnew"],item:{id:"minecraft:snowball",count:1},billboard:"center",view_range:4f,Glowing:1b,teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0.12f,0f],scale:[0.45f,0.45f,0.45f]}}
execute if score $gfsl mg.st matches 3 run summon minecraft:item_display -77.5 66 80.5 {Tags:["mg.fx","mg.gfb","mg.gfnew"],item:{id:"minecraft:snowball",count:1},billboard:"center",view_range:4f,Glowing:1b,teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0.12f,0f],scale:[0.45f,0.45f,0.45f]}}
execute if score $gfsl mg.st matches 4 run summon minecraft:item_display -73.5 66 80.5 {Tags:["mg.fx","mg.gfb","mg.gfnew"],item:{id:"minecraft:snowball",count:1},billboard:"center",view_range:4f,Glowing:1b,teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0.12f,0f],scale:[0.45f,0.45f,0.45f]}}
scoreboard players operation $cur mg.st = @s mg.gfi
execute as @e[tag=mg.gfnew] run function mg:golf/ball_init
function mg:golf/stroke_start
