# Bonus RPG d'un slasher abattu (appelé par terra/k_raptor avant la remise à zéro)
scoreboard players operation @s mg.trgr += @s mg.tvkr
scoreboard players operation $kx mg.st = @s mg.tvkr
scoreboard players operation $kx mg.st *= #12 mg.st
execute store result storage mg:terra s.n int 1 run scoreboard players get $kx mg.st
function mg:terra/rpg/xpk with storage mg:terra s
execute if score @s mg.trch matches 10 run scoreboard players operation @s mg.trqp += @s mg.tvkr
execute if score @s mg.trch matches 10 if score @s mg.trqp matches ..2 run tellraw @s [{"text":"🦖 Premiers pas : ","color":"gold"},{"score":{"name":"@s","objective":"mg.trqp"},"color":"yellow","bold":true},{"text":" / 3 slashers","color":"yellow"}]
execute if score @s mg.trch matches 10 if score @s mg.trqp matches 3.. run function mg:terra/rpg/ch {n:15}
