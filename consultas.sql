-- ============================================================
-- MÓDULO 1: CONSULTAS Y FILTRADO BÁSICO
-- ============================================================

-- Petición A: Clientes de México o Colombia
SELECT nombre, edad
FROM clientes
WHERE pais IN ('México', 'Colombia');

-- Petición B: Clientes de 25 a 40 años con más de 5 compras
SELECT *
FROM clientes
WHERE edad BETWEEN 25 AND 40
  AND compras_totales > 5;



-- ============================================================
-- MÓDULO 1: AGREGACIONES Y AGRUPAMIENTO (GROUP BY)
-- ============================================================

-- Petición C: Total y promedio de compras por país
-- (Escribe aquí tu consulta)


-- Petición D: Países con promedio de compras superior a 6
-- (Escribe aquí tu consulta)