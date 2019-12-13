import random

import database as db

book_list = [
["The Hunger Games", "Suzanne Collins"],
["Harry Potter and the Philosopher's Stone", "J.K Rowling"],
["Harry Potter and the Chamber of Secrets", "J.K Rowling"],
["Harry Potter and the Prisoner of Azkaban", "J.K Rowling"],
["Harry Potter and the Goblet of Fire", "J.K Rowling"],
["Harry Potter and the Order of Phoenix", "J.K Rowling"],
["Harry Potter and the Half-Blood Prince", "J.K Rowling"],
["Harry Potter and the Deathly Hallows", "J.K Rowling"],
["Harry Potter and the Cursed Child, Parts I", "J.K Rowling"],
["Harry Potter and the Cursed Child, Parts II", "J.K Rowling"],
["To Kill a Mockingbird", "Harper Lee"],
["Pride and Prejudice", "Jane Austen"],
["Twillight", "Stephenie Meyer"],
["The Book Thief", "Markus Zusak"],
["Animal Farm", "George Orwell"],
["The Chronicles of Narnia", "C.S. Lewis"],
["The political future of the European Community", "R. Pryce"],
["Handbuch der organischen Chemie", "F.K. Beilstein"],
["Corporation tax", "C.N. Beattie"],
["Report of an information science index languages test", "E. Michael Keen and Jeremy A. Digger"],
["Institutions of economic growth", "J.P.Powelson"],
["Industrial approaches to urban problems", "Jordan D. Lewis, Lynn Lewis"],
["The constitution of inorganic compounds", "John L.T. Waugh"],
["The Japanese steel industry", "K. Kawahito"],
["Practical instrumentation tranducers", "by F.J. Oliver"],
["The rise and development of Western civilization", "J.L. Stipp, A.W. Dirrim, C.W. Hollister"],
["Bayeux in the late eighteenth century", "Hufton, Olwen H"],
["Human factor aspects of aircraft noise", "H. C. Ganguli and M. S. Prakash Rao"],
["International liquidity", "R. Hawtrey"],
["The Counter-Revolution, doctrine and action, 1789-1804", "J. Godechot."], 
["Transport", "J. Radice."],
["La crise europeene et la premiere guerre mondiale", "Pierre Renouvin."],
["La Revolution Francaise", "G. Lefebvre."],
["The silent language", "Edward T. Hall."],
["Readings in the history of American agriculture", "edited by W.D. Rasmussen."], 
["The electrical double layer", "M.J. Sparnaay."],  
["Science of education and the psychology of the child", "J. Piaget."], 
["France between the Republics", "D.M. Pickles."], 
["The passing of the Irish Act of Union : a study in parliamentary politics", "G.C. Bolton."], 
["The Reformation in Germany", "J. Lortz"], 
["The Reformation in Germany", "J. Lortz"], 
["Construction surveying", "G.A. Scott."],
["Loudspeakers", "G.A. Briggs."],
["Toward global equilibrium : collected papers", "edited by Dennis L. Meadows and Donella H. Meadows."],
["Basics of reprography", "A. Tyrrell."],
["Mechanical seals", "Ehrhard Mayer."],
["Principles of organic mass spectrometry", "D.H. Williams and I. Howe."],
["Circuit theory with computer methods", "O. Wing."],
["Basic structural behaviour via models", "B. Hilson."],
["Games nations play : analyzing international politics", "J. Spanier."],
["A commentary on the collected poems of W.B. Yeats", "A.N. Jeffares."],
["Deformation processing", "W.A. Backofen."],
["Karst landforms", "M.M. Sweeting."],
["The Hall effect in metals and alloys", "C.M. Hurd."],
["Must the seas die?", "Colin Moorcraft."],
["Secondary metabolism in plants and animals", "M. Luckner."],
["Geology of Yorkshire", "P.F. Kendall and H.E. Wroot"],
["Money, wealth, and economic theory", "Boris P. Pesek, Thomas R. Saving."],
["Time series analysis : forecasting and control", "George E.P. Box and Gwilym M. Jenkins."],
["Chemotherapy and drug resistance in malaria", "W. Peters."],
["Ring-forming polymerizations", "R.J. Cotter and M. Matzner"],
["Haematology : rudimental, practical and clinical", "F. Nour-Eldin."],
["Industrial electrochemical processes", "edited by A.T. Kuhn."],
["Instrumentation in process control", "E.J. Wightman."],
["The statistical analysis of time series", "T.W. Anderson."],
["Fibres and fabrics of today", "H. Thomson."],
["Indexes and indexing", "R.L. Collison."],
["Fine powders : preparation, properties and uses", "C.R. Veale."],
["Molecules and life : historical essays on the interplay of chemistry and biology", "J.S. Fruton."],
["Highly dispersed aerosols", "N.A. Fuchs and A.G. Sutugin."],
["On site, 1921-1971", "Alan Jenkins."],
]

entry_list = []

def generate_time(start_Y = 0, end_Y = 0, amount = 0):
    time_array = []
    count = 0
    for y in range(start_Y, end_Y + 1):
        if count >= amount:
            break
        start_m = 1
        end_m = 12
        for m in range(start_m, end_m + 1):
            start_d = 1
            end_d = 1
            # big month 31 days
            if m == 2:
                # Leap month
                if y % 4 == 0:
                    if y % 100 == 0:
                        end_d = 28
                    else:
                        end_d = 29
                else:
                    end_d = 28
            elif m in [1,3,5,7,8,10,12]:
                end_d = 31
            else:
                end_d = 30
            d = start_d
            while d < end_d + 1:
                time_array.append(str(d) + "/" + str(m) + "/" + str(y))
                count += 1
                d += random.randint(0, 7)
    return time_array

f = open("database.txt","r+")
t_arr = generate_time(2015, 2019, 200)

book_count = []
for i in range(len(book_list)):
    book_count.append(0)

id_list = []
for i in range(9999):
    i = i + random.randint(1, 30)
    if i < 700:
        id_list.append("0")
    else:
        idn = str(i)
        for i in range(4 - len(idn)):
            idn = "0" + idn
            print(idn)
            id_list.append(idn)

for i in range(len(t_arr)):
    book = book_list[i % 70]
    entry = str(1 + i % 70) + "_" + str(book_count[i % 70]) + ",\"" + str(book[0]) + "\"," + str(book[1]) + "," + str(t_arr[i]) + "," + id_list[random.randint(0, len(id_list))] + ",\n"
    book_count[i % 70] = book_count[i % 70] + 1
    entry_list.append(entry)

f.writelines(entry_list)
f.close()
