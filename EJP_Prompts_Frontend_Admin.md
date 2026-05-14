# 🏗️ EJP — Prompts de Développement UI/UX
### Plateforme Numérique de l'Église des Jeunes Prodiges
> Stack : **Tailwind CSS + JavaScript vanilla** | Animations fluides | Design moderne & spirituel
> Organisation : `/frontend/` (espace membre) et `/admin/` (back office)

---

## 🎨 CHARTE GRAPHIQUE GLOBALE (à appliquer sur toutes les pages)

```
Couleurs principales :
  - Primaire    : #1E3A5F  (bleu marine profond — sérieux, confiance)
  - Accent      : #F5A623  (or/ambre — spiritualité, excellence)
  - Succès      : #27AE60  (vert — progression validée)
  - Danger      : #E74C3C  (rouge — refus, alerte)
  - Fond clair  : #F8F9FA
  - Fond sombre : #0F1B2D
  - Texte       : #1A1A2E

Typographie :
  - Titres  : Playfair Display (Google Fonts)
  - Corps   : Inter (Google Fonts)

Motif de fond : léger motif géométrique doré en filigrane (opacité 5%)
Logo EJP : initiales stylisées en or sur fond marine
```

---

# 📁 DOSSIER `/frontend/` — Espace Membre

---

## 📄 `frontend/login.html` — Page de Connexion

```
Crée une page de connexion moderne pour une application religieuse appelée "EJP" 
(Église des Jeunes Prodiges) en HTML + Tailwind CSS + JavaScript vanilla.

=== DESIGN & LAYOUT ===
- Fond plein écran en dégradé diagonal : du bleu marine #1E3A5F vers le bleu nuit #0F1B2D
- Centré verticalement et horizontalement, carte de connexion flottante avec effet glassmorphism
  (backdrop-blur, fond blanc à 10% d'opacité, bordure blanche subtile)
- Logo EJP en haut de la carte : initiales dorées (#F5A623) sur cercle marine, taille 80px
- Sous-titre : "Bienvenue dans votre espace membre" en blanc avec opacité 80%

=== FORMULAIRE ===
- Champ "Identifiant ou e-mail" avec icône 👤 en prefix
- Champ "Mot de passe" avec icône 🔒 en prefix + bouton œil pour afficher/masquer
- Case à cocher "Rester connecté"
- Lien "Mot de passe oublié ?" aligné à droite
- Bouton "Se connecter" : fond doré #F5A623, texte blanc, pleine largeur, border-radius xl

=== ANIMATIONS ===
- À l'ouverture : la carte monte de bas en haut avec opacity fade (translateY + opacity, 600ms ease-out)
- Les champs s'illuminent avec un glow doré au focus (box-shadow #F5A623 avec opacité 40%)
- Le bouton "Se connecter" fait un léger scale(1.02) au hover + shimmer effect (pseudo-élément 
  qui traverse en diagonale)
- Si login invalide : shake animation horizontale sur la carte (keyframes, 500ms)
- Indicateur de chargement spinner dans le bouton au clic

=== IMAGE À GÉNÉRER ===
Génère ou décris une image de fond optionnelle pour les grands écrans (layout 2 colonnes) :
côté gauche = illustration vectorielle d'une communauté de jeunes rassemblés, style plat moderne,
palette bleu/or, avec une citation biblique en superposition.

=== RESPONSIVE ===
- Mobile : carte occupe 90% de la largeur, padding réduit
- Desktop : carte max-w-md centrée sur fond animé

=== JAVASCRIPT ===
- Validation des champs avant soumission (champ vide = bordure rouge + message d'erreur animé)
- Toggle show/hide password
- Simulation de connexion : si identifiant = "demo" et mdp = "ejp2026" → redirect vers dashboard.html
```

---

## 📄 `frontend/dashboard.html` — Tableau de Bord Membre

