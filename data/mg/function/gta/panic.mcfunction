# @s vient de tirer : les passants proches paniquent (husk invisible et immobile une seconde, ils le fuient)
execute if entity @e[type=minecraft:husk,tag=mg.gpanic,distance=..10] run return 0
summon minecraft:husk ~ ~ ~ {Tags:["mg.gta","mg.npc","mg.gpanic"],NoAI:1b,Silent:1b,Invulnerable:1b,PersistenceRequired:1b,active_effects:[{id:"minecraft:invisibility",duration:-1,amplifier:0,show_particles:0b}],attributes:[{id:"minecraft:scale",base:0.2}]}
scoreboard players set @e[type=minecraft:husk,tag=mg.gpanic,distance=..1] mg.gtw8 30
