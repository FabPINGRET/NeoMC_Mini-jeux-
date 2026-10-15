# 🎃 Halloween : entités du décor (mg.lby) ; rappelé par lobby/deco tant que le thème est actif
function mg:lobby/theme/clear
execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents *[minecraft:item_model="mg:balloon"] if score $rp mg.st matches 1 run function mg:lobby/theme/halloween/pumpkin_lit
execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents *[minecraft:item_model="mg:item_box"] if score $rp mg.st matches 1 run function mg:lobby/theme/halloween/pumpkin_carved
execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents *[minecraft:item_model="mg:star"] if score $rp mg.st matches 1 run function mg:lobby/theme/halloween/pumpkin_lit
execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents minecraft:nether_star if score $rp mg.st matches 1 run function mg:lobby/theme/halloween/pumpkin_lit
execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents *[minecraft:item_model="mg:balloon"] run item replace entity @s contents with minecraft:jack_o_lantern
execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents *[minecraft:item_model="mg:item_box"] run item replace entity @s contents with minecraft:carved_pumpkin
execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents *[minecraft:item_model="mg:star"] run item replace entity @s contents with minecraft:jack_o_lantern
execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents minecraft:nether_star run item replace entity @s contents with minecraft:jack_o_lantern
execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents *[minecraft:item_model="mg:crystal"] run item replace entity @s contents with minecraft:wither_skeleton_skull
execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents minecraft:amethyst_cluster run item replace entity @s contents with minecraft:wither_skeleton_skull
execute as @e[type=minecraft:armor_stand,tag=mg.lby] run item replace entity @s armor.head with minecraft:carved_pumpkin
summon minecraft:text_display 0.5 74 0.5 {Tags:["mg.lby","mg.thx"],billboard:"center",background:1426063360,shadow:1b,text:[{"text":"🎃 Joyeux Halloween ! 🎃","color":"gold","bold":true},{"text":"\nBonbons ou mini-jeux ?","color":"dark_purple","italic":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