```
Crée le tableau de bord personnel d'un membre de l'EJP en HTML + Tailwind CSS + JavaScript vanilla.
Le membre connecté s'appelle "Jean Kodjo", il est au statut "Star ⭐".

=== LAYOUT GLOBAL ===
- Sidebar fixe à gauche (largeur 260px) sur desktop, menu hamburger sur mobile
- Zone principale scrollable à droite
- En-tête sticky avec nom du membre, avatar et cloche de notifications

=== SIDEBAR ===
Icônes + libellés pour les liens :
  🏠 Tableau de bord (actif)
  🎓 Mes formations
  📈 Ma progression
  📅 Événements
  🔔 Notifications
  ⚙️ Mon compte
  🚪 Déconnexion

Animation : au hover sur un lien, fond doré avec texte marine, transition 200ms.
Indicateur actif : barre verticale dorée à gauche du lien actif.

=== ZONE PRINCIPALE — CONTENU ===

**Bloc 1 — Carte de bienvenue hero**
- Fond dégradé marine → bleu roi
- "Bonjour, Jean 👋" en grand (text-3xl, Playfair Display)
- Statut avec badge animé : étoile ⭐ dorée pulsante + texte "Star"
- Date d'entrée à l'EJP : "Membre depuis le 15 janvier 2026"
- Animation entrée : slide-in depuis la gauche, 500ms

**Bloc 2 — Statistiques rapides (4 cartes en grille)**
Cartes avec icône + chiffre + libellé :
  📹 7/10 vidéos complétées
  ✅ 8 sessions de service
  📅 3 mois à l'EJP
  🏆 Niveau : Star

Chaque carte : fond blanc, ombre douce, border-radius xl.
Animation : les 4 cartes apparaissent en stagger (délais de 100ms entre chaque) avec fade+scale.

**Bloc 3 — Progression formations**
- Titre "Ma progression dans les formations"
- Barre de progression animée : 70% (couleur #F5A623 qui remplit de gauche à droite, 1s ease)
- Liste des 3 derniers modules avec statut (✅ complété / 🔄 en cours / 🔒 non commencé)
- Bouton "Voir toutes mes formations →"

**Bloc 4 — Bouton Demande de Progression**
- Si conditions remplies : grand bouton gradient doré avec icône ⬆️
  "Faire une demande de progression vers Pilote"
  Au hover : glow effect doré autour du bouton
- Si conditions non remplies : bouton grisé avec tooltip explicatif

**Bloc 5 — Notifications récentes**
Liste de 3 notifications avec icône, texte et date, avec animation slide-in depuis la droite.

=== IMAGE À GÉNÉRER ===
Illustration pour la carte hero : silhouette d'une étoile stylisée en or sur fond abstrait,
style minimaliste vectoriel, pour représenter visuellement le statut "Star".

=== RESPONSIVE ===
- Mobile : sidebar en drawer (slide depuis la gauche au clic hamburger, overlay sombre derrière)
- Grille de stats : 2x2 sur mobile, 4x1 sur desktop
```

---

## 📄 `frontend/formations.html` — Page Formations

```
Crée la page "Mes Formations" de l'espace membre EJP en HTML + Tailwind CSS + JavaScript.

=== LAYOUT ===
Même sidebar que dashboard.html. Zone principale avec :

**En-tête de page**
- Titre "🎓 Mes Formations" (Playfair Display, text-3xl)
- Barre de progression globale animée en haut : "7 sur 10 formations complétées"
- Badge statut : "Formations obligatoires ✅ / Optionnelles 📚"

**Filtres**
- Boutons filtre pill : [Tous] [Obligatoires] [Optionnels] [Complétés] [Non commencés]
- Au clic : animation de transition du contenu (fade + slight scale)

**Liste des modules (accordéon)**
Exemple de structure à créer :

MODULE 1 — "Les Fondements de la Foi" 🔒 Obligatoire
  → Vidéo 1 : "Introduction à la vision de l'EJP" ✅ Vue le 20/03/2026
  → Vidéo 2 : "Les valeurs de l'église" ✅ Vue le 21/03/2026
  → Vidéo 3 : "Le parcours du disciple" 🔄 En cours

MODULE 2 — "Vie Communautaire" 🔒 Obligatoire
  → Vidéo 1 : "Comprendre le service" ⬜ Non vu
  → Vidéo 2 : "La famille des disciples" ⬜ Non vu

MODULE 3 — "Développement Personnel" 📚 Optionnel
  → ...

**Carte de chaque vidéo**
- Thumbnail YouTube simulée (placeholder avec icône ▶️)
- Titre de la vidéo
- Durée estimée
- Badge statut (Vu ✅ / En cours 🔄 / Non vu ⬜)
- Bouton "Regarder" → ouvre une modale avec l'iframe YouTube
- Si déjà vu : coche verte animée (check qui se dessine en SVG stroke animation)

**Modale vidéo**
- Overlay sombre animé (fade-in)
- Iframe YouTube responsive dans la modale
- Fermer avec ✕ ou clic en dehors
- À la fermeture : enregistrement automatique comme "vu" + animation confetti légère

=== ANIMATIONS ===
- Modules s'ouvrent en accordéon avec smooth height animation (max-height + overflow)
- Cartes vidéo : au hover, légère élévation (translateY -4px + shadow)
- Barre de progression se remplit animée au chargement de la page

=== IMAGE À GÉNÉRER ===
Icône/illustration pour chaque module thématique :
- Module 1 "Foi" → croix stylisée en or sur fond marine
- Module 2 "Communauté" → silhouettes de personnes en cercle
- Module 3 "Développement" → plante qui pousse
Style : icônes vectorielles plates, palette EJP (bleu + or).
```

