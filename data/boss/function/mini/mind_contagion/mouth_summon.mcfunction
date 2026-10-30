summon armor_stand -11760 177 -207.5 {Invisible:1b,PersistenceRequired:1b,Tags:["mind_boss_mouth"],attributes:[{id:"minecraft:scale",base:3}],Pose:{Head:[70f,0f,0f]},DisabledSlots:4144959,equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{"properties":[{"name":"textures","value":"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYmEwNzc5OGE4ODEzNTE3Njg0MjBlYjY3N2I5MzRjOWMwNWVhNmJmZjIwZWIyMWI1NDA5Y2E5OWYzZTNhZGU4MiJ9fX0="}]}}}}}

summon armor_stand -11760 169 -196 {NoGravity:1b,Silent:1b,Invulnerable:1b,Tags:["mind_boss_mouth_pivot"],DisabledSlots:4144959,Rotation:[180F,0F]}

execute as @n[tag=mind_boss_mouth,distance=0..] at @s positioned ~ ~5 ~ run particle dust{color:[0.000,0.145,0.149],scale:3} ~ ~ ~ 1 1 1 0 100

setblock -11739 147 -177 minecraft:redstone_block

setblock -11739 147 -183 stone
fill -11743 147 -186 -11741 147 -186 stone
setblock -11741 147 -177 minecraft:redstone_block

scoreboard players set boss_mind_mouth_angle Value 0
