# Un plot (macro) : murs de barrières invisibles sur toute la hauteur, sol au premier passage, panneau flottant
$function mg:plot/walls {x1:$(wx1),x2:$(wx2),z1:$(wz1),z2:$(wz2)}
$execute unless data storage mg:plot built.p$(n) run fill $(bx1) 63 $(bz1) $(bx2) 63 $(bz2) minecraft:stone_bricks
$execute unless data storage mg:plot built.p$(n) run fill $(gx1) 63 $(gz1) $(gx2) 63 $(gz2) minecraft:grass_block
$data modify storage mg:plot built.p$(n) set value 1b
$kill @e[type=minecraft:text_display,tag=mg.pd$(n)]
$summon minecraft:text_display $(lx) 80 $(lz) {Tags:["mg.pdisp","mg.pd$(n)"],billboard:"center",text:[{"text":"PLOT $(n)","color":"gold","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[3f,3f,3f]}}
$data modify storage mg:plot cur set value {n:$(n),name:""}
function mg:plot/label_get with storage mg:plot cur
