# Pile de pièces (+5) en $(x) $(z) ; si le point est dans un pilier, rien cette fois
$execute unless block $(x) 43 $(z) minecraft:air run return 0
$summon minecraft:item $(x).5 43.2 $(z).5 {Tags:["mg.keep","mg.pvpcoin"],PickupDelay:10s,Age:-32768s,Item:{id:"minecraft:gold_nugget",count:5,components:{"minecraft:custom_data":{pvpc_coin:1b},"minecraft:custom_name":{"text":"Pièces","color":"gold","italic":false}}}}
$particle minecraft:wax_on $(x).5 43.6 $(z).5 0.3 0.3 0.3 0 12
