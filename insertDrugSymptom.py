import psycopg2
import uuid


#class DrugSymptom(models.Model):
 #       id = models.CharField(primary_key=True, max_length=64, default=uuid.uui$
  #      drug = models.CharField(max_length=255, null=True, blank=True)
   #     symptom = models.CharField(max_length=255, null=True, blank=True)
    #    def __unicode__(self):
#                return smart_unicode(self.id)


#DB: django
#User: django
#Pass: As4g98HO8J

try:
	conn = psycopg2.connect("dbname='django' user='django' host='localhost' password='As4g98HO8J'")
	cur = conn.cursor()
except:
	print "failed connecting to database"

#Inserting

try:

	#Generate unique ID
	bidoof = str(uuid.uuid1())
	
	cur.execute("""
		INSERT INTO website_DrugSymptom
		(id, drug, symptom)
		VALUES
		('{}', 'Caffeine', 'Dehydration')
		""".format(bidoof))
	conn.commit()
except:
	print "If the following 6 lines of code above does not work, this should print"


#Now let's see our insert in action baby
try:
	cur.execute("""
		SELECT * FROM website_DrugSymptom
	""")
except:
	print "If the following 3 lines of code above does not work, this should print"

rows = cur.fetchall()
dict = {}

print "\n And here is the database \n"


#Prints the database
for row in rows:
	print row


