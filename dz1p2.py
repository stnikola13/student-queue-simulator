import random

class ListNode:                                                                  # Klasa cvora (studenta).
    def __init__(self, fName=None, lName=None, bid=None, major=None, year=None):
        self.fName = fName                                                      # Informacija o imenu studenta.
        self.lName = lName                                                      # Informacija o prezimenu studenta.
        self.bid = bid                                                          # Broj indeksa studenta.
        self.major = major                                                      # Studijski program studenta.
        self.year = year                                                        # Godina studija studenta.
        self.next = None                                                        # Pokazivac.

class ListHeader:                                                           # Heder ulancane liste, ujedno i klasa
    def __init__(self):                                                     # cele ulancane liste.
        self.head = None                                                    # Inicijalizacija hedera sa pokazivacem na
        self.numElem = 0                                                    # None i brojacem elemenata.

    def insert(self, fName, lName, bid, major, year):                       # Umetanje novog cvora.
        new = ListNode(fName, lName, bid, major, year)
        if self.head == None:                                               # Ukoliko lista nema elemenata, kao jedan
            self.head = new                                                 # jedini se postavlja new cvor i vezuje
            new.next = self                                                 # za heder. Brojac se povecava za jedan.
            self.numElem += 1
        else:
            p = self.head                                                   # U slucaju da postoji bar jedan clan liste,
            while (p != self):                                              # formira se pokazivac p koji ce iterirati
                if p.bid == new.bid:                                        # sve dok ne dodje do kraja liste. U toku
                    break                                                   # prolaska proverava da li postoji student
                if p.next == self:                                          # sa istim brojem indeksa kao onaj koji
                        self.numElem += 1                                   # treba da se upise. Ukoliko postoji
                        p.next = new                                        # preskace se umetanje tog cvora.
                        new.next = self                                     # Pokazivac dolazi do kraja i umece novi
                        break                                               # cvor na kraj liste.
                p = p.next

    def fetch(self, number):
        """ Funckija fetch podrazumeva da ce indeks koji se unosi biti u range-u duzine liste. """
        p = self.head                                                       # Funkcija fetch na osnovu number (indeksa)
        counter = 1                                                         # koji se unosi pronalazi element sa tim
        while (p != self):                                                  # brojem, poredeci brojac counter i number.
            if (counter == number):                                         # Kada dodje do match-a vraca podatke.
                return p.fName, p.lName, p.bid, p.major, p.year
            p = p.next
            counter += 1

    def delete(self, bid):
        """Funckija delete u ovom slucaju brise studenta iz liste na osnovu broja indeksa koji korisnik unese."""
        if self.head == None:                                                   # Ukoliko je lista prazna, izbacuje se
            print("U listi nema studenata. Molimo prvo unesite podatke o studentima.\n")                     # greska.
        else:
            testNode = ListNode(bid=bid)                                        # Ukoliko nije, sledi postupak:
            p = self.head                                                       # p je pokazivac na prvi element.
            q = None                                                            # q je pokazivac za jedno mesto iza p-a.
            t = False                                                           # t je pom. prom. koja belezi da li je
            while (p != self):                                                  # obavljeno brisanje.
                if (p.next == self) and (q == None) and (testNode.bid == p.bid):
                    p.next = None                                               # Slucaj kad je u pitanju prvi jedini
                    self.head = None                                            # cvor, tada se on brise i prevezuje se
                    t = True                                                    # lista.
                    break
                elif (testNode.bid == p.bid):                                   # U ostalim slucajevima, kad se naidje
                    if p == self.head:                                          # na cvor sa istim brojem indeksa, prvo
                       self.head = p.next                                       # se proverava da li je prvi cvor.
                       p.next = None                                            # Ako jeste, prevezuje se heder.
                    else:                                                       # U slucaju da nije prvi vrsi se
                        q.next = p.next                                         # klasicno premestanje pokazivaca.
                        p.next = None
                    t = True
                    break
                q = p                                                           # Iteracija pokazivaca.
                p = p.next
            if t:
                self.numElem -= 1                                               # Ukoliko je izvrseno brisanje, brojac
            if not t:                                                           # elem. se smanjuje za jedan; ukoliko
                print("Dati student ne postoji u listi!\n")                     # nije,izbacuje se obavestenje o greski.

    def createQueue(self):                                                      # Funkcija za kreiranje reda od liste.
        queue = ListHeader()
        while (self.numElem > 0):                                               # Dokle god postoji elemenata u listi
            n = random.randint(1, self.numElem)                                 # ciklus dohvata podatke studenta sa
            fName, lName, bid, major, year = self.fetch(n)                      # rednim brojem u listi koji generise
            self.delete(bid)                                                    # random. Brise iz liste i dodaje u red.
            queue.insert(fName, lName, bid, major, year)
        return queue

    def isEmpty(self):                                                          # Proverava da li je red prazan.
        if self.numElem == 0:
            return True
        else:
            return False

    def simulate(self, threshold):                                              # Funkcija za simuliranje upisa.
        steps = 0                                                               # Steps je brojac koraka.
        while not(self.isEmpty()):                                              # Dokle god lista nije prazna ulazi se
            p = self.head                                                       # u ciklus, generise broj i uporedjuje
            steps += 1                                                          # sa pragom threshold. Ukoliko je veci,
            n = random.random()                                                 # ispisuju se neophodni podaci, i
            fName, lName, bid, major, year = self.fetch(1)                      # student sa datim podacima se brise iz
            self.delete(bid)                                                    # reda; ukoliko nije, brise se student
            if (n >= threshold):                                                # pa se ponovo dodaje na kraj reda.
                print("{} {}, {}. godina upisana".format(fName, lName, int(year) + 1))
            else:                                                               # Na pocetku svakog ulaska u ciklus se
                self.insert(fName, lName, bid, major, year)                     # pokazivac vraca na prvi element usled
                                                                                # konstantnog menjanja duzine reda.
        return steps                                                            # F-ja vraca vrednost steps.

