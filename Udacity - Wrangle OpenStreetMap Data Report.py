#!/usr/bin/env python
# coding: utf-8

# # Wrangle OpenStreetMap Data
# 
# **Akash Patel**

# ## Map Area

# The area I chose for this project to analyze is Denver which is the capital city of Colorado.
# 
# OpenStreetMap coordinates:  
# 
# - **Longitude:** -105.2298000, -104.4800000
# - **Latitude:** 39.5956000, 39.9329000

# ## Identifying and Cleaning Problems in the Map

# 1. I first created a sample file (**Sample_data.py**) using script provided by Udacity, a sample containing every 500the element from the original file (**denver_colorado_osm**)
# 2. To get the unique tags, I parsed through the dataset by using count_tags function (**mapparser.py**)
# 
#     > <font color=blue>
#         {'bounds': 1,
#          'member': 44664,
#          'meta': 1,
#          'nd': 3526619,
#          'node': 3132214,
#          'note': 1,
#          'osm': 1,
#          'relation': 1725,
#         'tag': 1842489,
#          'way': 396041}</font>
#          
#      
# 3. I then checked "k" value for each < tag > and see if there are any potential problems. (**process_map.py**)
# 
#    > <font color=blue>{'lower': 2509, 'lower_colon': 1149, 'other': 41, 'problemchars': 0}</font>
#     
# 4. I first analyzed the sample data (**audit.py**) to view unsual street names. I found few street names to be inconsistency and abbreviated. (such as Ln and Ln., blvd, blvd.,blvd,)
# 5. I then used **data.py** and **schema.py** on original data to clean the street names and convert XML to CSV format.

# ## Data Overview

# #### File Sizes:
# - denver_colorado_osm: 714mb
# - sample_osm:1.4mb
# - nodes.csv: 270mb
# - nodes_tags.csv: 16.2mb
# - ways.csv: 24.7mb
# - ways_nodes.csv: 86mb
# - ways_tags.csv: 46.4mb
# - denver_colorado_osm.db: 497.2mb

# ## Importing to Database

# Finally, after cleaninng the data and converting from XML to CSV, I was ready to import the files to SQL Database using a given schema.(**SQL_DB.py**)

# ### Inspecting Database

# After importing the files to database, I was ready to run queries and inspect the database. (**DB_Query.py**)

# #### Number of Nodes:
# 
# > SELECT COUNT(*) FROM nodes
# 
# Output: <font color=blue>3132214</font>  

# #### Number of Ways:
# > SELECT COUNT(*) FROM ways
# 
# Output: <font color=blue>396041</font> 

# #### Number of Unique Users:
# > SELECT COUNT(distinct(uid)) FROM (SELECT uid FROM nodes UNION ALL SELECT uid FROM ways)
# 
# Output: <font color=blue>1467</font> 

# #### Top Contributing User:
# >SELECT e.user, COUNT(*) as num \
#                             FROM (SELECT user FROM nodes UNION ALL SELECT user FROM ways) e \
#                             GROUP BY e.user \
#                             ORDER BY num DESC \
#                             LIMIT 1 
#                             
# Output: <font color=blue>chachafish</font> 

# #### Biggest Religion:
# > SELECT nodes_tags.value, COUNT(*) as num ' \
#                            'FROM nodes_tags \
#                                 JOIN (SELECT DISTINCT(id) FROM   nodes_tags WHERE value="place_of_worship") i \
#                                 ON nodes_tags.id=i.id \
#                             WHERE nodes_tags.key="religion" \
#                             GROUP BY nodes_tags.value \
#                             ORDER BY num DESC\
#                             LIMIT 1
#                             
# Output: <font color=blue>Christian</font>  

# #### Popular Amenity:
# > SELECT nodes_Tags.value, COUNT(*) as num \
#                             FROM nodes_Tags \
#                                 JOIN (SELECT DISTINCT(id) FROM nodes_Tags WHERE value='bank') i \
#                                 ON nodes_Tags.id=i.id \
#                             WHERE nodes_Tags.key='name' \
#                             GROUP BY nodes_Tags.value \
#                             ORDER BY num DESC \
#                             LIMIT 1
#                             
# Output: <font color=blue>Restaurant</font>                            

# #### Biggest Bank:
# > SELECT value, COUNT(*) as num \
#                             FROM nodes_tags \
#                             WHERE key="amenity" \
#                             GROUP BY value \
#                             ORDER BY num DESC \
#                             LIMIT 1
# 
# Output: <font color=blue>Chase</font>                           
#                             

# #### Popular Cuisine:
# > SELECT nodes_tags.value, COUNT(*) as num \
#                             FROM nodes_tags \
#                                 JOIN (SELECT DISTINCT(id) FROM nodes_tags WHERE value="restaurant") i \
#                                 ON nodes_tags.id=i.id \
#                             WHERE nodes_tags.key="cuisine" \
#                             GROUP BY nodes_tags.value \
#                             ORDER BY num DESC
#                             
# Output: <font color=blue>American</font>  

# ## Conclusion

# The datafile that I downloaded from OpenStreetMap was quite large with few inconsistencies in the format and abbreviation, but in general, the data was cleaner than what I had expected to easily complete this project. 
# This project was good exercise in learning data gathering, auditing, cleaninig, and analysis. It was also a good experience to learn the basis of creating and importing data with a SQL database.
# 
# Suggestions for improvements for data in openstreetmap is to develop scripts to maintan, clean and most up-to-date data regularly for future users. 

# In[ ]:




