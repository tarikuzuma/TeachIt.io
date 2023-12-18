create database teachit;
use teachit;

CREATE TABLE thread (
	rate INTEGER,
    upvote INTEGER,
    downvote INTEGER,
    author VARCHAR(20) NOT NULL,
    date_upload DATETIME NOT NULL,
    post_title VARCHAR(200) NOT NULL
);

INSERT INTO thread (rate, upvote, downvote, author, date_upload, post_title)
VALUES
    (55, 50, 5, 'Alice Johnson', '2023-01-01 12:30:00', 'New study shows promising results in cancer treatment'),
    (14, 12, 2, 'Bob Smith', '2023-02-15 09:45:00', 'Breakthrough in neuroscience: Understanding brains complexity'),
    (17, 2, 15, 'Charlie Brown', '2023-03-10 18:20:00', 'Exploring climate change impact on biodiversity'),
    (110, 100, 10, 'David Davis', '2023-04-20 15:10:00', 'Quantum computing advancements revolutionize data processing'),
    (30, 5, 25, 'Eva Walker', '2023-05-05 11:55:00', 'AI models predict future patterns in global weather'),
    (33, 30, 3, 'Frank Wilson', '2023-06-18 14:40:00', 'Nanotechnology breakthrough for sustainable energy production'),
    (822, 800, 22, 'Grace Moore', '2023-07-22 08:00:00', 'Understanding genetic mutations linked to rare diseases'),
    (85, 80, 5, 'Hannah Campbell', '2023-08-09 13:20:00', 'Newly discovered exoplanets open possibilities for life beyond Earth'),
    (35, 5, 30, 'Isaac Mitchell', '2023-09-14 16:05:00', 'Discoveries in quantum mechanics challenge fundamental principles'),
    (128, 120, 8, 'Jack Carter', '2023-10-25 10:10:00', 'Innovative methods for carbon capture and storage'),
    (12, 2, 10, 'Kate Phillips', '2023-11-07 07:30:00', 'Advancements in artificial photosynthesis for renewable energy'),
    (64, 60, 4, 'Liam Evans', '2023-12-12 19:15:00', 'Exploring the microbiomes role in human health'),
    (45, 10, 35, 'Mia Gonzalez', '2021-01-20 20:45:00', 'Developments in gene editing technology: Implications and ethics'),
    (162, 150, 12, 'Noah Stewart', '2022-02-28 11:25:00', 'AI-driven drug discovery accelerates pharmaceutical research'),
    (29, 7, 22, 'Olivia Jenkins', '2022-03-05 16:50:00', 'Latest breakthrough in renewable energy technology');


/*LIMIT TESTING*/
INSERT into thread VALUES (169,168,1,'Mon Olarte','2023-12-11','Why is the sky blue?');
Insert into thread Values (110, 100, 10, 'Liam Evans', '2023-12-12', 'Exploring the microbiomes role in human health');
Insert into thread Values (10000, 10000, 0, 'Liam Evans', '2022-12-12', 'Exploring the microbiomes role in human health');

DELETE FROM thread;

DELETE FROM thread
WHERE author = 'Liam Evans'
;

DROP table thread;

SELECT * FROM thread;
SELECT * FROM thread ORDER BY date_upload DESC;

SET SQL_SAFE_UPDATES = 0;