# Chaque tick (@s = mg.lgear) : équipement retiré dès qu'il quitte le spawn ou s'occupe ailleurs ; protégé en vol plané
execute unless function mg:elytra/gear_keep run return run function mg:elytra/free_stop
execute if predicate mg:gliding run effect give @s minecraft:resistance 2 4 true
