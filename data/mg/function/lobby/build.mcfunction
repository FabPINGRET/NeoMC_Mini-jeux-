# Lobby (centre 0 64 0, sol en y=63)
fill -15 63 -15 15 63 15 minecraft:quartz_block
fill -15 63 -15 15 63 -15 minecraft:sea_lantern
fill -15 63 15 15 63 15 minecraft:sea_lantern
fill -15 63 -15 -15 63 15 minecraft:sea_lantern
fill 15 63 -15 15 63 15 minecraft:sea_lantern
fill -1 63 -1 1 63 1 minecraft:gold_block
fill -8 63 -8 -8 63 -8 minecraft:glowstone
fill 8 63 -8 8 63 -8 minecraft:glowstone
fill -8 63 8 -8 63 8 minecraft:glowstone
fill 8 63 8 8 63 8 minecraft:glowstone

# Panneau flottant
kill @e[type=minecraft:text_display,tag=mg.deco]
summon minecraft:text_display 0.5 67.5 8.5 {Tags:["mg.deco"],billboard:"center",text:[{"text":"✦ MINI-JEUX ✦","color":"gold","bold":true}],transformation:{translation:[0f,0f,0f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[4f,4f,4f]}}
