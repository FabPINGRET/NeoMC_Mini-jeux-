scoreboard players set $pvt mg.st 0
execute as @a[tag=mg.pvpc,scores={mg.phc=0}] run title @s actionbar [{"text":"💰 ","color":"gold"},{"score":{"name":"@s","objective":"mg.pco"},"color":"yellow","bold":true},{"text":" pièces   ","color":"gold"},{"text":"🔥 série ","color":"red"},{"score":{"name":"@s","objective":"mg.pks"},"color":"red","bold":true}]
execute as @e[type=minecraft:wolf,tag=mg.pdog] run function mg:pvpc/dog_check
scoreboard players add $pvc mg.st 1
execute if score $pvc mg.st matches 15.. run function mg:pvpc/coin_spawn
