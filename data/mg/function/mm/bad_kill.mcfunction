# @s (pas le tueur) a tué un innocent : il est éliminé aussi
tellraw @a[tag=mg.mmx] [{"text":"🔪 ","color":"red"},{"selector":"@s","color":"yellow"},{"text":" a tué un innocent… et le paie de sa vie !","color":"gray"}]
execute if items entity @s container.* minecraft:bow run function mg:mm/drop_here
clear @s
effect clear @s minecraft:glowing
function mg:core/eliminate
