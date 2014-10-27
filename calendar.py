from icalendar import Calendar, Event, vText, vCalAddress
from datetime import datetime
from pytz import timezone

tz = timezone('Europe/Berlin')

# Create Calendar
cal = Calendar()

# Setup Calendar Header
cal.add('prodid', '-//pystada-calendar//pystada.github.io//')
cal.add('version', '2.0')

# PyStaDa
event = Event()
event['uid'] = '20140212T193000/0000001@pystada.github.io'
event.add('summary', 'Python Stammtisch Darmstadt')
desc = vText('Öffentlicher Stammtisch zur Programmiersprache Python')
event.add('description', desc)
event.add('dtstart', datetime(2014, 1, 29, 19, 30, 0, tzinfo=tz))
event.add('dtend', datetime(2014, 1, 29, 22, 00, 0, tzinfo=tz))
event.add('dtstamp', datetime(2014, 1, 29, 16, 00, 0, tzinfo=tz))
event.add('rrule', {'freq': 'weekly', 'interval': 2})
event.add('location', 'Trollhöhle, Wilhelm-Leuschner-Straße 36, 64293 Darmstadt')
event.add('url', 'https://pystada.github.io')
organizer = vCalAddress('mailto:pystada@lists.chaos-darmstadt.de')
event.add('organizer', organizer)

# Gegentermine PyUGRM
event.add('exdate', datetime(2014, 5, 15, 19, 30, 0, tzinfo=tz))
event.add('exdate', datetime(2014, 7, 16, 19, 30, 0, tzinfo=tz))
event.add('exdate', datetime(2014, 9, 18, 19, 30, 0, tzinfo=tz))
event.add('exdate', datetime(2014, 11, 12, 19, 30, 0, tzinfo=tz))
event.add('exdate', datetime(2015, 1, 15, 19, 30, 0, tzinfo=tz))
event.add('exdate', datetime(2015, 3, 11, 19, 30, 0, tzinfo=tz))
event.add('exdate', datetime(2015, 5, 14, 19, 30, 0, tzinfo=tz))

cal.add_component(event)

print(cal.to_ical().decode('utf-8'))
