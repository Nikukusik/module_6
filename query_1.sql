SELECT s.name, AVG(scores.mark) from students s
JOIN scores ON s.id = scores.student_id
GROUP BY s.name
ORDER BY AVG(scores.mark) DESC
LIMIT 5;