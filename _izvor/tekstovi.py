# Tekstovi stranice. Svaki tekst ima verziju na hrvatskom (hr), engleskom (en) i talijanskom (it).
# Odlomci su odvojeni praznim retkom. Kod pjesama se prijelomi redaka čuvaju.
# Redak koji sadrži samo ". . ." prikazuje se kao pauza na sredini.
# Novi tekst: dodaj ga na VRH popisa TEKSTOVI (najnoviji prvi), pa pokreni:  python3 _izvor/build.py

TEKSTOVI = [
    {
        "vrsta": "crtica",
        "datum": "2026-11-03",
        "hr": {
            "slug": "masline",
            "naslov": "Masline",
            "opis": "Crtica na čakavskom o jednom danu berbe maslina, od jutarnje rose do gorčeg ulja.",
            "tekst": """
Jutra nisu rana. Rabi čekati da se jutarnja rosa osuši. Svejeno se skupimo do 8 najkašnije. Gre ki je šerijo. Kante, mriže, grablje. Tresač nikako jer će ruvinati stablo!

Tri auta, dvoje dice, samo jedna prikolica jer druga auta nimaju kuku. Svake godine ista priča. Trebali smo još malo čekati. Radman će biti loš. Nismo zadovoljni.

Ali drugače nismo mogli dobiti godišnji. Nidan od nas. Tečemo prije i pokle dela. Po dicu, po grablje, po mrižu, po pinjate s užinon. Pa zabimo jisti, dok prven nisu ruke i kolina počela klecati.

Manji je vrga maslinu u usta. Nismo snimili ča je načinija s licen, ali svi ćemo se toga sjećati. Teti se pauk spustija na glavu, pa je vikala. Do drugega maslinika su je čuli.

Do podne smo u kratkima, i fali za piti. Predvečer doma gremo bez riči. Dica spidu, radio sviri. Klima u autu grije da se ki ne nazebe. Ali ruke i dalje trepe. Križa zatežu, oči na po koplja.

Jene grablje smo puštili.

Nisu isti ljudi brali ovega lita. A ulje je bilo gorčije nego prija.
""",
        },
        "en": {
            "slug": "olives",
            "naslov": "Olives",
            "opis": "A sketch about one day of the olive harvest in Istria, from the morning dew to a more bitter oil.",
            "tekst": """
The mornings don’t start early. You have to wait for the morning dew to dry. Still, we gather by eight at the latest. The serious ones show up. Buckets, nets, rakes. No shaker, never, it would ruin the tree!

Three cars, two kids, only one trailer, because the other cars have no tow hook. Same story every year. We should have waited a little longer. The yield will be poor. We are not happy.

But there was no other way to get the days off. Not for any of us. We run around before and after work. For the kids, for the rakes, for the net, for the pots with lunch. Then we forget to eat, until the first of us feels their hands and knees begin to give.

The little one put an olive in his mouth. We didn’t film the face he made, but we will all remember it. A spider dropped onto auntie’s head, and she screamed. They heard her in the next olive grove.

’Til noon we are in short sleeves, and there is nothing to drink. Towards evening we drive home without a word. The kids sleep, the radio plays. The heater is on in the car, so nobody catches a cold. But our hands still tremble. Our backs ache, our eyes droop.

One rake we left untouched.

It wasn’t the same people harvesting this year. And the oil was more bitter than before.
""",
        },
        "it": {
            "slug": "olive",
            "naslov": "Olive",
            "opis": "Un bozzetto su una giornata di raccolta delle olive in Istria, dalla rugiada del mattino a un olio più amaro.",
            "tekst": """
Le mattine non iniziano presto. Bisogna aspettare che la rugiada del mattino si asciughi. Comunque ci troviamo entro le otto al più tardi. Arriva chi fa sul serio. Secchi, reti, rastrelli. Niente scuotitore, mai, rovinerebbe l’albero!

Tre macchine, due bambini, un solo rimorchio, perché le altre macchine non hanno il gancio. Ogni anno la stessa storia. Avremmo dovuto aspettare ancora un po’. La resa sarà scarsa. Non siamo contenti.

Ma in nessun altro modo riuscivamo ad avere le ferie. Nessuno di noi. Corriamo prima e dopo il lavoro. A prendere i bambini, i rastrelli, la rete, le pentole con la merenda. Poi ci dimentichiamo di mangiare, finché al primo non cominciano a cedere le mani e le ginocchia.

Il piccolo si è messo un’oliva in bocca. Non abbiamo filmato la faccia che ha fatto, ma ce la ricorderemo tutti. Alla zia è sceso un ragno sulla testa e ha urlato. L’hanno sentita fino all’oliveto accanto.

Fino a mezzogiorno siamo in maniche corte, e manca sempre da bere. Verso sera torniamo a casa senza una parola. I bambini dormono, la radio suona. In macchina il riscaldamento è acceso perché nessuno si raffreddi. Ma le mani tremano ancora. La schiena tira, gli occhi mezzi chiusi.

Un rastrello non l’abbiamo toccato.

Quest’anno a raccogliere non c’erano le stesse persone. E l’olio era più amaro di prima.
""",
        },
    },
    {
        "vrsta": "kolumna",
        "datum": "2026-10-30",
        "hr": {
            "slug": "tri-sekunde-tisine",
            "naslov": "Tri sekunde tišine",
            "opis": "Kolumna o tišini u radijskom razgovoru i o tome zašto je ponekad važnija od sljedećeg pitanja.",
            "tekst": """
Na radiju postoji izraz za tišinu koja traje predugo. Zovemo je mrtvi zrak. Tri sekunde bez glasa, bez glazbe. Dovoljne da slušatelj pomisli da se nešto pokvarilo. Da mi se dlanovi oznoje, srce brže počne lupati, a oči panično tražiti uzrok. Playlista, pult, botuni, tehničar.

Gdje je greška? Što sam krivo stisnula? Ima li struje?

Naučili smo se bojati tih sekundi. Pažljivo pratiti. Popuniti ponovljenim najavama, džinglovima, vremenskom prognozom. A ponekad bi upravo tišina rekla više od svega što imamo pripremljeno.

Kad smo zadnji put stali?

Mislim na razgovore o ne baš jednostavnim temama. Na prijateljicu koja prvi put naglas kaže da se nakon poroda nije prepoznala. Na oca koji opisuje čekaonicu onkologije. Na trenutak nakon što sugovornik izgovori nešto što ga je koštalo vremena… života… ljudi.

Ne treba tada sljedeće pitanje. Treba tri sekunde. Treba pustiti da rečenica sjedne, da slušatelj čuje do kraja, da i on malo zašuti.

Nedavno sam razgovarala s jednom majkom o tome kako je postala mama. Čekala je jedno, a dobila dvoje. Razumijemo li to? Možda. Nudimo li suosjećanje ili priliku da sebe pronađemo u toj priči? Vrlo vjerojatno ovo drugo.

Živimo u vremenu kada ne slušamo. Čekamo red da nešto kažemo. Što prije. Što brže. Što glasnije.

Potrebna je tišina. U svijetu koji vrišti, koji se cijepa, koji se pali, koji blješti reklamama i lijepim licima – izaberi mene!!! – nema ljudi koji zastaju da ti stave ruku na rame. A opet tu smo, jedni kraj drugih, licem u lice, više i bliže nego ikad prije.

„Slušaj…“, rekla mi je sugovornica. I prije nego što je nastavila svoju priču, čula sam udah, njezinu knedlu u grlu, izdah. Hrabar, a toliko težak da sam i ja osjetila teret u svojem krilu. I lagala bih kad bih rekla da sam ga nosila skupa s njom kroz razgovor. Nosila sam tek mali dio.

A ispred mene tonski zapis koji teče. Glas koji ostaje. I tanka vodoravna linija iza svakog slušaj.

Udah, knedla u grlu, izdah. Točno tri sekunde. Potrebne tri sekunde. Za nju, za mene, za tebe (kad jednog dana čuješ tu priču).

Ništa onda nije stalo. Ništa onda nije mrtvo. Sve je baš tu. Kad udahneš da te uvuče u tu dubinu, s knedlom spusti dolje kroz grlo, u tvoju nutrinu. Da si tu, da čuješ, iako nema tona. Ali je jeka glasnija no ikad. Od nje, do mene, do tebe, i od tebe dalje.

Slušaj

. . .

ili čitaj. Stavila sam ovdje tri točke, za svaku tu sekundu.

Da prođe ta priča, čiju god da slušaš. Da je osjetiš, da je čuješ. Da si tu. Pričekaj.

Ne svoj red. Ne sljedeće pitanje. Treba tri sekunde… života između nas.

Mrtvi zrak, kažemo. A meni se čini da je to najživlji dio emisije.
""",
        },
        "en": {
            "slug": "three-seconds-of-silence",
            "naslov": "Three seconds of silence",
            "opis": "A column about silence in a radio conversation, and why it sometimes matters more than the next question.",
            "tekst": """
In radio there is a term for silence that lasts too long. We call it dead air. Three seconds without a voice, without music. Enough for a listener to think something has broken. Enough for my palms to sweat, my heart to beat faster and my eyes to search in panic for the cause. Playlist, desk, buttons, technician.

Where is the mistake? What did I press wrong? Has the power gone out?

We have learned to fear those seconds. To watch them closely. To fill them with repeated announcements, jingles, the weather forecast. And yet sometimes silence would say more than anything we have prepared.

When did we last stop?

I think of conversations about subjects that are anything but simple. Of a friend saying out loud, for the first time, that after giving birth she did not recognize herself. Of a father describing the waiting room of an oncology ward. Of the moment after a guest says something that cost them time… life… people.

That is when you don’t need the next question. You need three seconds. You need to let the sentence sink, let the listener hear it to the end, let them fall quiet for a moment, too.

Not long ago I spoke with a mother about how she became a mum. She waited for one, and got two. Do we understand that? Maybe. Do we offer compassion, or a chance to find ourselves in that story? Most likely the latter.

We live in a time when we don’t listen. We wait for our turn to say something. As soon as possible. As fast as possible. As loud as possible.

We need silence. In a world that screams, that splits, that catches fire, that glitters with ads and pretty faces – pick me!!! – there are no people who stop to put a hand on your shoulder. And yet here we are, side by side, face to face, more and closer than ever before.

“Listen…”, my guest said. And before she went on with her story, I heard her breathe in, the lump in her throat, the breath out. Brave, and so heavy that I felt the weight in my own lap. I would be lying if I said I carried it with her through the conversation. I carried only a small part.

And in front of me, the recording running. A voice that stays. And a thin horizontal line after every listen.

Breath in, the lump in the throat, breath out. Exactly three seconds. The three seconds that were needed. For her, for me, for you (when one day you hear that story).

Nothing stopped then. Nothing was dead. Everything was right there. When you breathe in and it pulls you into that depth, the lump goes down your throat, deep inside you. So that you are there, so that you hear, even though there is no sound. But the echo is louder than ever. From her, to me, to you, and on from you.

Listen

. . .

or read. I have put three dots here, one for each of those seconds.

Let the story pass through, whoever’s story you are listening to. Let yourself feel it, hear it. Be there. Wait.

Not your turn. Not the next question. It takes three seconds… of life between us.

Dead air, we call it. To me it feels like the most alive part of the show.
""",
        },
        "it": {
            "slug": "tre-secondi-di-silenzio",
            "naslov": "Tre secondi di silenzio",
            "opis": "Una rubrica sul silenzio in una conversazione radiofonica e sul perché a volte conta più della domanda successiva.",
            "tekst": """
In radio esiste un nome per il silenzio che dura troppo. Gli inglesi lo chiamano *dead air*, aria morta. Tre secondi senza voce, senza musica. Bastano perché l’ascoltatore pensi che qualcosa si sia rotto. Perché mi sudino le mani, il cuore cominci a battere più forte e gli occhi cerchino in preda al panico la causa. Playlist, mixer, tasti, tecnico.

Dov’è l’errore? Cosa ho premuto per sbaglio? È andata via la corrente?

Abbiamo imparato a temere quei secondi. A sorvegliarli. A riempirli di annunci ripetuti, jingle, previsioni del tempo. Eppure a volte proprio il silenzio direbbe più di tutto ciò che abbiamo preparato.

Quand’è stata l’ultima volta che ci siamo fermati?

Penso alle conversazioni su temi tutt’altro che semplici. A un’amica che per la prima volta dice ad alta voce che dopo il parto non si è riconosciuta. A un padre che descrive la sala d’attesa di un reparto di oncologia. Al momento in cui l’interlocutore pronuncia qualcosa che gli è costato tempo… vita… persone.

In quel momento non serve la domanda successiva. Servono tre secondi. Bisogna lasciare che la frase resti, che l’ascoltatore la senta fino in fondo, che anche lui taccia un po’.

Di recente ho parlato con una madre di come è diventata mamma. Ne aspettava uno, e ne sono arrivati due. Lo capiamo? Forse. Offriamo compassione o l’occasione di ritrovare noi stessi in quella storia? Molto probabilmente la seconda.

Viviamo in un tempo in cui non ascoltiamo. Aspettiamo il nostro turno per dire qualcosa. Il prima possibile. Il più in fretta possibile. Il più forte possibile.

Serve il silenzio. In un mondo che urla, che si spacca, che prende fuoco, che brilla di pubblicità e bei volti – scegli me!!! – non ci sono persone che si fermano a metterti una mano sulla spalla. Eppure siamo qui, uno accanto all’altro, faccia a faccia, più che mai e più vicini che mai.

«Ascolta…», mi ha detto la mia interlocutrice. E prima che continuasse la sua storia ho sentito un respiro, il nodo alla gola, un sospiro. Coraggioso, e così pesante che ne ho sentito il peso anche in grembo. Mentirei se dicessi di averlo portato insieme a lei per tutta la conversazione. Io ne ho portato solo una piccola parte.

E davanti a me la registrazione che scorre. Una voce che resta. E una sottile linea orizzontale dopo ogni ascolta.

Un respiro, il nodo alla gola, un sospiro. Esattamente tre secondi. I tre secondi necessari. Per lei, per me, per te (quando un giorno sentirai questa storia).

Allora niente si è fermato. Niente era morto. Era tutto lì. Quando inspiri e ti trascina in quella profondità, con il nodo scendi giù per la gola, dentro di te. Perché tu sia lì, perché tu senta, anche se non c’è suono. Ma l’eco è più forte che mai. Da lei, a me, a te, e da te ancora oltre.

Ascolta

. . .

o leggi. Ho messo qui tre puntini, uno per ogni secondo.

Lascia che quella storia passi, di chiunque sia la storia che stai ascoltando. Che tu la senta, che tu l’ascolti. Che tu sia lì. Aspetta.

Non il tuo turno. Non la domanda successiva. Servono tre secondi… di vita tra noi.

Aria morta, la chiamano. A me sembra la parte più viva della trasmissione.
""",
        },
    },
    {
        "vrsta": "pjesma",
        "datum": "2026-10-30",
        "hr": {
            "slug": "majica",
            "naslov": "Majica",
            "opis": "Pjesma o jednoj majici koja je prošla ljubav, majčinstvo i sve ono što se šiva.",
            "tekst": """
Imaš li ti jednu ovakvu majicu?
Crnu, ali sad sivu
s natpisom koji ti je oko nasmijalo,
možda tek ostavilo uspomenu živu.

Moja ima bateriju, da
(polupraznu ili polupunu, ovisi kako gledaš)
I čekam da se napuni već par ljeta.

Bila je Ivanova dugo, pa moja.
Odavno joj se rastegnuo ovratnik
i promijenila boja.

Prošla je utrke, plaže i mora
Neprospavane noći, i jutra spora.
Mrlje, koje se na jakom suncu još vide.
Male ruke koje su je rastegnule,
život što ide.

Moju majicu su vukli,
prljali, tukli.
Grizli, vezali, parali
– s njom smo dva života stvarali.

Ali vratim joj se uvijek.
Nekako se nadam
da će sunce napuniti bateriju kad padam.

Nekad je bila crna,
Sad je gotovo siva…
I uz sve rupe na njoj,
Sve što se zašiva…

Ostaje naša.

Čitava
– crna, ali siva.
""",
        },
        "en": {
            "slug": "the-t-shirt",
            "naslov": "The T-shirt",
            "opis": "A poem about one T-shirt that has lived through love, motherhood and everything that gets mended.",
            "tekst": """
Do you have a T-shirt like this?
Black, but grey now,
with a print that once made your eye smile,
or maybe just left a memory that lives on.

Mine has a battery, yes
(half empty or half full, depends how you look at it)
And I’ve been waiting a few summers now for it to charge.

For a long time, it was Ivan’s, then mine.
Its collar stretched long ago, and its colour went blind.

It has been through races, beaches and seas,
sleepless nights and slow mornings.
Stains that still show when the sun is high,
small hands that stretched it, life goin’ by.

My T-shirt has been pulled,
dirtied, beaten.
Bitten, tied, torn
– in it, two lives were born.

But I always come back to it.
Somehow, I hope the sun will charge the battery when I fall.

It used to be black, now it’s almost grey…
And with all its holes,
all the mending along the way…

It stays ours.

Whole
– black, but grey.
""",
        },
        "it": {
            "slug": "la-maglietta",
            "naslov": "La maglietta",
            "opis": "Una poesia su una maglietta che ha attraversato l’amore, la maternità e tutto ciò che si ricuce.",
            "tekst": """
Ce l’hai anche tu una maglietta così?
Nera, ma ora grigia,
con una scritta che ti ha fatto sorridere gli occhi,
o forse lasciato il ricordo che tocchi.

La mia ha una batteria, sì
(mezza scarica o mezza carica, dipende da come la guardi)
e aspetto che si carichi ormai da qualche estate.

È stata a lungo di Ivan, poi mia.
Il colletto si è sformato da tempo
e il colore è andato via.

Ha passato gare, spiagge e mari,
notti insonni e mattine lente.
Macchie, che al sole forte si vedono ancora.
Piccole mani che l’hanno allargata,
la vita che vola.

La mia maglietta l’hanno tirata,
sporcata, picchiata.
Morsa, legata, strappata
– con lei il doppio d'una vita è stata creata.

Ma ci torno sempre.
In qualche modo spero
che il sole ricarichi la batteria quando cado davvero.

Un tempo era nera,
ora è quasi grigia…
E con tutti i suoi buchi,
tutto ciò che si ripigia…

Resta nostra.

Intera
– nera, ma grigia.
""",
        },
    },
    {
        "vrsta": "crtica",
        "datum": "2026-10-30",
        "hr": {
            "slug": "jutarnji-program",
            "naslov": "Jutarnji program",
            "opis": "Crtica o jutru u pekari prije posla i teti koja zna sve vijesti prije novinara.",
            "tekst": """
Jedem zdravo, ali svako jutro kad radim od sedam, parkiram auto na uzbrdici kraj mesnice i bacam se u lov na bijeli *doughnut*. Svatko ima svoje grijehe. Kolegama uzmem čokoladni kroasan. Nisam ih nikad pitala žele li to. Zaključila sam da je šećer bolji prije lokalnih vijesti nego na kraju dana.

Teta za pultom zna sve vijesti prije nas. Dok mi slaže sve u jedan veliki škatroc da se ne zgnječi, ispriča mi zašto djeca danas kasnije idu u školu, koji su radovi na cesti (a nitko nije najavio!?), što se danas obilježava, zašto autobus opet kasni.

„Puštite to u eter“, kaže i namigne.

Često se zapitam o stvarima koje navodno znam. Jesam li ja to promašila dan? Trebam li biti na terenu, a ne za njenim pultom?

I dok ja imam svoje dvojbe, ona mi iznova kaže da san lipa, i da danas izgledam manje umorno. „Pomalo na delu i lipi dan“, rečenica je uvijek ista. Ali uvijek jednako zagrije.

Do lokalnih vijesti nema više ni *doughnuta* ni kroasana. A ja sam već čula najbolji jutarnji program.
""",
        },
        "en": {
            "slug": "the-morning-show",
            "naslov": "The morning show",
            "opis": "A sketch about a morning at the bakery before work, and the woman who knows the news before the journalists do.",
            "tekst": """
I eat healthily, but every morning when I start work at seven, I park on the hill by the butcher’s and go hunting for a white doughnut. Everyone has their sins. For my colleagues I get chocolate croissants. I have never asked them whether they wanted them. I decided sugar is better before the local news than at the end of the day.

The woman behind the counter knows all the news before we do. While she packs everything into one big paper bag, so nothing gets squashed, she tells me why children start school later these days, which roadworks are on (and nobody announced them!?), what is being marked today, why the bus is late again.

“Put that on the air,” she says, and winks.

I often wonder about the things I supposedly know. Have I missed the day? Should I be out in the field rather than behind her counter?

And while I sit with my doubts, she tells me once again that I look lovely, and less tired today. “*Pomalo na delu i lipi dan*” – take it easy at work, and have a lovely day. The sentence is always the same. But it always warms me just as much.

By the local news there is not a doughnut or a croissant left. And I have already heard the best morning show.
""",
        },
        "it": {
            "slug": "il-programma-del-mattino",
            "naslov": "Il programma del mattino",
            "opis": "Un bozzetto su una mattina in panetteria prima del lavoro e sulla signora che sa le notizie prima dei giornalisti.",
            "tekst": """
Mangio sano, ma ogni mattina quando lavoro dalle sette, parcheggio in salita vicino alla macelleria e vado a caccia di un *doughnut* bianco. Ognuno ha i suoi peccati. Ai colleghi prendo croissant al cioccolato. Non ho mai chiesto se li vogliano. Ho deciso che lo zucchero è meglio prima del notiziario locale che alla fine della giornata.

La signora al banco sa tutte le notizie prima di noi. Mentre mi sistema tutto in un grande cartoccio perché non si schiacci, mi racconta perché oggi i bambini vanno a scuola più tardi, quali lavori ci sono sulla strada (e nessuno li ha annunciati!?), che ricorrenza è oggi, perché l’autobus è di nuovo in ritardo.

«Questo dillo in onda», dice e mi fa l’occhiolino.

Spesso mi interrogo sulle cose che presumibilmente so. Ho sbagliato giornata? Dovrei essere sul campo, e non al suo banco?

E mentre io ho i miei dubbi, lei mi ripete che sono bella e che oggi sembro meno stanca. «*Pomalo na delu i lipi dan*» – piano col lavoro, e buona giornata. La frase è sempre la stessa. Ma scalda ogni volta allo stesso modo.

All’ora del notiziario locale non resta più né un *doughnut* né un croissant. E io ho già sentito il miglior programma del mattino.
""",
        },
    },
]
