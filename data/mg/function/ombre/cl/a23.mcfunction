# Piège à loups (3 au plus)
scoreboard players operation $own mg.st = @s mg.olpid
scoreboard players set $n mg.st 0
execute as @e[type=minecraft:marker,tag=mg.oltrap] if score @s mg.olo = $own mg.st run scoreboard players add $n mg.st 1
execute if score $n mg.st matches 3.. as @e[type=minecraft:marker,tag=mg.oltrap,sort=furthest,limit=1] if score @s mg.olo = $own mg.st run function mg:ombre/cl/trap_rm
scoreboard players operation $d mg.st = $pa mg.st
scoreboard players add $d mg.st 10
execute store result storage mg:ombre s.d int 1 run scoreboard players get $d mg.st
execute align xyz positioned ~0.5 ~ ~0.5 run summon minecraft:marker ~ ~ ~ {Tags:["mg.ol","mg.oltrap","mg.olnn"]}
execute align xyz positioned ~0.5 ~ ~0.5 run summon minecraft:block_display ~ ~ ~ {Tags:["mg.ol","mg.oltrapd","mg.olnn"],block_state:{Name:"minecraft:heavy_weighted_pressure_plate"},transformation:{left_rotation:[0f,0f,0f,1f],right_rotation:[0f,0f,0f,1f],translation:[-0.45f,0f,-0.45f],scale:[0.9f,1f,0.9f]}}
scoreboard players add $oltid mg.st 1
scoreboard players operation @e[tag=mg.olnn] mg.olid = $oltid mg.st
scoreboard players operation @e[tag=mg.olnn] mg.olo = $own mg.st
execute store result score @e[tag=mg.olnn,tag=mg.oltrap] mg.olpw run scoreboard players get $d mg.st
tag @e[tag=mg.olnn] remove mg.olnn
playsound minecraft:block.chain.place player @a ~ ~ ~ 0.8 0.8
function mg:ombre/cl/end
