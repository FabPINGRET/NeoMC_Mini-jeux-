# @s : mission « Chasse : le carnotaure » (un carnotaure traqué, apparu loin de la colonie si besoin)
scoreboard players set @s mg.tvm 4
execute unless entity @e[tag=mg.tvhunt] as @e[type=minecraft:marker,tag=mg.tvfar,sort=random,limit=1] at @s run function mg:terra/hunt_spawn
function mg:terra/hunt_loc
tellraw @s [{"text":"🦖 Mission : ","color":"red","bold":true},{"text":"un carnotaure rôde. Suis le 📡 et abats-le (prends du renfort !). ","color":"gray"},{"text":"+400 ₵","color":"green"}]
