# @s : plus de mission (caisse posée ou portée retirée, localisateur vers la colonie)
scoreboard players operation $own mg.st = @s mg.tvpid
execute as @e[tag=mg.tvcrate] if score @s mg.tvo = $own mg.st run kill @s
execute as @e[tag=mg.tvcarry] if score @s mg.tvo = $own mg.st run kill @s
tag @s remove mg.tvcar
effect clear @s minecraft:slowness
scoreboard players set @s mg.tvm 0
scoreboard players set @s mg.tvmp 0
scoreboard players set @s mg.tvmo 0
execute if entity @s[tag=mg.tvw] run function mg:terra/loc {x:0,y:65,z:0}
