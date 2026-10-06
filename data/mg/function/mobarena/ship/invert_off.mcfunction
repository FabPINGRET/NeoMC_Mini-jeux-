effect clear @a[tag=mg.play] minecraft:levitation
effect give @a[tag=mg.play] minecraft:slow_falling 10 0 true
execute as @a at @s run playsound minecraft:block.beacon.activate master @s ~ ~ ~ 1 1
