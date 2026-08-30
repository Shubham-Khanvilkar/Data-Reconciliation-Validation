-- Record counts
SELECT 'source_a' AS source_name, COUNT(*) AS record_count FROM source_a
UNION ALL
SELECT 'source_b', COUNT(*) FROM source_b;

-- Total value comparison
SELECT
    (SELECT SUM(total_value) FROM source_a) AS source_a_total,
    (SELECT SUM(total_value) FROM source_b) AS source_b_total,
    (SELECT SUM(total_value) FROM source_a) -
    (SELECT SUM(total_value) FROM source_b) AS net_variance;

-- Record-level value mismatches
SELECT
    a.account_id,
    a.total_value AS source_a_value,
    b.total_value AS source_b_value,
    a.total_value - b.total_value AS variance
FROM source_a a
JOIN source_b b ON a.account_id = b.account_id
WHERE ABS(a.total_value - b.total_value) > 1000
ORDER BY ABS(a.total_value - b.total_value) DESC;

-- Missing from Source B
SELECT a.account_id
FROM source_a a
LEFT JOIN source_b b ON a.account_id = b.account_id
WHERE b.account_id IS NULL;

-- Missing from Source A
SELECT b.account_id
FROM source_b b
LEFT JOIN source_a a ON a.account_id = b.account_id
WHERE a.account_id IS NULL;

-- Duplicate business keys
SELECT account_id, COUNT(*) AS occurrences
FROM source_a
GROUP BY account_id
HAVING COUNT(*) > 1;
