create database teachit;
use teachit;

CREATE TABLE thread (
	rate INTEGER,
    upvote INTEGER,
    downvote INTEGER,
    author VARCHAR(20) NOT NULL,
    date_upload DATE NOT NULL,
    post_title VARCHAR(200) NOT NULL
);

INSERT into thread VALUES (69,68,1,'Mon Olarte','2023-11-11','Why is my balls blue?');
INSERT into thread VALUES (300,1,299,'Jan Micheal','2022-11-11','AITAH For murdering all of my family members? From top to bottom, death is inevitable?');
INSERT into thread VALUES (12,7,5,'Edwin Gumba','2023-10-11','My teacher in USERDES is kinda thick...');
INSERT into thread VALUES (16,15,1,'Morrissey Yu','2024-06-04','Assins Creed Is Cool...');

DELETE FROM thread;

SELECT * FROM thread;
SELECT * FROM thread ORDER BY date_upload DESC;

SET SQL_SAFE_UPDATES = 0;