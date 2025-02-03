-- data_processing/dbt_transformations.sql
-- This is a sample DBT model SQL file for transforming raw telegram data

WITH raw AS (
    SELECT *
    FROM {{ ref('raw_telegram_data') }}
),
cleaned AS (
    SELECT DISTINCT
           id,
           TRIM(text) as text,
           date,
           channel
    FROM raw
    WHERE text IS NOT NULL
)
SELECT * FROM cleaned;

