# La Cathédrale Maudite — tick
# Nuées de chauves-souris : elles foncent sur le joueur le plus proche et infligent Wither au contact
execute as @e[type=minecraft:bat,tag=mg.swarm] at @s facing entity @p[tag=mg.play] eyes run tp @s ^ ^ ^0.3
execute as @e[type=minecraft:bat,tag=mg.swarm] at @s if entity @a[tag=mg.play,distance=..1.8] run effect give @a[tag=mg.play,distance=..1.8] minecraft:wither 4 1 true
execute if entity @e[tag=mg.boss] run function mg:mobarena/cathedral/boss_tick
