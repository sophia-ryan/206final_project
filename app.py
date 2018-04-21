# from flask import Flask, render_template, request, g
from flask import *
import sqlite3

DATABASE = 'restaurant.db'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/')
def index():
    return '''
            <img src="/static/guyfiere.png" />
            <h1> Diners Drive-Ins and Dives Finder! </h1>
            <h2> Click on a state/country to see resturants featured on Diners Drive-Ins and Dives </h2>
            <ul>
                <li><a href="alabama"> Restaurants in Alabama! </a><li>
                <li><a href="arizona"> Restaurants in Arizona! </a><li>
                <li><a href="california"> Restaurants in California! </a><li>
                <li><a href="colorado"> Restaurants in Colorado! </a><li>
                <li><a href="connecticut"> Restaurants in Connecticut! </a><li>
                <li><a href="dc"> Restaurants in DC! </a><li>
                <li><a href="florida"> Restaurants in Florida! </a><li>
                <li><a href="georgia"> Restaurants in Georgia! </a><li>
                <li><a href="hawaii"> Restaurants in Hawaii! </a><li>
                <li><a href="idaho"> Restaurants in Idaho! </a><li>
                <li><a href="illinois"> Restaurants in Illinois! </a><li>
                <li><a href="indiana"> Restaurants in Indiana! </a><li>
                <li><a href="iowa"> Restaurants in Iowa! </a><li>
                <li><a href="kansas"> Restaurants in Kansas! </a><li>
                <li><a href="kentucky"> Restaurants in Kentucky! </a><li>
                <li><a href="louisiana"> Restaurants in Louisiana! </a><li>
                <li><a href="maine"> Restaurants in Maine! </a><li>
                <li><a href="maryland"> Restaurants in Maryland! </a><li>
                <li><a href="massachusetts"> Restaurants in Massachusetts! </a><li>
                <li><a href="michigan"> Restaurants in Michigan! </a><li>
                <li><a href="minnesota"> Restaurants in Minnesota! </a><li>
                <li><a href="mississippi"> Restaurants in Mississippi! </a><li>
                <li><a href="missouri"> Restaurants in Missouri! </a><li>
                <li><a href="nebraska"> Restaurants in Nebraska! </a><li>
                <li><a href="nevada"> Restaurants in Nevada! </a><li>
                <li><a href="newhampshire"> Restaurants in New Hampshire! </a><li>
                <li><a href="newjersey"> Restaurants in New Jersey! </a><li>
                <li><a href="newmexico"> Restaurants in New Mexico! </a><li>
                <li><a href="newyork"> Restaurants in New York! </a><li>
                <li><a href="northcarolina"> Restaurants in North Carolina! </a><li>
                <li><a href="ohio"> Restaurants in Ohio! </a><li>
                <li><a href="oklahoma"> Restaurants in Oklahoma! </a><li>
                <li><a href="oregon"> Restaurants in Oregon! </a><li>
                <li><a href="pennsylvania"> Restaurants in Pennsylvania! </a><li>
                <li><a href="rhodeisland"> Restaurants in Rhode Island! </a><li>
                <li><a href="southcarolina"> Restaurants in South Carolina! </a><li>
                <li><a href="tennessee"> Restaurants in Tennessee! </a><li>
                <li><a href="texas"> Restaurants in Texas! </a><li>
                <li><a href="utah"> Restaurants in Utah! </a><li>
                <li><a href="virginia"> Restaurants in Virginia! </a><li>
                <li><a href="washington"> Restaurants in Washington! </a><li>
                <li><a href="westvirginia"> Restaurants in West Virginia! </a><li>
                <li><a href="wisconsin"> Restaurants in Wisconsin! </a><li>
                <li><a href="wyoming"> Restaurants in Wyoming! </a><li>
                <li><a href="bc"> Restaurants in BC - Canada! </a><li>
                <li><a href="ontario"> Restaurants in Ontario - Canada! </a><li>
                <li><a href="cuba"> Restaurants in Cuba! </a><li>
                <li><a href="italy"> Restaurants in Italy! </a><li>
                <li><a href="mexico"> Restaurants in Mexico! </a><li>
                <li><a href="spain"> Restaurants in Spain! </a><li>
                <li><a href="uk"> Restaurants in UK! </a><li>

            </ul>
    '''

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