---

## 📄 `frontend/progression.html` — Ma Progression

```
Crée la page "Ma Progression" de l'espace membre EJP en HTML + Tailwind CSS + JavaScript.

=== CONTENU PRINCIPAL ===

**Section 1 — Parcours visuel (Timeline verticale)**
Affiche les 5 niveaux du parcours sous forme de timeline verticale interactive :

🟢 Niveau 1 : Nouveau Membre — [COMPLÉTÉ] (date : 15/01/2026)
🌟 Niveau 2 : Star           — [ACTUEL]   (date : 10/03/2026)
✈️ Niveau 3 : Pilote         — [EN COURS] (conditions à remplir)
🏛️ Niveau 4 : Pilier         — [VERROUILLÉ]
🌍 Niveau 5 : Missionnaire   — [VERROUILLÉ]

Design de la timeline :
- Ligne verticale dorée connectant les nœuds
- Chaque nœud = cercle avec icône correspondante
- Nœuds complétés : fond doré, coche blanche
- Nœud actuel : pulsation animée (ring qui s'étend et disparaît en loop)
- Nœuds futurs : fond gris, icône verrou
- Clic sur un nœud : ouvre un panneau latéral avec les détails/conditions

**Section 2 — Conditions pour progresser vers Pilote**
Card blanche avec :
- Titre "Pour devenir Pilote ✈️"
- Liste des conditions avec indicateurs visuels :
  ✅ Formation initiale complétée
  🔄 Sessions de service : 8/12 (barre de progression animée)
  ⬜ Demande validée par le Chef
- Bouton "Faire ma demande" (actif seulement si toutes les conditions = ✅)

**Section 3 — Historique des statuts**
Tableau chronologique :
  15/01/2026 → Nouveau Membre
  10/03/2026 → Star (validé par Chef Amos)

**Section 4 — Sessions de service**
- Compteur animé : "8 sessions enregistrées"
- Liste des sessions avec date et description
- Graphique bar simple (Canvas ou SVG) montrant la fréquence mensuelle

=== ANIMATIONS ===
- Timeline : chaque nœud s'anime en séquence au scroll (Intersection Observer)
- Compteur sessions : compte de 0 à 8 animé (requestAnimationFrame)
- Anneau pulsant sur le nœud actuel : @keyframes pulse-ring en CSS pur

=== IMAGE À GÉNÉRER ===
Illustration hero pour cette page : une route/chemin qui monte, avec des étapes symbolisées
par les 5 icônes (étoile, avion, pilier, globe), style vectoriel plat, couleurs EJP.
```

---

## 📄 `frontend/evenements.html` — Événements

```
Crée la page "Événements" de l'espace membre EJP en HTML + Tailwind CSS + JavaScript.

=== SECTION HERO ===
- Grand bandeau avec fond dégradé marine
- Titre "📅 Événements de l'EJP"
- Sous-titre "Ne manquez aucun rassemblement"

=== ÉVÉNEMENTS À VENIR — SECTION PRINCIPALE ===
Grille de cartes événements (3 colonnes desktop, 1 colonne mobile) :

**Carte événement :**
- Image/affiche de l'événement en haut (aspect ratio 16:9, object-cover)
  → placeholder : dégradé coloré avec titre en overlay si pas d'image
- Badge "À venir" ou "Aujourd'hui !" ou "Passé" (couleurs différentes)
- Nom de l'événement (text-xl, Playfair Display)
- Date et heure avec icône 📅
- Lieu avec icône 📍
- Extrait de description (2 lignes max, truncate)
- Bouton "En savoir plus" → ouvre modale de détail

**Modale détail événement :**
- Image plein format en haut
- Toutes les infos
- Bouton de partage (copier le lien)
- Animation : slide-up depuis le bas

=== SECTION ARCHIVES ===
- Liste compacte des événements passés (format tableau simplifié)
- Filtre par mois/année

=== ANIMATIONS ===
- Cartes : apparition en stagger au scroll (Intersection Observer)
- Hover sur carte : légère élévation + zoom subtil de l'image (scale 1.05, overflow hidden)
- Badge "Aujourd'hui !" : clignotement doux

=== IMAGE À GÉNÉRER ===
3 affiches événement placeholder en style EJP pour les cartes :
1. "Culte de Pentecôte 2026" — fond marine avec flammes stylisées dorées
2. "Retraite Spirituelle" — fond vert foncé avec montagnes au coucher de soleil
3. "Soirée de Louange" — fond nuit avec étoiles et notes de musique dorées
Style : affiche de type flyer moderne, typographie Playfair Display, logo EJP en bas.
```

