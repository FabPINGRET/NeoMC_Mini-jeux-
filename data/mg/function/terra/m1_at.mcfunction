# @s : caisse larguée en $(x) $(y) $(z)
scoreboard players operation $own mg.st = @s mg.tvpid
$execute in mg:terranova positioned $(x) $(y) $(z) run function mg:terra/crate_new
scoreboard players set @s mg.tvm 1
scoreboard players set @s mg.tvmp 0
$function mg:terra/loc {x:$(x),y:$(y),z:$(z)}
tellraw @s [{"text":"📦 Mission : ","color":"yellow","bold":true},{"text":"une caisse de matériel a été larguée dans la jungle. Suis le 📡, ramasse-la (accroupi 3 s) et rapporte-la à la colonie. ","color":"gray"},{"text":"+150 ₵","color":"green"}]
playsound minecraft:block.note_block.bell player @s ~ ~ ~ 0.8 1.2
