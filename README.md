# proyecto-final-arqui
-- El documento de diseño es system_designA00824494.pdf

## Endpoints:
- /recommend - POST: Espera los atributos `uid` (int) y `rating` (bool), aunque `rating` es opcional y su valor default es `False`. Responde con una lista de strings bajo el atributo `recommended movies` (list<str>).
- /login - POST: Espera los atributos `email` (str) y `password` (str). Responde con el atributo `message` con valor `auth` (str) y otro atributo llamado `uid` (int), que es el id del usuario dentro de la base de datos de usuarios.  
- /signup - POST: Espera los atributos `email` (str), `password` (str) y `preferences` (str), donde preferences es una lista separada por comas de los géneros preferidos del usuario capitalizados. Retorna el atributo `message` con valor `user succesfully registered` cuando la operación procedió con éxito.