---

## 📄 `frontend/compte.html` — Mon Compte

```
Crée la page "Mon Compte" de l'espace membre EJP en HTML + Tailwind CSS + JavaScript.

=== SECTIONS ===

**Section 1 — Informations personnelles**
- Avatar centré avec bouton "Changer la photo" (hover : overlay avec icône caméra)
- Formulaire en 2 colonnes :
  Nom | Prénom
  Téléphone | E-mail
  Date d'arrivée (lecture seule)
  Chef responsable (lecture seule)
  Statut actuel (lecture seule, avec badge coloré)
- Bouton "Enregistrer les modifications" (doré)
- Animation : champs en mode lecture par défaut, au clic "Modifier" ils deviennent éditables
  (transition de background-color et border)

**Section 2 — Sécurité**
- Formulaire de changement de mot de passe :
  Ancien mot de passe
  Nouveau mot de passe (avec indicateur de force : barre colorée)
  Confirmer le nouveau mot de passe
- Bouton "Mettre à jour"

**Section 3 — Préférences de notifications**
- Toggles (switch animé) pour :
  ✅ Recevoir les rappels d'événements par e-mail
  ✅ Être notifié quand ma demande de progression est traitée
  ⬜ Recevoir la newsletter de l'EJP

=== ANIMATIONS ===
- Avatar upload : drag & drop zone avec animation de bordure pointillée dansante
- Indicateur force mot de passe : barre qui change de couleur (rouge → orange → vert) 
  en temps réel selon la complexité
- Succès enregistrement : toast notification qui slide depuis le haut avec confetti
```

---

# 📁 DOSSIER `/admin/` — Back Office Administrateur

---

## 📄 `admin/login.html` — Connexion Admin

```
Crée une page de connexion pour l'espace administrateur de l'EJP.
Design sobre et sécurisé, différent du login membre.

=== DESIGN ===
- Fond entièrement sombre : #0F1B2D
- Carte de connexion centrée, fond #1A2942, bordure subtile dorée
- Badge "🔐 Espace Administrateur" en rouge/orange en haut de la carte
- Champs : identifiant admin + mot de passe
- Bouton : fond rouge sombre #C0392B (couleur différente = accès différent)
- Mention "Accès réservé à l'administration de l'EJP" en bas, texte grisé

=== SÉCURITÉ UI ===
- Après 3 tentatives échouées : formulaire se verrouille 30 secondes (countdown affiché)
- Animation lock qui se "ferme" visuellement lors du verrouillage

=== ANIMATIONS ===
- Même logique que login.html membre mais palette rouge/sombre
- Particules de fond très subtiles (points dorés qui bougent lentement, Canvas)
```

---

## 📄 `admin/dashboard.html` — Tableau de Bord Admin

```
Crée le tableau de bord principal de l'administrateur EJP en HTML + Tailwind + JavaScript.
Vue d'ensemble complète de toute l'église.

=== SIDEBAR ADMIN ===
Liens avec icônes :
  📊 Tableau de bord
  👥 Membres
  👨‍💼 Chefs & Groupes
  🎓 Formations
  ⛪ Cultes
  📋 PV Réunions
  📅 Événements
  📬 Communications
  ⚙️ Paramètres
  🚪 Déconnexion

Style sidebar : fond #0F1B2D, texte blanc, accent doré sur l'item actif.
Logo EJP en haut de la sidebar.

=== ZONE PRINCIPALE ===

**Ligne 1 — KPI Cards (5 cartes)**
Avec compteur animé (de 0 vers la valeur, 1s) :
  👤 Total membres : 124
  ⭐ Stars : 45
  ✈️ Pilotes : 23
  🏛️ Piliers : 8
  🌍 Missionnaires : 3

Cartes : fond blanc, icône colorée, chiffre en text-3xl bold, léger shadow.
Animation stagger à l'entrée de page.

**Ligne 2 — Alertes & Actions rapides**
- Card "⏳ Demandes en attente" : badge rouge avec le nombre (ex: 7)
  Liste des 3 dernières demandes avec boutons Valider ✅ / Refuser ❌ inline
- Card "📅 Prochain événement" : mini card avec infos

**Ligne 3 — Graphiques**
- Graphique en barres : "Répartition des membres par statut" (SVG ou Canvas)
  Couleurs différentes par statut, légende, animation fill de bas en haut
- Graphique ligne : "Nouveaux membres par mois" (6 derniers mois)

**Ligne 4 — Activité récente**
- Feed chronologique des dernières actions :
  "Jean Kodjo a demandé une progression vers Pilote — il y a 2h"
  "Chef Amos a validé la demande de Marie Doe — hier"
  "Nouvel événement ajouté : Culte de Pentecôte — il y a 3 jours"
  Chaque ligne avec icône + texte + badge de temps
  Animation : slide-in depuis la droite au chargement

=== IMAGE À GÉNÉRER ===
Illustration minimaliste pour la zone d'accueil vide (premier accès) :
un tableau de bord vide avec message "Bienvenue, commencez par ajouter des membres"
style illustration plate moderne, palette EJP.
```

