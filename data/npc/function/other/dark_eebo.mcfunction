execute positioned -11532 187 -183 run playsound minecraft:entity.strider.ambient neutral @a[tag=mg.flw] ~ ~ ~ 1 2

execute positioned -11538 187 -183 unless entity @a[distance=7..,gamemode=!spectator,tag=mg.flw] if entity @a[distance=..7,gamemode=!spectator,tag=mg.flw] positioned -11532 187 -183 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dark Eebo","color":"blue"},{"text":"> Why, why does Eebo hate me, why? My own brother and now YOU! You hate me too!","color":"white"},{"text":" ⇒","color":"light_purple"}]
execute positioned -11538 187 -183 unless entity @a[distance=7..,gamemode=!spectator,tag=mg.flw] if entity @a[distance=..7,gamemode=!spectator,tag=mg.flw] run setblock -11552 173 -169 redstone_block
execute positioned -11538 187 -183 unless entity @a[distance=7..,gamemode=!spectator,tag=mg.flw] if entity @a[distance=..7,gamemode=!spectator,tag=mg.flw] positioned -11532 187 -183 run kill @n[tag=boss_marker,distance=..3]

execute positioned -11538 187 -183 if entity @a[distance=7..,gamemode=!spectator,tag=mg.flw] positioned -11532 187 -183 run tellraw @a[distance=..10,tag=mg.flw] [{"text":"<"},{"text":"Dark Eebo","color":"blue"},{"text":"> I'm in a bad mood, I don't want to talk until everybody is here.","color":"white"}]


#execute if score quest_name Story matches 0
#execute if score mainstory story >= 0 Value 
