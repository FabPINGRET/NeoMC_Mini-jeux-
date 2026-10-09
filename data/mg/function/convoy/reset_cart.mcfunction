# Convoi au départ
kill @e[tag=mg.cvc]
kill @e[tag=mg.cvl]
summon minecraft:block_display -59.5 81 21200.5 {Tags:["mg.cvc"],Glowing:1b,teleport_duration:2,block_state:{Name:"minecraft:barrel",Properties:{facing:"up"}},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.8f,0f,-0.8f],scale:[1.6f,1.3f,1.6f]}}
summon minecraft:text_display -59.5 83 21200.5 {Tags:["mg.cvl"],billboard:"center",teleport_duration:2,text:{"text":"🚚 CONVOI","color":"gold","bold":true}}
scoreboard players set $cvh mg.st 100
scoreboard players set $cvt mg.st 0
scoreboard players set $cvp mg.st 0
bossbar add mg:convoy {"text":"🚚 Convoi"}
bossbar set mg:convoy max 120
bossbar set mg:convoy value 0
bossbar set mg:convoy color yellow
bossbar set mg:convoy players @a[tag=mg.play]
