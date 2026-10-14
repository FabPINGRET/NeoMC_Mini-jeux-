# @s est mort en portant la caisse : elle retombe là où il était (dernière position connue)
execute store result storage mg:terra d.x int 1 run scoreboard players get @s mg.tvx
execute store result storage mg:terra d.y int 1 run scoreboard players get @s mg.tvy
execute store result storage mg:terra d.z int 1 run scoreboard players get @s mg.tvz
scoreboard players operation $own mg.st = @s mg.tvpid
execute as @e[tag=mg.tvcarry] if score @s mg.tvo = $own mg.st run kill @s
function mg:terra/crate_drop_at with storage mg:terra d
tag @s remove mg.tvcar
effect clear @s minecraft:slowness
function mg:terra/loc with storage mg:terra d
tellraw @s {"text":"📦 Tu as lâché la caisse là où tu es tombé (📡).","color":"yellow"}