---

## 📄 `admin/membres.html` — Gestion des Membres

```
Crée la page de gestion des membres pour l'admin EJP en HTML + Tailwind + JavaScript.

=== EN-TÊTE ===
- Titre "👥 Gestion des Membres"
- Bouton primaire "+ Ajouter un membre" (doré, en haut à droite)
- Statistiques rapides inline : 124 membres | 12 ce mois | 7 en attente

=== BARRE DE RECHERCHE ET FILTRES ===
- Champ recherche (nom, prénom, téléphone) avec icône loupe, live filtering
- Filtres en ligne :
  [Tous les statuts ▾] [Tous les Chefs ▾] [Trier par ▾]
  Bouton "Exporter" (icône téléchargement, génère un CSV simulé)
- Animation : filtre qui "secoue" légèrement si aucun résultat trouvé

=== TABLEAU DES MEMBRES ===
Colonnes : Avatar | Nom Prénom | Statut | Chef | Date d'entrée | Sessions | Actions

- Avatar : photo de profil en cercle (initiales colorées si pas de photo)
- Statut : badge coloré avec icône (⭐ Star, ✈️ Pilote, etc.)
- Actions : icônes Voir 👁️ | Modifier ✏️ | Changer Chef 🔄

- Hover sur une ligne : fond légèrement plus clair + apparition des actions (opacity transition)
- Pagination en bas : précédent / 1 2 3 ... / suivant
- Skeleton loading : afficher des lignes grises animées (shimmer) pendant le "chargement"

=== MODALE — AJOUTER UN MEMBRE ===
Slide-in depuis la droite (drawer), fond overlay sombre :
- Photo de profil (upload ou initiales auto)
- Nom et Prénom
- Téléphone *
- E-mail
- Date d'arrivée
- Chef responsable (dropdown)
- Statut initial : Nouveau Membre (fixe)
- [Annuler] [Créer le compte]
→ À la création : toast "Compte créé ! Identifiant : ejp_jean_kodjo | MDP provisoire : EJP2026#"

=== MODALE — FICHE MEMBRE (détail) ===
Modal grande largeur (max-w-3xl), onglets :
  [ℹ️ Infos] [🎓 Formations] [📈 Progression] [📝 Notes]

Onglet Infos : toutes les données personnelles + historique des statuts (timeline mini)
Onglet Formations : liste des vidéos vues/non vues avec pourcentage
Onglet Progression : sessions de service, demandes passées
Onglet Notes : zone textarea pour notes du chef/admin + historique des notes

=== ANIMATIONS ===
- Filtrage table : fade-out/in des lignes qui disparaissent/apparaissent
- Tri colonnes : icône de tri qui pivote selon l'ordre
- Modale : slide-in + overlay fade avec cubic-bezier ease-out
```

---

## 📄 `admin/chefs.html` — Gestion des Chefs & Groupes

```
Crée la page de gestion des Chefs et Familles de Disciples en HTML + Tailwind + JavaScript.

=== LAYOUT EN 2 COLONNES ===
Colonne gauche (30%) : liste des Chefs
Colonne droite (70%) : détail du groupe du Chef sélectionné

=== COLONNE GAUCHE — LISTE DES CHEFS ===
- Chaque Chef = carte cliquable :
  Avatar | Nom du Chef | X membres sous sa responsabilité
- Bouton "+ Créer un compte Chef" en bas de la liste
- Chef sélectionné : carte surlignée avec bordure dorée

=== COLONNE DROITE — DÉTAIL DU GROUPE ===
Quand un Chef est sélectionné :
- En-tête : photo Chef, nom, date de prise de fonction
- "Famille de Disciples de [Nom Chef]" — X membres
- Table des membres du groupe avec statuts
- Bouton "Réattribuer un membre à un autre Chef" :
  → Modale de sélection avec drag & drop entre les groupes (ou simple dropdown)

=== FONCTIONNALITÉS ===
- Modale création compte Chef :
  Nom, prénom, téléphone, e-mail, photo
  → Génère identifiant chef + mdp provisoire
- Statistiques du groupe : % de progression moyen, nombre de demandes validées

=== ANIMATIONS ===
- Au clic sur un Chef : transition de la colonne droite (fade + slide depuis droite)
- Drag & drop de membres : effet de "levée" de la carte avec shadow, zone de dépôt surlignée
```

