from models import Publishers, Advertisements
from app import db

p1 = Publishers(username='admin')
p2 = Publishers(username='user')
p3 = Publishers(username='guest')
a1 = Advertisements(title='Adv 1', description='Descr 1', publisher_id=1)
a2 = Advertisements(title='Adv 2', description='Descr 2', publisher_id=2)
a3 = Advertisements(title='Adv 3', description='Descr 3', publisher_id=3)

db.session.add(p1)
db.session.add(p2)
db.session.add(p3)
db.session.add(a1)
db.session.add(a2)
db.session.add(a3)

db.session.commit()
