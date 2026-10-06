# GO : fin du survol, premier tour
execute as @a[tag=mg.mpview] run function mg:party/view_end
scoreboard players set $mpt mg.st 1
scoreboard players set $mph mg.st 0
scoreboard players set $mpu mg.st 0
function mg:party/round_title
function mg:party/bar_update
