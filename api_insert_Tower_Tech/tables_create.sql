create database towerTech;

use towerTech;

create table tbCapturaDeDados(
    idCapturaDeDados int,
    fkComputadores int,
    primary key (idCapturaDeDados, fkComputadores),
    usuarioMaq varchar(45),
    porcentual_CPU decimal(5,2),
    porcentual_RAM decimal(5,2),
    porcentual_DISCO decimal(5,2),
    internet varchar(13),
    datahora datetime
);

select * from tbCapturaDeDados;


truncate table tbCapturaDeDados;
drop table tbCapturaDeDados;