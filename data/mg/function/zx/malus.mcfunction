# Avancement mg:zmhurt : @s touché par un mob du mode Zombies → 8 % de chances d'un malus court
advancement revoke @s only mg:zmhurt
execute unless score $state mg.st matches 2 run return 0
execute unless entity @s[tag=mg.play,tag=!mg.zdead] run return 0
execute store result score #zml mg.st run random value 1..100
execute if score #zml mg.st matches 9.. run return 0
execute store result score #zml mg.st run random value 1..4
execute if score #zml mg.st matches 1 run effect give @s minecraft:slowness 1 2 true
execute if score #zml mg.st matches 1 run title @s actionbar {"text":"🐌 Jambe mordue : ralenti 1 s","color":"red"}
execute if score #zml mg.st matches 2 run effect give @s minecraft:blindness 2 0 true
execute if score #zml mg.st matches 2 run title @s actionbar {"text":"🩸 Du sang dans les yeux : aveuglé 2 s","color":"red"}
execute if score #zml mg.st matches 3 run effect give @s minecraft:nausea 4 0 true
execute if score #zml mg.st matches 3 run title @s actionbar {"text":"🤢 Infecté : nausée 4 s","color":"red"}
execute if score #zml mg.st matches 4 run effect give @s minecraft:weakness 3 0 true
execute if score #zml mg.st matches 4 run title @s actionbar {"text":"💢 Bras mordu : faiblesse 3 s","color":"red"}
playsound minecraft:entity.zombie.infect player @s ~ ~ ~ 0.8 1.2
