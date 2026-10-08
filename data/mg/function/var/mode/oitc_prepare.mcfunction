# One in the Chamber sur une autre carte ($ar) — appelé par oitc/prepare. Généré.
kill @e[distance=0..,type=minecraft:arrow]
function mg:var/arena/setup
function mg:var/arena/ceil
scoreboard players reset @a mg.pk
scoreboard players set @a[tag=mg.play] mg.lv 3
scoreboard players set @a[tag=mg.play] mg.ok 0
scoreboard players set @a[tag=mg.play] mg.cd 0
