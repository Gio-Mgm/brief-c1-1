import mysql.connector

# Connection MySQL Connector
mydb = mysql.connector.connect(
	host="localhost",
	user="user",
	password="azerty",
	database="parcours_combattant"

)
mycursor = mydb.cursor()

# Create database query
cr_db_q = '''
	CREATE DATABASE IF NOT EXISTS parcours_combattant CHARACTER SET 'utf8'
	'''
mycursor.execute(cr_db_q)


# Create table Soldat query
cr_t_soldat_q = '''
	CREATE TABLE IF NOT EXISTS Soldat (
		reg_number CHAR(10)    NOT NULL PRIMARY KEY,
		grade      VARCHAR(25) NOT NULL,
		name       VARCHAR(25) NOT NULL,
		email      VARCHAR(25)
	)
'''
mycursor.execute(cr_t_soldat_q)


# Create table Difficulty query
cr_t_diff_q = '''
	CREATE TABLE IF NOT EXISTS Difficulty (
		id    CHAR(1) PRIMARY KEY,
		bonus FLOAT
	)
'''
mycursor.execute(cr_t_diff_q)

# Create table Obstacle query
cr_t_obstacle_q = '''
	CREATE TABLE IF NOT EXISTS Obstacle (
		name VARCHAR(25) NOT NULL PRIMARY KEY,
		diff CHAR(1)     NOT NULL,
		mini FLOAT,
		CONSTRAINT fk_diff_id FOREIGN KEY (diff) REFERENCES Difficulty(id)
	)
'''
mycursor.execute(cr_t_obstacle_q)

# Create table Passage query
cr_t_passage_q = '''
	CREATE TABLE IF NOT EXISTS Passage (
		id INTEGER AUTO_INCREMENT NOT NULL PRIMARY KEY,
		soldat_id      CHAR(10)    NOT NULL,
		instructeur_id CHAR(10)    NOT NULL,
		obstacle_id    VARCHAR(25) NOT NULL,
		passage_date   DATE        NOT NULL,
		passage_time   INTEGER     NOT NULL,
		note 		   INTEGER     NOT NULL,
		CONSTRAINT fk_soldat_id      FOREIGN KEY (soldat_id)      REFERENCES Soldat(reg_number),
		CONSTRAINT fk_instructeur_id FOREIGN KEY (instructeur_id) REFERENCES Soldat(reg_number),
		CONSTRAINT fk_obstacle_id    FOREIGN KEY (obstacle_id)    REFERENCES Obstacle(name)
	)
'''
mycursor.execute(cr_t_passage_q)


#-----------------------------------

# Insert into Soldat query
ins_in_soldat_q ='''
	INSERT INTO Soldat (reg_number, grade, name, email) VALUES (%s, %s, %s, %s)
'''
soldat_val = [
	("1234567890", "Adjudant-chef", "Lopez", "" ),
	("2345678901", "Sergent-chef", "Amand", "" ),
	("3456789012", "Caporal", "Biez", "" ),
]
 mycursor.executemany(ins_in_soldat_q, soldat_val)
 mydb.commit()

#-----------------------------------

# Insert into Difficulty query
ins_in_diff_q = '''
	INSERT INTO Difficulty (id, bonus) VALUES (%s, %s)
'''
diff_val = [
	("1", 1.5),
	("2", 2.0),
	("3", 2.5),
]

mycursor.executemany(ins_in_diff_q, diff_val)
mydb.commit()

#-----------------------------------

# Insert into Obstacle query
ins_in_obstacle_q = '''
		INSERT INTO Obstacle (name, diff, mini) VALUES (%s, %s, %s)
'''
obstacle_val = [
	("rampé", "1", 2.0),
	("mur", "2", 3.0),
	("fosse", "3", 4.0)
]

mycursor.executemany(ins_in_obstacle_q, obstacle_val)
mydb.commit()

#-----------------------------------

# Insert into Passage query
ins_in_passage_q = '''
	INSERT INTO Passage (soldat_id, instructeur_id, obstacle_id, passage_date, passage_time, note)
	VALUES (%s, %s, %s, %s, %s, %s)
'''
passage_val = [
	("1234567890", "3456789012", "mur", "2020-01-15", 24, 3),
	("2345678901", "3456789012", "mur", "2020-01-15", 22, 3),
	("3456789012", "1234567890", "mur", "2020-01-15", 25, 3)
]

mycursor.executemany(ins_in_passage_q, passage_val)
mydb.commit()

#----------------------------------

# Delete record

del_from_passage_q = '''
	DELETE FROM Passage WHERE instructeur_id = '1234567890'
'''
mycursor.execute(del_from_passage_q)
mydb.commit()

update_diff_q = '''
	UPDATE Difficulty SET bonus = 3.0 WHERE id = "3"
'''

mycursor.execute(update_diff_q)
mydb.commit()
