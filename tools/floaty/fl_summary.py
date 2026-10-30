"""Affichage du bilan de gen_floaty.py (aucune logique : des lignes de texte à partir des compteurs de generate / wire).

    fl_summary.show(st, n, spawn, roots, missing, cu, terrain)       # terrain : nombre de cibles schedule du terrain (terrain_sched.txt)
"""
import fl_rewrite as R


def show(st, n, spawn, roots, missing, cu, terrain=0):
    print(f'spawn de la carte : {spawn} ; fichiers : {n["mcfunction"]} .mcfunction + {n["json"]} .json')
    print(f'chemins invalides écartés (majuscule / espace / espace de noms) : {len(st.invalid)}', st.invalid[:3])
    print(f'lignes lues {st.lines} ; retirées ({R.AUTHOR} hors chaînes) {st.dropped} ; LastOutput retirés {st.last_output} ; '
          f'setdisplay retirées {st.setdisplay} ; say -> tellraw {st.says}')
    print(f'revoke everything {st.revokes} -> {len(roots)} racines {roots} ; advancements announce_to_chat forcé : {st.announce}')
    print(f'advancements : critères modifiés (condition dimension) {st.criteria} sur {st.criteria_total} (les minecraft:impossible ne le sont pas)')
    s = n['state']
    print(f'install : {s["objectives"]} objectifs, {s["teams"]} équipes, {s["scores"]} scores, {s["bossbars"]} bossbars, {s["storage"]} storage ; '
          f'écartés : scores de vrais joueurs {s["scores_players"]} {n["players"]}, UUID {s["scores_uuid"]}, '
          f'inutilisables {s["scores_invalid"]}, objectifs {s["objectives_invalid"]}, équipes {s["teams_invalid"]}, '
          f'bossbars {s["bossbars_invalid"]}, storage {s["storage_skipped"]} ; options refusées : équipes / rendertype {s["options_invalid"]}, '
          f'bossbars {s["bossbar_props_invalid"]}')
    print(f'schedules de la carte : {s["sched_events"]} en attente, {s["sched_installed"]} reproduits dans install, '
          f'sans trampoline {s["sched_missing"]} {n["sched_missing"]}, rappels qui ne sont pas une fonction {s["sched_other"]}')
    print(f'sélecteurs : joueurs +tag {st.sel_player} (dont JSON "selector" : {st.sel_json}), entités +distance {st.sel_entity}')
    print(f'rattrapage : {cu["spawn_sites"]} sites spawnpoint -> {cu["checkpoints"]} points de contrôle distincts ; {cu["grant_sites"]} advancement grant '
          f'-> {cu["advancements"]} avancements suivis ; non suivis (préfixe store) {cu["skipped"]}, autres formes {cu["other"]} {st.catchup.other[:3]}')
    print(f'blocs de commande (Command:) réécrits : {st.blocks}')
    print(f'schedule : {len(st.sched)} fonctions distinctes (trampolines, dont {terrain} cibles des commandes du terrain), absentes de la carte : {missing}')
    print(f'fall_damage -> attribut : {st.falls} ; time query gardés (lecture seule) : {st.times} ; gamerule advance_time / random_tick_speed '
          f'+ time set|add RETIRÉS (état global du serveur) : {st.neutral} ; dimension overworld -> mg:floaty : {st.dims}')
    print('gamerule distincts :')
    for g, c in sorted(st.gamerules.items()):
        print(f'  {c:3d}  {g}')
    print(f'@x entre guillemets laissés tels quels : {st.str_skipped}')
    for l in st.str_examples:
        print('   ', l)
    why = {}
    for w, l in st.unsafe:
        why.setdefault(w, []).append(l)
    print(f'avertissements : {len(st.unsafe)}')
    for w, ls in sorted(why.items()):
        print(f'  [{w}] x{len(ls)} ex. : {ls[0][:140]}')
