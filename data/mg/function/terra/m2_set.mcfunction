scoreboard players set @s mg.tvm 2
$scoreboard players set @s mg.tvmo $(k)
scoreboard players set @s mg.tvmp 0
$function mg:terra/loc {x:$(x),y:$(y),z:$(z)}
$tellraw @s [{"text":"🛡 Mission : ","color":"aqua","bold":true},{"text":"l'outpost $(n) va être attaqué. Rejoins-le (📡) : la défense commence à ton arrivée près du générateur. Tiens 90 s ! ","color":"gray"},{"text":"+250 ₵","color":"green"}]
playsound minecraft:block.note_block.bell player @s ~ ~ ~ 0.8 1.2
