import csv, sqlite3


def number_of_nodes():
    result = cur.execute('SELECT COUNT(*) FROM nodes')
    return result.fetchone()[0]


def number_of_ways():
    result = cur.execute('SELECT COUNT(*) FROM ways')
    return result.fetchone()[0]


def number_of_unique_users():
    result = cur.execute('SELECT COUNT(distinct(uid)) FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways)')
    return result.fetchone()[0]


def top_contributing_user():
    for row in cur.execute('SELECT e.user, COUNT(*) as num \
                            FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e \
                            GROUP BY e.user \
                            ORDER BY num DESC \
                            LIMIT 1'):
        return row


def biggest_religion():
    for row in cur.execute('SELECT nodes_tags.value, COUNT(*) as num ' \
                           'FROM nodes_tags \
                                JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value="place_of_worship") i \
                                ON nodes_tags.id=i.id \
                            WHERE nodes_tags.key="religion" \
                            GROUP BY nodes_tags.value \
                            ORDER BY num DESC\
                            LIMIT 1'):
        return row


def biggest_bank():
    for row in cur.execute("SELECT nodes_Tags.value, COUNT(*) as num \
                            FROM nodes_Tags \
                                JOIN (SELECT DISTINCT(id) FROM nodes_Tags WHERE value='bank') i \
                                ON nodes_Tags.id=i.id \
                            WHERE nodes_Tags.key='name' \
                            GROUP BY nodes_Tags.value \
                            ORDER BY num DESC \
                            LIMIT 1"):
        return row


def popular_amenity():
    for row in cur.execute('SELECT value, COUNT(*) as num \
                            FROM nodes_tags \
                            WHERE key="amenity" \
                            GROUP BY value \
                            ORDER BY num DESC \
                            LIMIT 1'):
        return row


def popular_cuisines():
    for row in cur.execute('SELECT nodes_tags.value, COUNT(*) as num \
                            FROM nodes_tags \
                                JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value="restaurant") i \
                                ON nodes_tags.id=i.id \
                            WHERE nodes_tags.key="cuisine" \
                            GROUP BY nodes_tags.value \
                            ORDER BY num DESC'):
        return row


if __name__ == '__main__':
    con = sqlite3.connect("denver_colorado_osm.db")
    cur = con.cursor()
    print "Number of Nodes: ", number_of_nodes()
    print "Number of Ways: ", number_of_ways()
    print "Number of Unique Users: ", number_of_unique_users()
    print "Top Contributing User: ", top_contributing_user()
    print "Biggest Religion: ", biggest_religion()
    print "Popular Amenity: ", popular_amenity()
    print "Biggest Bank: ", biggest_bank()
    print 'Popular Cuisine: ', popular_cuisines()
