# @s : serveur (joueur ou robot, à sa position) — lance la balle en l'air ; frappe auto au sommet
kill @e[type=minecraft:item_display,tag=mg.tnball,tag=mg.tnk]
scoreboard players operation $tnside mg.st = @s mg.tns
summon minecraft:item_display ^ ^1.2 ^0.6 {Tags:["mg.tent","mg.npc","mg.tnball","mg.tnnew"],item:{id:"minecraft:firework_star",count:1,components:{"minecraft:firework_explosion":{shape:"small_ball",colors:[I;13434675]}}},billboard:"center",teleport_duration:1,transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[0.45f,0.45f,0.45f]}}
execute as @e[type=minecraft:item_display,tag=mg.tnnew] run function mg:tennis/toss_ball
scoreboard players set @e[type=minecraft:marker,tag=mg.tncm,tag=mg.tnk,limit=1] mg.tnph 1
playsound minecraft:entity.snowball.throw master @a[tag=!mg.surv,distance=..40] ~ ~ ~ 0.6 1.4