# Napomena: Za korak je uzet svaki pokusaj upisa (ili se student upise, ili se prebaci na kraj read).

# Main program

random.seed()
students = ListHeader()
queue = None

print("----------------------------------------------")
print("Simulacija upisa na ETF - interaktivni program")
print("----------------------------------------------")
print("Opcije:")
print("1) Ucitavanje novog studenta")
print("2) Obrisi postojeceg studenta")
print("3) Ispisi spisak studenata")
print("4) Kreiraj red")
print("5) Izvrsi simulaciju")
print("6) Dohvati informacije o studentu")
print("7) Zavrsetak programa")
print("Napomena: Ukoliko ste tek pokrenuli program, prvo unesite podatke o studentima.")


''' Funcionalnost glavnog programa: Komentari nisu individulano pisani vec se ovde navode osnove. Unosi se ceo broj
izmedju 1 i 7 za izbor opcije u meniju. Nakon izbora bilo koje od opcija u zavisnosti od podatka koji se dodatno
trazi se proverava ispravnost tog podatka i ispisuje greska ukoliko je pogresno unet i ulazi se u sledecu iteraciju
ciklusa. Opcija 1 pomocu funkcije insert ubacuje studenta u ulancanu listu, opcija dva na osnovu indeksa pomocu
funkcije delete brise studenta iz liste. Opcije 3 prikazuje spisak studenata u listi na osnovu jednog prolaska kroz
listu. Opcija 4 pomocu funkcije createQueue formira red. Opcija 5 nakon unetog praga izvrsava simulaciju koristeci
funkciju simulate. Opcija 6 polazi jednom kroz listu i ukoliko postoji dohvata informacije o studentu sa unetim brojem
indeksa. Opcija 7 zavrsava program. '''


