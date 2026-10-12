# @s bat le record du serveur
scoreboard players operation #srv mg.dsb = @s mg.dtt
item modify entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] contents {function:"minecraft:set_name",entity:"this",target:"custom_name",name:[{selector:"@s",color:"white"}]}
data modify storage mg:dropadv rec set from entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] item.components."minecraft:custom_name"
tellraw @a[tag=!mg.surv] [{"text":"🏆 Nouveau record du serveur : ","color":"gold","bold":true},{"selector":"@s","color":"yellow"},{"text":" en ","color":"gold"},{"score":{"name":"#srv","objective":"mg.dsb"},"color":"white","bold":true},{"text":" essais !","color":"gold"}]
execute as @a[tag=!mg.surv] at @s run playsound minecraft:entity.firework_rocket.twinkle master @s ~ ~ ~ 1 1
