# Échéance : prochain essai dans 45-60 s par défaut ; 2 packs présents = nouvel essai dans 5 s ; emplacement tiré au hasard
execute store result score $tmhc mg.st run random value 900..1200
execute store result score #tmhn mg.st if entity @e[type=minecraft:item_display,tag=mg.tmhk]
execute if score #tmhn mg.st matches 2.. run return run scoreboard players set $tmhc mg.st 100
execute if score $tma mg.st matches 1 store result score #tmhs mg.st run random value 0..6
execute if score $tma mg.st matches 2 store result score #tmhs mg.st run random value 0..5
execute if score $tma mg.st matches 3 store result score #tmhs mg.st run random value 0..5
execute if score $tma mg.st matches 1 if score #tmhs mg.st matches 0 positioned 0.5 89 40000.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 1 if score #tmhs mg.st matches 1 positioned 5.5 73 39992.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 1 if score #tmhs mg.st matches 2 positioned -4.5 73 40008.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 1 if score #tmhs mg.st matches 3 positioned 10.5 73 39980.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 1 if score #tmhs mg.st matches 4 positioned -9.5 73 40020.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 1 if score #tmhs mg.st matches 5 positioned 15.5 89 39960.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 1 if score #tmhs mg.st matches 6 positioned -14.5 89 40040.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 2 if score #tmhs mg.st matches 0 positioned 0.5 81 40357.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 2 if score #tmhs mg.st matches 1 positioned 0.5 81 40443.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 2 if score #tmhs mg.st matches 2 positioned -9.5 81 40371.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 2 if score #tmhs mg.st matches 3 positioned 10.5 81 40429.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 2 if score #tmhs mg.st matches 4 positioned 0.5 81 40394.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 2 if score #tmhs mg.st matches 5 positioned 0.5 81 40406.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 3 if score #tmhs mg.st matches 0 positioned 0.5 81 40780.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 3 if score #tmhs mg.st matches 1 positioned 0.5 81 40820.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 3 if score #tmhs mg.st matches 2 positioned -9.5 81 40760.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 3 if score #tmhs mg.st matches 3 positioned 10.5 81 40840.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 3 if score #tmhs mg.st matches 4 positioned 0.5 81 40792.5 run function mg:tdm/pack_new
execute if score $tma mg.st matches 3 if score #tmhs mg.st matches 5 positioned 0.5 81 40808.5 run function mg:tdm/pack_new
