# Macro : caractère $(c) → nc.m (guillemet ou antislash : la macro échoue, le caractère est retiré)
$data modify storage mg:tel nc.m set from storage mg:tel $(map)."$(c)"
