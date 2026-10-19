# Sethkar, le pharaon-liche : jars
execute if score $hp mg.st matches 513.. run return 0
execute if score $obp4 mg.st matches 1.. run return run function mg:ombre/boss/sethkar/jarchk
scoreboard players set $obp4 mg.st 1
data merge entity @s {Invulnerable:1b}
tellraw @a[distance=..40] {"text":"Sethkar se réfugie dans sa magie : brise les trois vases canopes (clic droit) !","color":"gold","bold":true}
summon minecraft:interaction 192.0 65 -34.0 {Tags:["mg.ol","mg.oljar"],width:1.2f,height:1.6f,response:1b}
summon minecraft:interaction 206.0 65 -34.0 {Tags:["mg.ol","mg.oljar"],width:1.2f,height:1.6f,response:1b}
summon minecraft:interaction 199.0 65 -20.0 {Tags:["mg.ol","mg.oljar"],width:1.2f,height:1.6f,response:1b}
summon minecraft:item_display 192.0 65.6 -34.0 {Tags:["mg.ol","mg.oljar","mg.oljard"],item:{id:"minecraft:decorated_pot",count:1},Glowing:1b,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:item_display 206.0 65.6 -34.0 {Tags:["mg.ol","mg.oljar","mg.oljard"],item:{id:"minecraft:decorated_pot",count:1},Glowing:1b,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
summon minecraft:item_display 199.0 65.6 -20.0 {Tags:["mg.ol","mg.oljar","mg.oljard"],item:{id:"minecraft:decorated_pot",count:1},Glowing:1b,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.2f,1.2f,1.2f]}}
