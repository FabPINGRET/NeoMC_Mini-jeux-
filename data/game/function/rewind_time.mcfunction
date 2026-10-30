function boss:final/init

tp @a[tag=mg.flw] 152 58 -12 -90 0
particle minecraft:enchant 152 59.5 -12 0.3 0.3 0.3 0 300 normal

spawnpoint @a[tag=mg.flw] 152 58 -12
scoreboard players set $flsp mg.st 26

function music:end

#Important Scores
scoreboard players set @a[tag=mg.flw] grow_timer -1
scoreboard players set @a[tag=mg.flw] shrink_timer -1
scoreboard players set @a[tag=mg.flw] SoundtrackOverride 0

