# Chaque seconde : zombies tombés hors de la carte ou perdus
execute as @e[type=minecraft:zombie,tag=mg.zz] at @s if entity @s[y=-64,dy=139] run function mg:zm/lost
execute as @e[type=minecraft:zombie,tag=mg.zz] at @s unless entity @a[tag=mg.play,tag=!mg.zdead,distance=..48] run function mg:zm/lost
execute if score $zph mg.st matches 1 run title @a[tag=mg.play] actionbar [{"text":"🧟 Manche ","color":"dark_green"},{"score":{"name":"$zr","objective":"mg.st"},"color":"green","bold":true},{"text":" — restants : ","color":"gray"},{"score":{"name":"$zal","objective":"mg.st"},"color":"yellow"},{"text":" + ","color":"gray"},{"score":{"name":"$zleft","objective":"mg.st"},"color":"yellow"}]
