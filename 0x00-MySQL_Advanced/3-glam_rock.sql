-- lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (IFNULL(split, '2022')  - formed) AS lifespan
FROM meta_bands
WHERE style = 'Glam rock'
ORDER BY lifespan DESC, band_name ASC;
