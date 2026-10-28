# Chaque seconde : zombies tombés hors de la carte ou perdus
execute as @e[tag=mg.zz,x=-44,y=-64,z=39034,dx=92,dy=384,dz=94] at @s if entity @s[y=-64,dy=139] run function mg:zm4/lost
execute as @e[tag=mg.zz,x=-44,y=-64,z=39034,dx=92,dy=384,dz=94] at @s unless entity @a[tag=mg.play,tag=!mg.zdead,distance=..48] run function mg:zm4/lost
execute positioned 2 80 39081 run function mg:zx/second
execute if score $zleft mg.st matches ..0 if score $zal mg.st matches ..3 run effect give @e[tag=mg.zz,x=-44,y=-64,z=39034,dx=92,dy=384,dz=94] minecraft:glowing infinite 0 true
execute if score $zph mg.st matches 1 run title @a[tag=mg.play] actionbar [{"text":"🧟 Manche ","color":"dark_green"},{"score":{"name":"$zr","objective":"mg.st"},"color":"green","bold":true},{"text":" — restants : ","color":"gray"},{"score":{"name":"$zal","objective":"mg.st"},"color":"yellow"},{"text":" + ","color":"gray"},{"score":{"name":"$zleft","objective":"mg.st"},"color":"yellow"}]