---

## 📄 `admin/formations.html` — Gestion des Formations

```
Crée la page de gestion des formations (Back Office) EJP en HTML + Tailwind + JavaScript.

=== LAYOUT EN 2 PARTIES ===

**Partie gauche — Structure des modules (30%)**
- Liste accordion des modules :
  MODULE 1 — Les Fondements (5 vidéos) ✏️ 🗑️
  MODULE 2 — Vie Communautaire (3 vidéos) ✏️ 🗑️
- Bouton "+ Créer un module" en bas
- Les modules sont réordonnables par drag & drop (poignée ⠿ à gauche)

**Partie droite — Vidéos du module sélectionné (70%)**
- Titre du module avec possibilité de renommer inline (clic → input)
- Liste des vidéos :
  Chaque vidéo = carte avec :
  - Thumbnail YouTube (iframe preview ou image)
  - Titre de la vidéo
  - Badge : 🔒 Obligatoire / 📚 Optionnel
  - Ordre d'affichage (réordonnables)
  - Statistiques : "Vu par 87/124 membres (70%)"
  - Actions : ✏️ Modifier | 🗑️ Supprimer
- Bouton "+ Ajouter une vidéo"

=== MODALE AJOUT/MODIFICATION VIDÉO ===
- Titre *
- Module (dropdown)
- Description courte
- Lien YouTube * → preview automatique de la thumbnail en temps réel
- Type : ● Obligatoire ○ Optionnel
- Ordre dans le module

=== STATISTIQUES GLOBALES ===
Bandeau en haut :
- Membres ayant 100% des formations obligatoires : 34/124
- Vidéo la plus vue : "Introduction à la vision"
- Vidéo la moins vue : "Le service avancé"

=== ANIMATIONS ===
- Drag & drop avec animation de réorganisation fluide
- Preview YouTube qui apparaît avec fade-in quand l'URL est valide
- Barre de progression par vidéo : fill animé
```

---

## 📄 `admin/demandes.html` — Validation des Demandes de Progression

```
Crée la page de gestion des demandes de progression en HTML + Tailwind + JavaScript.

=== EN-TÊTE ===
- Titre "📈 Demandes de Progression"
- Compteur badge rouge : "7 demandes en attente"
- Onglets : [En attente (7)] [Approuvées] [Refusées] [Toutes]

=== LISTE DES DEMANDES ===
Chaque demande = carte avec :
- Avatar + Nom du membre
- Demande : "Passage de Star ⭐ à Pilote ✈️" (avec flèche animée entre les deux badges)
- Chef responsable
- Date de la demande
- Depuis combien de temps en attente (badge rouge si > 7 jours)
- Conditions système :
  ✅ Formations obligatoires : 10/10 complétées
  ✅ Sessions de service : 13/12
  ✅ Durée minimum : 3 mois 2 semaines
- Bouton "Voir la fiche complète"
- Boutons d'action : [✅ Approuver] [❌ Refuser avec commentaire]

=== MODALE REFUS ===
- Textarea "Commentaire pour le membre (obligatoire)"
- Bouton "Confirmer le refus"

=== ACTIONS EN LOT ===
- Checkbox sur chaque carte
- Action "Approuver la sélection" si plusieurs cochées

=== ANIMATIONS ===
- Une fois approuvée/refusée : la carte fait un slide-out vers la droite avec color flash
  (vert pour approuver, rouge pour refuser) avant de disparaître
- Compteur en-tête se décrémente animé après chaque traitement
- Confetti léger quand le dernier dossier de la liste est traité
```

---

## 📄 `admin/cultes.html` — Archive des Cultes

