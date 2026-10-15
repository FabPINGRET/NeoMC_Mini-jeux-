# 🎃 Halloween : PNJ « 🎃 Sorcière » (corps, zone cliquable, indication) ; idempotent, appelé par lobby/theme/halloween/reskin et chaque seconde par lobby/theme/halloween/fx
execute in minecraft:overworld unless loaded 22 64 22 run return 0
execute as @e[tag=mg.thnpc,tag=mg.thmob] run function mg:lobby/theme/gone
kill @e[tag=mg.thnpc]
execute in minecraft:overworld run summon minecraft:witch 22.5 64 22.5 {Rotation:[135f,0f],Tags:["mg.thx","mg.thmob","mg.thnpc"],NoAI:1b,Silent:1b,Invulnerable:1b,PersistenceRequired:1b,DeathLootTable:"minecraft:empty",CustomName:{"text":"Sorcière","color":"gold"},equipment:{mainhand:{id:"minecraft:suspicious_stew",count:1}},drop_chances:{mainhand:0f}}
execute in minecraft:overworld run summon minecraft:interaction 22.5 64 22.5 {Tags:["mg.thx","mg.thnpc","mg.thnpci"],width:0.9f,height:2.1f,response:1b}
execute in minecraft:overworld run summon minecraft:text_display 22.5 66.45 22.5 {Tags:["mg.thx","mg.thnpc"],billboard:"center",background:0,shadow:1b,text:[{"text":"🎃 Sorcière","color":"gold","bold":true},{"text":"\nClic droit","color":"yellow"}]}
