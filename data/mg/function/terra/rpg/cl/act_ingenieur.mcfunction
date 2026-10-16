# @s (ingénieur) : tourelle automatique à ses pieds (une seule par ingénieur)
scoreboard players operation $own mg.st = @s mg.tvpid
execute as @e[tag=mg.trtur] if score @s mg.tvo = $own mg.st run kill @s
execute align xz positioned ~0.5 ~ ~0.5 run summon minecraft:marker ~ ~ ~ {Tags:["mg.tv","mg.trtur","mg.trtm","mg.trtn"]}
execute align xz positioned ~0.5 ~ ~0.5 run summon minecraft:block_display ~ ~ ~ {Tags:["mg.tv","mg.trtur","mg.trtn"],block_state:{Name:"minecraft:dispenser",Properties:{facing:"up"}},transformation:{translation:[-0.35f,0f,-0.35f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[0.7f,0.7f,0.7f]}}
execute align xz positioned ~0.5 ~ ~0.5 run summon minecraft:block_display ~ ~ ~ {Tags:["mg.tv","mg.trtur","mg.trtn"],block_state:{Name:"minecraft:lightning_rod"},transformation:{translation:[-0.5f,0.7f,-0.5f],left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],scale:[1f,0.8f,1f]}}
scoreboard players operation @e[tag=mg.trtn] mg.tvo = $own mg.st
execute if score $rk mg.st matches ..2 run scoreboard players set @e[tag=mg.trtn,tag=mg.trtm] mg.tvst 20
execute if score $rk mg.st matches 3.. run scoreboard players set @e[tag=mg.trtn,tag=mg.trtm] mg.tvst 30
execute if score $rk mg.st matches 2.. run tag @e[tag=mg.trtn,tag=mg.trtm] add mg.trtx
tag @e[tag=mg.trtn] remove mg.trtn
playsound minecraft:block.anvil.place player @a ~ ~ ~ 0.6 1.6
