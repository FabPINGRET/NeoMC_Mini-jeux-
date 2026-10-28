# Chaque seconde : zombies tombés hors de la carte ou perdus
execute as @e[tag=mg.zz,x=-25,y=-64,z=23153,dx=72,dy=384,dz=72] at @s if entity @s[y=-64,dy=139] run function mg:zm/lost
execute as @e[tag=mg.zz,x=-25,y=-64,z=23153,dx=72,dy=384,dz=72] at @s unless entity @a[tag=mg.play,tag=!mg.zdead,distance=..48] run function mg:zm/lost
execute positioned 11 80 23189 run function mg:zx/second
execute if score $zleft mg.st matches ..0 if score $zal mg.st matches ..3 run effect give @e[tag=mg.zz,x=-25,y=-64,z=23153,dx=72,dy=384,dz=72] minecraft:glowing infinite 0 true
execute if score $zph mg.st matches 1 run title @a[tag=mg.play] actionbar [{"text":"🧟 Manche ","color":"dark_green"},{"score":{"name":"$zr","objective":"mg.st"},"color":"green","bold":true},{"text":" — restants : ","color":"gray"},{"score":{"name":"$zal","objective":"mg.st"},"color":"yellow"},{"text":" + ","color":"gray"},{"score":{"name":"$zleft","objective":"mg.st"},"color":"yellow"}]
