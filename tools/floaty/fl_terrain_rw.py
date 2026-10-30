"""Réécriture des commandes du terrain de « Scourge of the Floaty Isles » dans les chunks des fichiers region (.mca), au build.

    run = fl_terrain_rw.Pass(rewrite=True, dim='minecraft:overworld')
    nouveaux_octets = run.file('region/r.0.0.mca', octets)       # scan ET réécriture en une passe ; autre fichier : octets inchangés
    run.stats, run.pending, run.finds, run.after                  # voir Pass ; run.rewritten(), run.sched_targets(), run.effects()

Par chunk qui passe le pré-filtre (fl_terrain.prefilter) : fl_nbt.loads_spans (l'arbre + la position de chaque chaîne), emplacement des
commandes (blocs de commande et minecarts : `Command` ; panneaux : `click_event.command` NBT, ou `clickEvent.value` dans une chaîne
JSON, ré-encodée en JSON compact et ASCII pur : un caractère hors BMP y devient un échappement Unicode), fl_terrain_cmd.rewrite_command
par commande, puis remplacement des chaînes (préfixe u16 + MUTF-8 : fl_nbt.encode_str, comme Java ; une source en MUTF-8 valide, paires
de substitution ou NUL en C0 80, est donc réécrite normalement) du plus loin au plus près : le NBT ne porte aucune longueur d'octets
imbriquée, tout le reste est recopié tel quel. Un chunk est LAISSÉ (commandes en 'laisse', raison) si : une chaîne source n'est pas du
MUTF-8 strict ('mutf8', défensif : fl_nbt.loads refuse déjà un tel chunk, que fl_terrain compte alors « illisible ») ; le chunk réécrit
dépasserait 255 secteurs ('taille') ; l'arbre d'origine avec les chaînes substituées n'égale pas le NBT relu des nouveaux octets, un
NaN valant un NaN ('verif'). Une commande de
plus de 32767 caractères ('trop_long') ou dont la chaîne dépasse 65535 octets ('chaine') est laissée seule. Le chunk réécrit est
recompressé en zlib, niveau 6 (fl_mca.record). Seuls les fichiers dont un chunk a changé sont reconstruits (fl_mca.rebuild) ; un en-tête
corrompu laisse le fichier entier ('en_tete'). Une reconstruction qui ne se relit pas comme prévu (fl_mca.check) lève VerifyError.
"""
import json
from collections import Counter, namedtuple

import fl_mca
import fl_nbt
import fl_signs
import fl_terrain
import fl_terrain_cmd as C

MAX_CMD = 32767                                  # longueur maximale d'une commande de bloc de commande
Change = namedtuple('Change', 'found new action reason')     # new : texte final de la commande (celui de found si rien n'a changé)
_SAME = (None, 'inchange', None)


def _equal(a, b):
    """a == b, sauf qu'un NaN égale un NaN (un flottant NaN du chunk, recopié tel quel, ne doit pas faire échouer la vérification)."""
    if a == b:
        return True
    if isinstance(a, float) and isinstance(b, float):
        return a != a and b != b
    if isinstance(a, dict) and isinstance(b, dict):
        return a.keys() == b.keys() and all(_equal(v, b[k]) for k, v in a.items())
    if isinstance(a, list) and isinstance(b, list):
        return len(a) == len(b) and all(_equal(x, y) for x, y in zip(a, b))
    return False


def _revert(res, reason):
    for k, (_, action, _) in res.items():
        if action in ('reecrit', 'noop'):
            res[k] = (None, 'laisse', reason)


def _plan(root, finds, ctx):
    """-> (edits [(conteneur, clé, nouvelle chaîne, [clés de res])], res {(pos, type, commande): (nouvelle, action, raison)}). Ne modifie
    pas l'arbre du chunk (les événements des panneaux JSON sont dans des copies décodées)."""
    edits, res = [], {}

    def decide(pos, kind, cmd):
        new, action, reason = C.rewrite_command(cmd, ctx)
        if new is not None and len(new) > MAX_CMD:
            new, action, reason = None, 'laisse', 'trop_long'
        res[(pos, kind, cmd)] = (new, action, reason)
        return new, (pos, kind, cmd)

    for f in finds:
        if f.ref is not None and isinstance(f.ref[0].get(f.ref[1]), str):
            new, k = decide(f.pos, f.kind, f.command)
            if new is not None:
                edits.append((f.ref[0], f.ref[1], new, [k]))
    for be in fl_terrain._tile_entities(fl_terrain._content(root)):
        kind = fl_signs.kind_of(be)
        for label, msg, box, key, _ in fl_signs.sign_slots(be, kind) if kind in fl_signs.SIGN_IDS else ():
            obj, events = fl_signs.message_events(msg)
            if not events or (isinstance(msg, str) and obj is None) or not isinstance(box, (dict, list)):
                continue
            keys = []
            for ev, field in events:
                new, k = decide(fl_terrain._pos(be), label, ev[field])
                if new is None:
                    continue
                keys.append(k)
                if obj is None:
                    edits.append((ev, field, new, [k]))              # composant NBT : la chaîne de l'événement elle-même
                else:
                    ev[field] = new
            if keys and obj is not None:
                edits.append((box, key, json.dumps(obj, separators=(',', ':'), ensure_ascii=True), keys))      # ASCII pur : aucun octet multi-octets
    return edits, res


