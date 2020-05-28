create database if not exists Cine;

use Cine;


CREATE TABLE IF NOT EXISTS peliculas(
	
    id_pelicula int not null auto_increment,
    nombre varchar(50) not null,
    sipnosis varchar(255) not null,
    FLanzamiento date not null,
    
    primary key(id_pelicula)

)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS horarios(
	id_horario int not null auto_increment,
    dia date not null,
    hora varchar(10) not null,
    
    primary key (id_horario)
    

)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS asientos(
	id_asiento int not null auto_increment,
    fila varchar(2) not null,
    numero varchar(3) not null,
    
    primary key(id_asiento)


)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS salas(
	id_sala int not null auto_increment,
    numero_sala varchar(3) not null,
    tipo_sala varchar(20) not null,
    numero_asientos varchar(4),
	

    primary key(id_sala)
	
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS generos(

	id_genero int not null,
    genero varchar(30) not null,
    
    primary key(id_genero)

)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS usuarios(
	id_usuario int not null auto_increment,
    nombre varchar(50) not null,
    correo varchar(40) not null,
    tipo_usuario varchar(40) not null,
    usuario varchar(50) not null,
    pass varchar(50) not null,

	primary key(id_usuario)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS administradores(
	id_admin int not null auto_increment,
    nombre varchar(50) not null,
    correo varchar(40) not null,
    direccion varchar(80) not null,
    telefono varchar(11) not null,
    usuario varchar(50) not null,
    pass varchar(50) not null,

	primary key(id_admin)
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS peliculas_generos(

	id_genero int,
    id_pelicula int,
    
    primary key(id_pelicula,id_genero),
    constraint fk_id_pelicula foreign key(id_pelicula)
    references peliculas(id_pelicula)
    on delete cascade
    on update cascade,
    
    constraint fk_id_genero foreign key(id_genero)
    references generos(id_genero)
    on delete cascade
    on update cascade

)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS peliculas_salas(
	
    id_pelisala int not null auto_increment,
    id_pelicula int,
    id_sala int,
    
    primary key(id_pelisala),
    constraint fk_id_pelisala_peli foreign key(id_pelicula)
    references peliculas(id_pelicula)
    on delete cascade
    on update cascade,
    
	constraint fk_id_pelisala_sala foreign key(id_sala)
    references salas(id_sala)
    on delete cascade
    on update cascade



) ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS peliculas_horarios (
	id_pelihorario int not null auto_increment,
    id_pelicula int,
    id_horario int,
    precio float,
    
    primary key(id_pelihorario),
    constraint fk_id_peli foreign key(id_pelicula)
    references peliculas(id_pelicula)
    on delete cascade
    on update cascade,
    
	constraint fk_id_horario foreign key(id_horario)
    references horarios(id_horario)
    on delete cascade
    on update cascade
    
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS salas_asientos (
	id_sala_asiento int not null auto_increment,
    id_sala int,
    id_asiento int,
    estado_asiento varchar(20),
	disponibilidad_asiento varchar(20) not null,
    estado_sala varchar(20),
    
    primary key(id_sala_asiento),
    constraint fk_id_sala foreign key(id_sala)
    references salas(id_sala)
    on delete cascade
    on update cascade,
    
	constraint fk_id_asiento foreign key(id_asiento)
    references asientos(id_asiento)
    on delete cascade
    on update cascade
    
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS tickets (
	id_ticket int not null auto_increment,
	id_pelihorario int,
	id_sala_asiento int,
    
    primary key(id_ticket),
    constraint fk_id_pelihorario foreign key(id_pelihorario)
    references peliculas_horarios(id_pelihorario)
    on delete cascade
    on update cascade,
    
	constraint fk_id_sala_asiento foreign key(id_sala_asiento)
    references salas_asientos(id_sala_asiento)
    on delete cascade
    on update cascade
    
)ENGINE = INNODB;

CREATE TABLE IF NOT EXISTS compras (
	id_compra int not null auto_increment,
	id_ticket int,
	id_usuario int,
    
    primary key(id_compra),
    constraint fk_id_ticket foreign key(id_ticket)
    references tickets(id_ticket)
    on delete cascade
    on update cascade,
    
	constraint fk_id_usuario foreign key(id_usuario)
    references usuarios(id_usuario)
    on delete cascade
    on update cascade
    
)ENGINE = INNODB;

insert into compras(id_usuario,id_ticket) values ('1','1')