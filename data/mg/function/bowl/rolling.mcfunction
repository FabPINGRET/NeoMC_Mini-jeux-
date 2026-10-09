# @s : la boule roule (bruit de roulement), fin quand elle est dans la fosse
scoreboard players operation #ln mg.st = @s mg.bln
scoreboard players set #n mg.st 0
execute as @e[type=minecraft:item_display,tag=mg.bball] if score @s mg.bln = #ln mg.st run scoreboard players add #n mg.st 1
scoreboard players operation #q mg.st = @s mg.btm
scoreboard players set #k mg.st 4
scoreboard players operation #q mg.st %= #k mg.st
execute if score #q mg.st matches 0 as @e[type=minecraft:item_display,tag=mg.bball] if score @s mg.bln = #ln mg.st at @s run playsound minecraft:block.wood.step master @a[tag=!mg.surv,distance=..24] ~ ~ ~ 0.5 0.5
execute if score @s mg.btm matches 300.. as @e[type=minecraft:item_display,tag=mg.bball] if score @s mg.bln = #ln mg.st run kill @s
execute if score #n mg.st matches 0 run scoreboard players set @s mg.btm 0
execute if score #n mg.st matches 0 run scoreboard players set @s mg.bph 2
