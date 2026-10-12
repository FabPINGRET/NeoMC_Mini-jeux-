scoreboard players set $evtk mg.st 0
tag @a remove mg.evl
execute in minecraft:overworld run tag @a[x=-70,y=30,z=-70,dx=140,dy=100,dz=140,tag=!mg.play,tag=!mg.surv,gamemode=!spectator] add mg.evl
execute unless score $evn mg.st matches -2147483648.. run scoreboard players set $evn mg.st 1800
execute if score $evon mg.st matches 1.. unless score $state mg.st matches 0 run return run function mg:lobby/ev/stop
execute if score $evon mg.st matches 1.. run return run function mg:lobby/ev/run
execute unless score $state mg.st matches 0 if score $evn mg.st matches 1..60 run function mg:lobby/ev/postpone
execute unless entity @a[tag=mg.evl] if score $evn mg.st matches 1..60 run function mg:lobby/ev/postpone
execute unless score $state mg.st matches 0 run return 0
execute unless entity @a[tag=mg.evl] run return 0
scoreboard players remove $evn mg.st 1
execute if score $evn mg.st matches 60 run function mg:lobby/ev/pick
execute if score $evn mg.st matches 1..60 run function mg:lobby/ev/countdown
execute if score $evn mg.st matches ..0 run function mg:lobby/ev/start