@app.route('/alabama')
def alabama():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE (PhoneNumber LIKE '205-________') OR (PhoneNumber LIKE '334-________') OR (PhoneNumber LIKE '256-________') OR (PhoneNumber LIKE '938________') OR (PhoneNumber LIKE '251________') ")
    # rests = [dict(id=row[0],name=row[1], address=row[2], episode=row[3], phone_number = row[4]) for row in cur.fetchall()]
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Alabama'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/arizona')
def arizona():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE (PhoneNumber LIKE '480-________') OR (PhoneNumber LIKE '602-________') OR (PhoneNumber LIKE '928-________') OR (PhoneNumber LIKE '623-________') OR (PhoneNumber LIKE '520-________') ")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Arizona'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/california')
def california():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%CA%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'California'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/colorado')
def colorado():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE (PhoneNumber LIKE '719-________') OR (PhoneNumber LIKE '303-________') OR (PhoneNumber LIKE '720-________') OR (PhoneNumber LIKE '970________')")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Colorado'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/connecticut')
def connecticut():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%CT%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Connecticut'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/dc')
def dc():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%DC%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'DC'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/florida')
def flordia():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%FL%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Florida'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/georgia')
def georgia():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%GA%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Georgia'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/hawaii')
def hawaii():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%HI%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Hawaii'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/idaho')
def idaho():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%ID%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Idaho'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/illinois')
def illinois():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%IL%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Illinois'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/indiana')
def indiana():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%IN%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Indiana'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/iowa')
def iowa():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%IA%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Iowa'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/kansas')
def kansas():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%KS%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Kansas'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/kentucky')
def kentucky():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%KY%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Kentucky'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/louisiana')
def louisiana():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%LA%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Louisiana'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/maine')
def maine():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%ME%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Maine'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/maryland')
def maryland():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%MD%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Maryland'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/massachusetts')
def massachusetts():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%MA%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Massachusetts'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/michigan')
def michigan():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%MI%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Michigan'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/minnesota')
def minnesota():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%MN%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Minnesota'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/mississippi')
def mississippi():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%MS%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Mississippi'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/missouri')
def missouri():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%MO%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Missouri'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/nebraska')
def nebraska():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%NE%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Nebraska'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/nevada')
def nevada():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%NV%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Nevada'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/newhampshire')
def newhampshire():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%NH%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'New Hampshire'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/newjersey')
def newjersey():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%NJ%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'New Jersey'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/newmexico')
def newmexico():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%NM%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'New Mexico'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/newyork')
def newyork():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%NY%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'New York'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/northcarolina')
def northcarolina():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%NC%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'North Carolina'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/ohio')
def ohio():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%OH%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Ohio'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/oklahoma')
def oklahoma():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%OK%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Oklahoma'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/oregon')
def oregon():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%OR%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Oregon'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/pennsylvania')
def pennsylvania():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%PA%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Pennsylvania'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/rhodeisland')
def rhodeisland():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%RI%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Rhode Island'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/southcarolina')
def southcarolina():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%SC%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'South Carolina'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/tennessee')
def tennessee():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%TN%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Tennessee'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/texas')
def texas():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%TX%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Texas'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/utah')
def utah():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%UT%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Utah'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/virginia')
def virginia():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%VA%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Virginia'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/washington')
def washington():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%WA%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Washington'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/westvirginia')
def westvirginia():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%WV%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'West Virginia'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/wisconsin')
def wisconsin():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%WI%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Wisconsin'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/wyoming')
def wyoming():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%WY%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Wyoming'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/bc')
def bc():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%BC%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'BC - Canada'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/ontario')
def ontario():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%Ontario%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Ontario - Canada'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/cuba')
def cuba():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%Cuba%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Cuba'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/italy')
def italy():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%Italy%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Italy'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/mexico')
def mexico():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%Mexico%'")
    # might have an issue with New Mexico
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Mexico'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/spain')
def spain():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%Spain%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'Spain'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)

@app.route('/uk')
def uk():
    g.db = connect_db()
    cur = g.db.execute("SELECT Name, Address, EpisodeId, PhoneNumber FROM Restaurants WHERE Address LIKE '%UK%'")
    rests = [dict(name=row[0], address=row[1], episode=row[2], phone_number=row[3]) for row in cur.fetchall()]
    stateName = 'UK'
    g.db.close()
    return render_template('print_items.html', rests=rests, stateName=stateName)


if __name__ == '__main__':
    print('starting Flask app', app.name)
    app.run(debug=True)
