tag @s add mg.mpmenu
tellraw @s [{"text":"\n🏆 CLASSEMENT (tour ","color":"gold","bold":true},{"score":{"name":"$mpround","objective":"mg.st"},"color":"white"},{"text":"/","color":"gold"},{"score":{"name":"$mpmax","objective":"mg.st"},"color":"white"},{"text":")","color":"gold"}]
execute as @a[tag=mg.mpp] run tellraw @a[tag=mg.mpmenu] [{"text":"  ","color":"gray"},{"selector":"@s","color":"white"},{"text":" : ★ ","color":"yellow"},{"score":{"name":"@s","objective":"mg.mpk"},"color":"yellow"},{"text":"   ● ","color":"gold"},{"score":{"name":"@s","objective":"mg.mpm"},"color":"gold"}]
tag @s remove mg.mpmenu
