# GO ! (état 1 → 2)
scoreboard players set $state mg.st 2
effect clear @a[tag=mg.play] minecraft:slowness
effect clear @a[tag=mg.play] minecraft:resistance

title @a[tag=mg.play] title [{"text":"GO !","color":"green","bold":true}]
execute as @a at @s run playsound minecraft:event.raid.horn master @s ~ ~ ~ 0.7 1.4

execute if score $game mg.st matches 1 run function mg:spleef/go
execute if score $game mg.st matches 2 run function mg:tntrun/go
execute if score $game mg.st matches 3 run function mg:pvp/go
execute if score $game mg.st matches 4 run function mg:bedwars/go
execute if score $game mg.st matches 5 run function mg:sheepwar/go
execute if score $game mg.st matches 7 run function mg:sheepwar/go
execute if score $game mg.st matches 6 run function mg:mobarena/go
execute if score $game mg.st matches 20 run function mg:splegg/go
execute if score $game mg.st matches 22 run function mg:sumo/go
execute if score $game mg.st matches 23 run function mg:dropper/go
execute if score $game mg.st matches 26 run function mg:oitc/go
execute if score $game mg.st matches 27 run function mg:tnttag/go
execute if score $game mg.st matches 28 run function mg:blockparty/go
execute if score $game mg.st matches 29 run function mg:anvil/go
execute if score $game mg.st matches 30 run function mg:turf/go
execute if score $game mg.st matches 31 run function mg:quake/go
execute if score $game mg.st matches 36 run function mg:paintball/go
execute if score $game mg.st matches 56 run function mg:icerace/go
execute if score $game mg.st matches 57..58 run function mg:bb/go
execute if score $game mg.st matches 59 run function mg:party/go
