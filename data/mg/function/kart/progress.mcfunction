scoreboard players operation @s mg.kpg = @s mg.klp
scoreboard players operation @s mg.kpg *= #k1000 mg.st
scoreboard players operation @s mg.kpg += @s mg.kcp
execute if entity @s[tag=mg.kfin] run scoreboard players set @s mg.kpg 900000
execute if entity @s[tag=mg.kfin] run scoreboard players operation @s mg.kpg -= @s mg.kfp