```
Crée la page d'archive des cultes EJP (Back Office) en HTML + Tailwind + JavaScript.

=== EN-TÊTE ===
- Titre "⛪ Archive des Cultes"
- Bouton "+ Ajouter un culte"
- Champ de recherche (titre, thème, date)

=== FILTRES ===
- Par thème (dropdown) : Louange / Enseignement / Évangélisation / Prière / Spécial
- Par année : [2024] [2025] [2026]
- Par mois (apparaît quand une année est sélectionnée)

=== GRILLE DE CULTES ===
Cartes cultes (3 colonnes) :
- Thumbnail de la vidéo YouTube en haut
- Badge thème (couleur par thème)
- Titre du culte (Playfair Display)
- Date (icône calendrier)
- Résumé tronqué (2 lignes)
- Bouton ▶️ "Voir le culte" → ouvre modale avec iframe YouTube
- Icônes ✏️ Modifier | 🗑️ Supprimer

=== MODALE AJOUT/MODIFICATION ===
- Titre du culte *
- Date *
- Thème (dropdown)
- Résumé court
- Lien YouTube * → preview automatique

=== ANIMATIONS ===
- Cards : apparition au scroll (Intersection Observer, stagger de 80ms)
- Modale YouTube : slide-up depuis le bas, overlay sombre
- Filtre : transition fade des cartes qui entrent/sortent
```

---

## 📄 `admin/reunions.html` — PV des Réunions

```
Crée la page de gestion des Procès-Verbaux de réunions EJP en HTML + Tailwind + JavaScript.

=== EN-TÊTE ===
- Titre "📋 Procès-Verbaux des Réunions"
- Bouton "+ Nouveau PV"

=== FILTRES & RECHERCHE ===
- Recherche par mot-clé dans le titre
- Filtre département (dropdown) : 
  Équipe Audiovisuelle | Louange | Intercession | Communication | Direction | Accueil
- Filtre période : date début → date fin (date pickers)

=== LISTE DES PV ===
Format liste (plus dense que les cartes) :
Chaque ligne :
- Icône 📄 selon le format (texte ou pièce jointe)
- Nom complet de la réunion selon la convention :
  "Réunion de l'Équipe Audiovisuelle _ 10/04/2026 _ Préparation du service de Pâques"
- Département : badge coloré
- Date : formatée "10 avril 2026"
- Boutons : 👁️ Voir | ✏️ Modifier | ⬇️ Télécharger | 🗑️ Supprimer

=== MODALE AJOUT/CONSULTATION PV ===
Large modal (max-w-4xl) :
- Nom de la réunion * (avec aide "Format : Réunion de [Dept] _ jj/mm/aaaa _ [Thème]")
- Département *
- Date *
- Mode de saisie : ● Texte riche (éditeur WYSIWYG simple) ○ Pièce jointe (upload PDF/Word)
- Contenu : zone de texte large avec outils de formatage basiques (gras, italique, liste)
- Bouton "Enregistrer le PV"

=== ANIMATIONS ===
- Liste : filtre en temps réel avec fade des items
- Accordéon pour afficher le texte du PV inline sans modale
- Badge département : couleur unique par département, générée dynamiquement
```

---

## 📄 `admin/evenements.html` — Gestion des Événements

```
Crée la page de gestion des événements (Back Office) EJP en HTML + Tailwind + JavaScript.

=== EN-TÊTE ===
- Titre "📅 Événements"
- Bouton "+ Créer un événement"
- Toggle vue : [🗂️ Liste] [📅 Calendrier]

=== VUE LISTE ===
Tableau avec colonnes :
Image miniature | Nom | Date | Lieu | Statut (À venir / En cours / Passé) | Notif envoyée ? | Actions

=== VUE CALENDRIER ===
Grille calendrier mensuelle en CSS/JS pur :
- Navigation mois précédent/suivant
- Jours avec événements : point coloré + tooltip au hover avec le nom
- Clic sur une date → modale détail

=== MODALE CRÉATION/MODIFICATION ÉVÉNEMENT ===
- Nom de l'événement *
- Date et heure *
- Lieu *
- Description (textarea)
- Affiche/image : zone upload drag & drop
  → Preview de l'image uploadée avec animation de fondu
- Section "Envoyer une notification" :
  ☐ Envoyer par e-mail
  ☐ Envoyer par SMS
  Destinataires : ● Tous les membres ○ Par statut ○ Par groupe du Chef
  [Aperçu du message] [Envoyer maintenant]

=== ANIMATIONS ===
- Upload image : barre de progression + preview qui zoom-in
- Calendrier : transition slide entre les mois (gauche ←→ droite selon navigation)
- Notification envoyée : animation d'avion en papier qui vole 🛩️ à travers l'écran

=== IMAGE À GÉNÉRER ===
Icône/illustration pour les événements sans image définie :
- Placeholder générique EJP : fond marine avec croix + flamme stylisée + date
  Style affiches modernes d'église africaine, typographie Playfair Display.
```

---

## 📄 `admin/communications.html` — Envoi de Communications

