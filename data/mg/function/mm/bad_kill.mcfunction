# @s (pas le tueur) a tué un innocent : il est éliminé aussi
tellraw @s [{"text":"🔪 Tu as tué un innocent… et tu le paies de ta vie !","color":"red"}]
execute if items entity @s container.* minecraft:bow run function mg:mm/drop_here
clear @s
effect clear @s minecraft:glowing
function mg:core/eliminate
