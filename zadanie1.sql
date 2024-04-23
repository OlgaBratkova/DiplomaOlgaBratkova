/* # Ольга Браткова, 15-я когорта — Финальный проект. Инженер по тестированию плюс */

SELECT c.login, COUNT(o.*)
FROM "Couriers" c INNER JOIN "Orders" o ON o."courierId" = c.id
WHERE o."inDelivery" = true
GROUP BY c.login;