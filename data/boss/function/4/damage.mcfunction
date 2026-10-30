scoreboard players remove boss:ed BossHealth 1
playsound minecraft:entity.strider.hurt hostile @a[tag=mg.flw] ~ ~ ~ 2 0.7
playsound minecraft:entity.strider.death hostile @a[tag=mg.flw] ~ ~ ~ 3 2
playsound minecraft:entity.enderman.hurt hostile @a[tag=mg.flw] ~ ~ ~ 3 0.1
execute unless score boss:ed BossHealth matches 0 run setblock -10061 95 -374 stone

execute if score boss:ed BossHealth matches 6 run bossbar set boss:ed value 6
execute if score boss:ed BossHealth matches 5 run bossbar set boss:ed value 5
execute if score boss:ed BossHealth matches 4 run bossbar set boss:ed value 4
execute if score boss:ed BossHealth matches 3 run bossbar set boss:ed value 3
execute if score boss:ed BossHealth matches 3 run bossbar set boss:ed color yellow
execute if score boss:ed BossHealth matches 2 run bossbar set boss:ed value 2
execute if score boss:ed BossHealth matches 1 run bossbar set boss:ed value 1
execute if score boss:ed BossHealth matches 1 run bossbar set boss:ed color red
execute if score boss:ed BossHealth matches 0 run bossbar set boss:ed value 0


execute if score boss:ed BossHealth matches 6 positioned -10058 116 -341 as @a[gamemode=!spectator,tag=mg.flw] run function summon:magmount
#execute if score boss:ed BossHealth matches 6 positioned -10058 116 -369 run function summon:magmount

#execute if score boss:ed BossHealth matches 5 positioned -10058 116 -341 run function summon:molten_imp
execute if score boss:ed BossHealth matches 5 positioned -10058 116 -369 as @a[gamemode=!spectator,tag=mg.flw] run function summon:molten_imp

execute if score boss:ed BossHealth matches 4 positioned -10058 116 -341 as @a[gamemode=!spectator,tag=mg.flw] run function summon:rust_knight
#execute if score boss:ed BossHealth matches 4 positioned -10058 116 -369 run function summon:rust_knight

#execute if score boss:ed BossHealth matches 3 positioned -10058 116 -341 run function summon:magmount
execute if score boss:ed BossHealth matches 3 positioned -10058 116 -369 as @a[gamemode=!spectator,tag=mg.flw] run function summon:magmount

execute if score boss:ed BossHealth matches 2 positioned -10058 116 -341 as @a[gamemode=!spectator,tag=mg.flw] run function summon:molten_imp
#execute if score boss:ed BossHealth matches 2 positioned -10058 116 -369 run function summon:molten_imp

function boss:4/melt
kill @e[tag=boss_ed_fella,distance=0..]


setblock -10053 95 -349 air