```
Crée la page de gestion des communications (e-mail et SMS) en HTML + Tailwind + JavaScript.

=== LAYOUT EN ONGLETS ===
[📧 E-mail] [📱 SMS] [📜 Historique]

=== ONGLET E-MAIL ===
- Destinataires : 
  Checkboxes : ☑ Tous | ☐ Nouveau Membre | ☐ Star | ☐ Pilote | ☐ Pilier | ☐ Missionnaire
  OU sélection manuelle : champ de recherche avec ajout de membres individuels
  → Compteur live "X membres sélectionnés"
- Objet de l'e-mail *
- Corps du message (éditeur WYSIWYG minimaliste : gras, italique, lien, liste)
- Pièce jointe : upload image/PDF (optionnel)
- Aperçu : bouton "👁️ Prévisualiser" → modale avec rendu de l'e-mail
- Bouton "Envoyer maintenant" (doré) | "Programmer pour plus tard" (outline)

=== ONGLET SMS ===
- Mêmes options de destinataires
- Compteur de caractères en temps réel (160 max pour 1 SMS, barre de couleur)
- Message court : textarea avec limite visible
- Aperçu sur "écran de téléphone" (mockup de téléphone en CSS)
- Bouton "Envoyer le SMS"

=== ONGLET HISTORIQUE ===
- Liste chronologique des communications envoyées :
  📧 "Invitation Culte de Pentecôte" — 10/04/2026 — Envoyé à 124 membres — Taux ouverture : 68%
  📱 "Rappel : Événement demain !" — 09/04/2026 — 89 destinataires
- Filtres : par type (e-mail/SMS), par date

=== ANIMATIONS ===
- Compteur destinataires : animation de chiffre qui change
- Mockup téléphone SMS : apparition avec perspective 3D subtle (transform rotateY)
- Bouton Envoyer : animation loading (spinner) puis confirmation ✅ avec son (optionnel)
```

---

## 📄 `admin/parametres.html` — Paramètres

```
Crée la page de paramètres de l'administration EJP en HTML + Tailwind + JavaScript.

=== SECTIONS ===

**Section 1 — Informations de l'église**
- Nom officiel : Église des Jeunes Prodiges
- Logo (upload)
- Adresse
- Téléphone principal
- Site web / Réseaux sociaux
- Bouton "Enregistrer"

**Section 2 — Gestion des statuts**
Tableau des 5 niveaux avec possibilité de modifier :
- Le nom/libellé
- L'icône associée
- La description affichée aux membres
(Statuts non supprimables, juste modifiables)

**Section 3 — Sécurité**
- Modifier le mot de passe admin
- Liste des comptes administrateurs actifs
- Bouton "Ajouter un co-administrateur"

**Section 4 — Données**
- Bouton "Exporter toute la base membres (CSV)"
- Bouton "Sauvegarder les données (JSON)"
- Zone dangereuse (fond rouge clair) : "Réinitialiser la plateforme" 
  → double confirmation avec saisie du texte "CONFIRMER"

=== ANIMATIONS ===
- Section danger : tremblement au hover du bouton de réinitialisation
- Upload logo : drag & drop avec preview
- Sauvegarde : animation de téléchargement avec barre de progression
```

---

# 🔧 NOTES TECHNIQUES GLOBALES

```
=== FICHIERS COMMUNS À CRÉER ===
/assets/
  css/
    tailwind.min.css  (via CDN)
    animations.css    (keyframes custom : pulse-ring, shimmer, shake, slide-in, confetti)
    theme.css         (variables CSS globales : couleurs, fonts, shadows)
  js/
    utils.js          (fonctions partagées : formatDate, toast notification, openModal)
    animations.js     (Intersection Observer pour scroll reveal, compteurs animés)
  img/
    logo-ejp.svg      (logo EJP à créer)
    placeholder-event.jpg
    placeholder-avatar.svg

=== CDN À INCLURE DANS TOUTES LES PAGES ===
- Tailwind CSS : https://cdn.tailwindcss.com
- Google Fonts : Playfair Display + Inter
- Lucide Icons (ou Heroicons) pour les icônes SVG
- Optionnel : Alpine.js pour les interactions légères

=== CONVENTIONS DE CODE ===
- Composants réutilisables en JavaScript vanille (fonctions createCard(), createModal())
- Classes Tailwind custom via @apply dans animations.css
- data-* attributes pour le JS (ex: data-modal="membre-detail")
- Commentaires en français dans le code

=== RESPONSIVE BREAKPOINTS ===
- Mobile  : < 768px  → tout en colonne, sidebar en drawer
- Tablet  : 768–1024px → sidebar réduite à icônes seules
- Desktop : > 1024px → layout complet sidebar + contenu
```

---

*Document généré pour l'EJP — Avril 2026 — Usage interne*
*Stack : HTML + Tailwind CSS + JavaScript Vanilla*
