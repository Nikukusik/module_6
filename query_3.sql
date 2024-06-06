SELECT AVG(sc.mark), sub.name FROM scores sc
JOIN subjects sub ON sc.subject_id = sub.id 
WHERE sub.id = 1