# @s : largue une bombe de type $(t) sous ses pieds, lancée dans la direction du regard
$scoreboard players set @s mg.$(cd) $(cdv)
execute anchored eyes positioned ^ ^ ^1 run summon minecraft:marker ~ ~ ~ {Tags:["mg.bdm"]}
execute store result score $fx mg.st run data get entity @e[type=minecraft:marker,tag=mg.bdm,limit=1] Pos[0] 1000
execute store result score $fy mg.st run data get entity @e[type=minecraft:marker,tag=mg.bdm,limit=1] Pos[1] 1000
execute store result score $fz mg.st run data get entity @e[type=minecraft:marker,tag=mg.bdm,limit=1] Pos[2] 1000
kill @e[type=minecraft:marker,tag=mg.bdm]
execute store result score $px0 mg.st run data get entity @s Pos[0] 1000
execute store result score $py0 mg.st run data get entity @s Pos[1] 1000
execute store result score $pz0 mg.st run data get entity @s Pos[2] 1000
scoreboard players operation $fx mg.st -= $px0 mg.st
scoreboard players operation $fy mg.st -= $py0 mg.st
scoreboard players remove $fy mg.st 1620
scoreboard players operation $fz mg.st -= $pz0 mg.st
execute positioned ~ 168.7 ~ run summon minecraft:tnt ~ ~ ~ {Tags:["mg.bomb","mg.bnew"],fuse:400s,explosion_power:0.0f}
$execute store result entity @e[type=minecraft:tnt,tag=mg.bnew,limit=1] Motion[0] double $(sp) run scoreboard players get $fx mg.st
$execute store result entity @e[type=minecraft:tnt,tag=mg.bnew,limit=1] Motion[1] double $(sp) run scoreboard players get $fy mg.st
$execute store result entity @e[type=minecraft:tnt,tag=mg.bnew,limit=1] Motion[2] double $(sp) run scoreboard players get $fz mg.st
scoreboard players operation @e[type=minecraft:tnt,tag=mg.bnew] mg.bid = @s mg.bid
$scoreboard players set @e[type=minecraft:tnt,tag=mg.bnew] mg.bty $(t)
scoreboard players set @e[type=minecraft:tnt,tag=mg.bnew] mg.bc4 0
$function mg:bomber/look_$(t)
tag @e[tag=mg.bnew] remove mg.bnew
playsound minecraft:entity.tnt.primed player @a ~ ~ ~ 0.8 1.2
