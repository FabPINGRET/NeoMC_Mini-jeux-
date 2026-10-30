# Un caractère de nrest : traduit par la table nc.map (absent = retiré), ajouté à nout
execute store result score #nl mg.st run data get storage mg:tel nrest
execute if score #nl mg.st matches 0 run return 0
data modify storage mg:tel nc.c set string storage mg:tel nrest 0 1
data modify storage mg:tel nrest set string storage mg:tel nrest 1
data modify storage mg:tel nc.m set value ""
function mg:tel/norm_ch with storage mg:tel nc
data modify storage mg:tel nc.o set from storage mg:tel nout
function mg:tel/norm_cat with storage mg:tel nc
function mg:tel/norm_step
