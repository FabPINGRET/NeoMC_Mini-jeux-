# 🧪 Infection — tick
scoreboard players add $ift mg.st 1
execute as @a[tag=mg.play] store result score @s mg.t run data get entity @s Pos[1]
execute as @a[tag=mg.play,tag=!mg.inf,scores={mg.t=..74}] run scoreboard players set @s mg.deaths 1
execute as @a[tag=mg.play,tag=!mg.inf,scores={mg.deaths=1..}] run function mg:inf3/make_zombie
execute as @a[tag=mg.play,tag=mg.inf,scores={mg.t=..74}] run scoreboard players set @s mg.deaths 1
execute as @a[tag=mg.play,tag=mg.inf,scores={mg.deaths=1..}] run function mg:inf3/zdie
execute store result score $ins mg.st if entity @a[tag=mg.play,tag=!mg.inf]
scoreboard players operation $inq mg.st = $ift mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $inq mg.st %= #20 mg.st
execute if score $inq mg.st matches 0 run function mg:inf3/second
execute if score $state mg.st matches 2 if score $ins mg.st matches 0 run return run function mg:inf3/zombies_win
execute if score $state mg.st matches 2 if score $ift mg.st matches 3600.. run function mg:inf3/survivors_win
