# 👑 King of the Hill — tick
scoreboard players add $kht mg.st 1
execute as @a[tag=mg.play,scores={mg.deaths=1..}] run function mg:koth/respawn
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,scores={mg.t=..74}] run function mg:koth/respawn
tag @a remove mg.khz
tag @a[tag=mg.play,x=-2,y=85,z=20398,dx=4,dy=3,dz=4,gamemode=!spectator] add mg.khz
execute store result score $khn mg.st if entity @a[tag=mg.khz]
execute store result score $khr mg.st if entity @a[tag=mg.khz,team=mg_red]
execute store result score $khb mg.st if entity @a[tag=mg.khz,team=mg_blue]
scoreboard players operation $khq mg.st = $kht mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $khq mg.st %= #20 mg.st
execute if score $khq mg.st matches 0 run function mg:koth/second
execute if score $kht mg.st matches 4800 run tellraw @a[tag=mg.play] {"text":"👑 Plus qu'une minute !","color":"gold"}
execute if score $state mg.st matches 2 if score $kht mg.st matches 6000.. run function mg:koth/timeout
execute store result score $alive mg.st if entity @a[tag=mg.play]
execute if score $state mg.st matches 2 if score $alive mg.st matches 0 run function mg:core/draw
