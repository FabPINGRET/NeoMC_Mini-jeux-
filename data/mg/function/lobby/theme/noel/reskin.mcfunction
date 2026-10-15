# 🎄 Noël : entités du décor (mg.lby) ; rappelé par lobby/deco tant que le thème est actif
function mg:lobby/theme/clear
execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents *[minecraft:item_model="mg:balloon"] run item replace entity @s contents with minecraft:snow_block
execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents *[minecraft:item_model="mg:item_box"] run item replace entity @s contents with minecraft:red_shulker_box
execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents *[minecraft:item_model="mg:crystal"] run item replace entity @s contents with minecraft:blue_ice
execute as @e[type=minecraft:item_display,tag=mg.lby] if items entity @s contents minecraft:amethyst_cluster run item replace entity @s contents with minecraft:blue_ice
execute as @e[type=minecraft:armor_stand,tag=mg.lby] run item replace entity @s armor.head with minecraft:leather_helmet[minecraft:dyed_color=13369344]
summon minecraft:text_display 0.5 74 0.5 {Tags:["mg.lby","mg.thx"],billboard:"center",background:1426063360,shadow:1b,text:[{"text":"🎄 Joyeux Noël ! 🎄","color":"red","bold":true},{"text":"\net bonnes fêtes sur NeoMC","color":"dark_green","italic":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[2f,2f,2f]}}
function mg:lobby/theme/noel/npc
