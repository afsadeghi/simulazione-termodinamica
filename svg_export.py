Nel file svg_export.py, la funzione generate_and_save a volte produce file .svg 
non validi: capita che il contenuto salvato includa ancora i delimitatori markdown 
(tipo ```svg all'inizio e ``` alla fine) invece del solo codice SVG puro, e a volte 
il tag di chiusura </svg> manca del tutto, come se la risposta fosse stata tagliata 
a metà. Trova la causa e correggi il codice.
