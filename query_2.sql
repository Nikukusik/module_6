SELECT s.name, AVG(sc.mark), sub.name FROM scores sc
JOIN students s ON sc.student_id = s.id 
JOIN subjects sub ON sc.subject_id = sub.id 
WHERE sub.id = 1
ORDER BY AVG(sc.mark) DESC