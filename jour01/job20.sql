
mysql> SELECT COUNT(*) AS nombre_etudiants_mineurs FROM etudiant WHERE age < 18;
+--------------------------+
| nombre_etudiants_mineurs |
+--------------------------+
|                        1 |
+--------------------------+
1 row in set (0.00 sec)
