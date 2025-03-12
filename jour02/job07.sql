
mysql> CREATE DATABASE entreprise;
Query OK, 1 row affected (0.01 sec)

mysql> USE entreprise;
Database changed
mysql> CREATE TABLE employe (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255),
    ->     prenom VARCHAR(255),
    ->     salaire DECIMAL(10, 2),
    ->     id_service INT
    -> );
Query OK, 0 rows affected (0.03 sec)

mysql> CREATE TABLE service (
    ->     id INT AUTO_INCREMENT PRIMARY KEY,
    ->     nom VARCHAR(255)
    -> );
Query OK, 0 rows affected (0.05 sec)

mysql> INSERT INTO service (nom) VALUES ('Développement');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO service (nom) VALUES ('Marketing');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO service (nom) VALUES ('RH');
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Dupont', 'Jean', 3500, 1);
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Martin', 'Lucie', 2800, 2);
Query OK, 1 row affected (0.01 sec)

mysql> INSERT INTO employe (nom, prenom, salaire, id_service) VALUES ('Durand', 'Pierre', 4000, 3);
Query OK, 1 row affected (0.00 sec)

mysql> SELECT * FROM employe WHERE salaire > 3000;
+----+--------+--------+---------+------------+
| id | nom    | prenom | salaire | id_service |
+----+--------+--------+---------+------------+
|  1 | Dupont | Jean   | 3500.00 |          1 |
|  3 | Durand | Pierre | 4000.00 |          3 |
+----+--------+--------+---------+------------+
2 rows in set (0.01 sec)

mysql> SELECT e.nom, e.prenom, s.nom AS service
    -> FROM employe e
    -> JOIN service s ON e.id_service = s.id;
+--------+--------+---------------+
| nom    | prenom | service       |
+--------+--------+---------------+
| Dupont | Jean   | Développement |
| Martin | Lucie  | Marketing     |
| Durand | Pierre | RH            |
+--------+--------+---------------+
3 rows in set (0.00 sec)

mysql>

