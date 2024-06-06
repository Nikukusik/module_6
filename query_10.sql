SELECT sc.subject_id, s.name, t.name FROM scores sc
JOIN students s ON sc.student_id = s.id
JOIN teachers t ON sc.teacher_id = t.id 
WHERE sc.teacher_id = 1 and sc.student_id = 1