def rewrite_chunk(raw, root, spans, finds, ctx):
    """NBT brut d'un chunk, son arbre et ses spans (fl_nbt.loads_spans), ses [Found] (fl_terrain.scan_chunk), ctx (fl_terrain_cmd.Ctx) ->
    (nouveau NBT brut ou None, res) ; res = {(pos, type, commande): (nouvelle, action, raison)} des commandes qui changent ou sont laissées.
    None : rien à changer, ou chunk laissé (res le dit)."""
    edits, res = _plan(root, finds, ctx)
    todo, seen = [], set()
    for box, key, new, keys in edits:
        span = spans.get((id(box), key))
        if span is None or (id(box), key) in seen:
            _revert(res, 'verif')
            return None, res
        try:
            fl_nbt.mutf8_decode(raw[span[0] + 2:span[1]])            # la chaîne remplacée se relit en MUTF-8 strict (déjà vrai si le chunk a été lu)
        except ValueError:
            _revert(res, 'mutf8')
            return None, res
        try:
            fl_nbt.encode_str(new)
        except ValueError:
            for k in keys:
                res[k] = (None, 'laisse', 'chaine')
            continue
        seen.add((id(box), key))
        todo.append((span, box, key, new))
    if not todo:
        return None, res
    buf = bytearray(raw)
    for span, _, _, new in sorted(todo, key=lambda t: t[0][0], reverse=True):      # du plus loin au plus près : les positions restent valables
        buf[span[0]:span[1]] = fl_nbt.encode_str(new)
    for _, box, key, new in todo:
        box[key] = new                                                # l'arbre devient celui qu'on attend du nouveau NBT
    new_raw = bytes(buf)
    if fl_mca.sectors(fl_mca.record(new_raw)) > fl_mca.MAX_SECTORS:
        _revert(res, 'taille')
        return None, res
    try:
        same = _equal(fl_nbt.loads(new_raw), root)
    except fl_terrain.READ_ERRORS:
        same = False
    if not same:
        _revert(res, 'verif')
        return None, res
    return new_raw, res


def _reverted(batch, reason):
    return [c if c.action not in ('reecrit', 'noop') else Change(c.found, c.found.command, 'laisse', reason) for c in batch]


class Pass:
    """Résultat cumulé d'un passage scan (+ réécriture) sur les fichiers du terrain.
    stats : Counter (voir fl_terrain) ; pending : {clé de A_VERIFIER: [(fichier, cx, cz)]} ; finds : [Found] AVANT réécriture ; after :
    [Change], un par Found, dans le même ordre (vide si rewrite=False) ; unread_cmd : chunks dont le pré-filtre voit une commande mais que
    fl_nbt ne lit pas (raison `illisible_cmd` du rapport : jamais fatal, leurs commandes ne sont pas réécrites ; seulement avec rewrite)."""

    def __init__(self, rewrite=True, dim=None):
        self.rewrite = rewrite
        self.stats, self.finds, self.after = Counter(), [], []
        self.pending = {k: [] for k in fl_terrain.A_VERIFIER}
        self.cmd = C.Ctx(dim)                                         # dim : dimension source de la carte (voir fl_terrain_cmd.Ctx)
        self.files = 0                                                # fichiers reconstruits
        self.unread_cmd = []                                          # (fichier, cx, cz) des chunks à commandes que le lecteur strict ne lit pas : NON réécrits

    def file(self, arc, data):
        """Octets d'un fichier du zip -> octets à écrire. region/ et entities/ (.mca) : scan + réécriture ; le reste (poi/, .mcc) : tel quel."""
        if not arc.endswith('.mca') or arc.startswith('poi/'):
            return data
        changes, batches = {}, []
        for i, raw in fl_mca.payloads(data, self.stats):
            root = spans = None
            if self.rewrite and fl_terrain.prefilter(raw):
                try:
                    root, spans = fl_nbt.loads_spans(raw)
                except fl_terrain.READ_ERRORS:
                    self.unread_cmd.append(fl_terrain.chunk_where(arc, i))     # scan_chunk relit, compte 'illisible' et rend []
            finds = fl_terrain.scan_chunk(raw, arc, i, self.stats, self.pending, root)
            if not finds:
                continue
            self.finds += finds
            res = {}
            if self.rewrite and root is not None:
                new_raw, res = rewrite_chunk(raw, root, spans, finds, self.cmd)
                if new_raw is not None:
                    changes[i] = new_raw
            if self.rewrite:
                batch = []
                for f in finds:
                    new, action, reason = res.get((f.pos, f.kind, f.command), _SAME)
                    batch.append(Change(f, f.command if new is None else new, action, reason))
                batches.append((i, batch))
        out = data
        if changes:
            try:
                out = fl_mca.rebuild(data, changes)
                fl_mca.check(data, out, changes)
                self.files += 1
            except fl_mca.McaError:
                out, batches = data, [(i, _reverted(b, 'en_tete')) for i, b in batches]
        for _, batch in batches:
            self.after += batch
        return out

    def sorted_pending(self):
        return {k: sorted(v) for k, v in self.pending.items()}

    def rewritten(self):
        """Nombre de commandes modifiées ou remplacées par NOOP."""
        return sum(1 for c in self.after if c.action in ('reecrit', 'noop'))

    def effects(self):
        """Counter des effets (tag, distance, say...) des commandes réécrites (une fois par occurrence)."""
        out = Counter()
        for c in self.after:
            if c.action == 'reecrit':
                out.update(self.cmd.fx[c.found.command])
        return out

    def sched_targets(self):
        """Fonctions planifiées (`schedule function X`) des commandes réécrites : un trampoline floaty:sched/... chacune (gen_floaty)."""
        out = set()
        for c in self.after:
            if c.action == 'reecrit':
                out |= self.cmd.sched[c.found.command]
        return sorted(out)
