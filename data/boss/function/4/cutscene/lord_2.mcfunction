playsound minecraft:entity.ravager.stunned neutral @a[tag=mg.flw] -10058 117 -355 3 1.4
tellraw @a[tag=mg.flw] [{"text":"<"},{"text":"Lord of Flame","color":"red"},{"text":"> FREE!","color":"white"},{"text":" ⇒","color":"light_purple"}]
summon armor_stand -10058 117 -355 {CustomNameVisible:1b,NoGravity:1b,Invulnerable:1b,HasVisualFire:1b,ShowArms:1b,NoBasePlate:1b,PersistenceRequired:1b,Tags:["lord_of_flame"],DisabledSlots:4144959,equipment:{feet:{id:"minecraft:leather_boots",count:1,components:{"minecraft:dyed_color":3158064,"minecraft:trim":{material:"minecraft:redstone",pattern:"minecraft:wild"}}},legs:{id:"minecraft:leather_leggings",count:1,components:{"minecraft:dyed_color":3158064,"minecraft:trim":{material:"minecraft:redstone",pattern:"minecraft:wild"}}},chest:{id:"minecraft:leather_chestplate",count:1,components:{"minecraft:dyed_color":3158064,"minecraft:trim":{material:"minecraft:redstone",pattern:"minecraft:wild"}}},head:{id:"minecraft:player_head",count:1,components:{"minecraft:profile":{id:[I;22323392,542788032,-1408984113,2046171730],properties:[{name:"textures",value:"eyJ0ZXh0dXJlcyI6eyJTS0lOIjp7InVybCI6Imh0dHA6Ly90ZXh0dXJlcy5taW5lY3JhZnQubmV0L3RleHR1cmUvMTQ2NDAwYTAxMWUxMDAxMjljZjA4ZTZkYTM4NzBmNzgzOTBmZTgyNGFjNzM4NTQ1MzgzZWZlN2I2ZjEzOTFmMiJ9fX0="}]}}}},CustomName:{"color":"red","text":"Lord of Flame"}}
particle lava -10058 121 -355 0.5 5 0.5 0 400
playsound minecraft:entity.lightning_bolt.impact master @a[tag=mg.flw] -10058 117 -355 3 0.5
playsound minecraft:block.respawn_anchor.set_spawn master @a[tag=mg.flw] -10058 117 -355 3 2

# Every 5 full repeaters is 2 seconds. Every 1 repeater tick is 0.1 seconds
schedule function floaty:sched/boss/4/cutscene/lord_3 4s
