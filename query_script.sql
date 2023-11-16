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

INSERT INTO thread (rate, upvote, downvote, author, date_upload, post_title)
VALUES
    (55, 50, 5, 'Alice Johnson', '2023-01-01', 'New study shows promising results in cancer treatment'),
    (14, 12, 2, 'Bob Smith', '2023-02-15', 'Breakthrough in neuroscience: Understanding brains complexity'),
    (17, 2, 15, 'Charlie Brown', '2023-03-10', 'Exploring climate change impact on biodiversity'),
    (110, 100, 10, 'David Davis', '2023-04-20', 'Quantum computing advancements revolutionize data processing'),
    (30, 5, 25, 'Eva Walker', '2023-05-05', 'AI models predict future patterns in global weather'),
    (33, 30, 3, 'Frank Wilson', '2023-06-18', 'Nanotechnology breakthrough for sustainable energy production'),
    (822, 800, 22, 'Grace Moore', '2023-07-22', 'Understanding genetic mutations linked to rare diseases'),
    (85, 80, 5, 'Hannah Campbell', '2023-08-09', 'Newly discovered exoplanets open possibilities for life beyond Earth'),
    (35, 5, 30, 'Isaac Mitchell', '2023-09-14', 'Discoveries in quantum mechanics challenge fundamental principles'),
    (128, 120, 8, 'Jack Carter', '2023-10-25', 'Innovative methods for carbon capture and storage'),
    (12, 2, 10, 'Kate Phillips', '2023-11-07', 'Advancements in artificial photosynthesis for renewable energy'),
    (64, 60, 4, 'Liam Evans', '2023-12-12', 'Exploring the microbiomes role in human health'),
    (45, 10, 35, 'Mia Gonzalez', '2021-01-20', 'Developments in gene editing technology: Implications and ethics'),
    (162, 150, 12, 'Noah Stewart', '2022-02-28', 'AI-driven drug discovery accelerates pharmaceutical research'),
    (29, 7, 22, 'Olivia Jenkins', '2022-03-05', 'Latest breakthrough in renewable energy technology');


DELETE FROM thread;

SELECT * FROM thread;
SELECT * FROM thread ORDER BY date_upload DESC;

SET SQL_SAFE_UPDATES = 0;