while True:
    print("----------------------------------------------------------")
    print("Odaberite neku od navedenih opcija unosom broja u konzolu:")
    n = input()
    try:
        n = int(n)
    except Exception:
        print("Neispravan unos!")
        continue
    if not (1 <= n <= 7):
        print("Neispravan unos!")
        continue

    if n == 1:
        print("--- Dodaj novog studenta ---")
        data = input("Molimo unesite podatke u obliku: Ime Prezime gggg/bbbb Smer Godina: ").strip().split()
        if (len(data) != 5):
           print("Neispravno uneti podaci!")
           continue
        if (data[3] not in {"ER", "SI"}):
            print("Neispravan studijski program!")
            continue
        try:
            m = int(data[-1])
        except Exception:
            print("Neispravna godina studiranja!")
            continue
        if not (1 <= m <= 4):
            print("Neispravna godina studiranja!")
            continue
        try:
            year, id = data[2].split("/")
            if (len(year) != 4) or (len(id) != 4):
                print("Neispravan broj indeksa!")
                continue
            year = int(year)
            id = int(id)
        except Exception:
            print("Neispravan broj indeksa!")
            continue

        students.insert(data[0], data[1], data[2], data[3], data[4])
        print("Student uspesno dodat!")

    if n == 2:
        print("--- Obrisi postojeceg studenta ---")
        data = input("Molimo unesite broj indeksa studenta u obliku gggg/bbbb: ").strip()
        try:
            year, id = data.split("/")
            if (len(year) != 4) or (len(id) != 4):
                print("Neispravan broj indeksa!")
                continue
            year = int(year)
            id = int(id)
        except Exception:
            print("Neispravan broj indeksa!")
            continue
        if students.isEmpty():
            print("Nema studenata u listi!")
            continue
        students.delete(data)
        print("Student obrisan.")

    if n == 3:
        p = students.head
        if (p != None):
            print("-----------------")
            print("Spisak studenata")
            print("-----------------")
            while (p != students):
                print("{} {}, {}, {}, {}. godina".format(p.fName, p.lName, p.bid, p.major, p.year))
                p = p.next
            print("Ukupan broj unetih studenata je {}.".format(students.numElem))
        else:
            print("Nema unetih studenata. Molimo prvo unesite podatke o studentima!")

    if n == 4:
        if students.isEmpty():
            print("Nema unetih studenata. Molimo prvo unesite podatke o studentima!")
            continue
        else:
            queue = students.createQueue()
            ans = input("Red uspesno kreiran! Prikazi red? (Da/Ne) ").strip()
            if (ans.lower() not in {"da", "ne"}):
                print("Pogresan unos")
                continue
            if (ans.lower() == "da"):
                p = queue.head
                if (p != None):
                    print("------------------------")
                    print("Spisak studenata u redu")
                    print("------------------------")
                    while (p != queue):
                        print("{} {}, {}, {}, {}. godina".format(p.fName, p.lName, p.bid, p.major, p.year))
                        p = p.next
                    print("Ukupan broj unetih studenata je {}.".format(queue.numElem))
            elif (ans.lower() == "ne"):
                print("Red nije ispisan.")
                continue

    if n == 5:
        if (queue == None):
            print("Nije formiran red. Molimo prvo formirajte red!")
            continue
        else:
            threshold = input("Molimo unesite prag za simulaciju 0<=x<=0.5: ")
            try:
                threshold = float(threshold)
            except Exception:
                print("Pogresan unos!")
            if not (0 <= threshold <= 0.5):
                print("Pogresan unos!")
            else:
                print("Simulacija uspesno izvrsena.")
                print("----------------------------")
                print("- Spisak upisanih studenata -")
                steps = queue.simulate(threshold)
                print("-----------------------------------")
                print("Broj koraka tokom simulacije je {}.".format(steps))

    if n == 6:
        if (queue.head == None):
            print("Nije formiran red. Molimo prvo formirajte red!")
            continue
        else:
            bid = input("Molimo unesite indeks studenta: ")
            try:
                year, id = bid.split("/")
                if (len(year) != 4) or (len(id) != 4):
                    print("Neispravan broj indeksa!")
                    continue
                year = int(year)
                id = int(id)
            except Exception:
                print("Neispravan broj indeksa!")
                continue
            p = queue.head
            t = False
            while (p != queue):
                if (p.bid == bid):
                    print("--- Podaci o trazenom studentu ---")
                    print("{} {}, {}, {}, {}.godina".format(p.fName, p.lName, p.bid, p.major, p.year))
                    t = True
                    break
                p = p.next
            if not t:
                print("Student sa unetim indeksom ne postoji u redu!")

    if n == 7:
        print("----------------------------")
        print("Program zaustavljen. Zdravo!")
        break