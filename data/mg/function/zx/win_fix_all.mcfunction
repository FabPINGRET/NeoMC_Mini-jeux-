# Toutes les 0,5 s : un joueur accroupi devant une fenêtre abîmée recloue une planche
scoreboard players set $zxt mg.st 0
execute as @e[type=minecraft:marker,tag=mg.zwin,scores={mg.zws=..5},distance=..80] at @s as @a[tag=mg.play,tag=!mg.zdead,distance=..2.6,sort=nearest,limit=1] if predicate mg:sneak run function mg:zx/win_fix
