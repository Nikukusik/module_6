SELECT sc.mark, g.name, sub.name FROM scores sc
JOIN students s ON sc.student_id = s.id 
JOIN groups g ON s.group_id = g.id
JOIN subjects sub ON sc.subject_id = sub.id 
WHERE g.id = 1 and sub.id = 1