tag @r[gamemode=!spectator,tag=bossroom,tag=mg.flw] add ck_fireball_target
particle minecraft:explosion -10151 155.5 -31 0 0 0 0 1 force
particle minecraft:lava -10151 155.5 -31 0.1 0.1 0.1 0.5 100 force
summon armor_stand -10151 154 -31 {CustomNameVisible:0b,NoGravity:1b,Invulnerable:1b,Invisible:1b,PersistenceRequired:1b,Tags:["ck_fireball"],DisabledSlots:4144959,equipment:{head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvYjdkNTdiNWJjOWFiM2Y1M2VjOWNjMmY5NGI3MmMxMzRhY2RlODU1YTY0M2MyNWU1YTI2YzNlMGIyYTYwM2FkZCJ9fX0="}]}}}},CustomName:"Krakenfire"}

playsound minecraft:entity.llama.spit hostile @a[tag=mg.flw] -10152 155 -31 3 0.5
playsound minecraft:entity.blaze.shoot hostile @a[tag=mg.flw] -10152 155 -31 3 0.8
