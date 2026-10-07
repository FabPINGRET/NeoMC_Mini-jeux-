data modify storage mg:survie g set value {d:"mg:survie",ya:0f,pi:0f}
$data modify storage mg:survie g.x set from storage mg:survie p.k$(id).home[0]
$data modify storage mg:survie g.y set from storage mg:survie p.k$(id).home[1]
$data modify storage mg:survie g.z set from storage mg:survie p.k$(id).home[2]
function mg:survie/goto with storage mg:survie g
$function mg:survie/resp_home {id:$(id)}
