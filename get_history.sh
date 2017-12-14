#!/bin/bash

# Locate the history file in your profile, and copy it to the same folder as this script.
# On Mac: ~/Library/Application\ Support/Google/Chrome/Default/History
# On Windows: C:\Users\YOUR USER NAME\AppData\Local\Google\Chrome\User Data\Default\History

sqlite3 History <<!
.headers on
.mode csv
.output out.csv
select datetime(last_visit_time/1000000-11644473600,'unixepoch') as 'date',url from  urls order by last_visit_time desc;
!
