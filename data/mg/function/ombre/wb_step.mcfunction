# Construction : 220 commandes par tick, dans la région chargée
execute unless data storage mg:ombre q[0] run function mg:ombre/b/next
execute if score $olb mg.st matches 153.. run return run function mg:ombre/wb_done
execute unless score $olrl mg.st = $olrr mg.st in mg:ombrelune run function mg:ombre/b/switch
execute in mg:ombrelune unless function mg:ombre/b/ready run return run schedule function mg:ombre/wb_step 2t
scoreboard players set $olk mg.st 220
execute in mg:ombrelune run function mg:ombre/b/run
schedule function mg:ombre/wb_step 1t
