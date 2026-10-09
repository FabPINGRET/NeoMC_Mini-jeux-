# @s : la quille tombe (côté de sa vitesse dominante) et glisse
tag @s add mg.bpdn
tag @s add mg.bpmv
scoreboard players operation #ax mg.st = @s mg.bvx
execute if score #ax mg.st matches ..-1 run scoreboard players operation #ax mg.st *= #km1 mg.st
scoreboard players operation #az mg.st = @s mg.bvz
execute if score #az mg.st matches ..-1 run scoreboard players operation #az mg.st *= #km1 mg.st
execute if score #az mg.st >= #ax mg.st if score @s mg.bvz matches 0.. run return run data merge entity @s {start_interpolation:0,interpolation_duration:6,transformation:{left_rotation:[0.7071f,0f,0f,0.7071f],right_rotation:[0f,0f,0f,1f],translation:[-1.5f,1.6875f,0f],scale:[3.0f,3.0f,3.0f]}}
execute if score #az mg.st >= #ax mg.st run return run data merge entity @s {start_interpolation:0,interpolation_duration:6,transformation:{left_rotation:[-0.7071f,0f,0f,0.7071f],right_rotation:[0f,0f,0f,1f],translation:[-1.5f,-1.3125f,0f],scale:[3.0f,3.0f,3.0f]}}
execute if score @s mg.bvx matches 0.. run return run data merge entity @s {start_interpolation:0,interpolation_duration:6,transformation:{left_rotation:[0f,0f,-0.7071f,0.7071f],right_rotation:[0f,0f,0f,1f],translation:[0f,1.6875f,-1.5f],scale:[3.0f,3.0f,3.0f]}}
data merge entity @s {start_interpolation:0,interpolation_duration:6,transformation:{left_rotation:[0f,0f,0.7071f,0.7071f],right_rotation:[0f,0f,0f,1f],translation:[0f,-1.3125f,-1.5f],scale:[3.0f,3.0f,3.0f]}}
