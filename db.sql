    CREATE TABLE Klanten (
    id int NOT NULL,
    voornaam varchar(255),
    achternaam varchar(255),
    email varchar(255),
    primary key (id)
    );
    CREATE TABLE Ticket (
    id int NOT NULL,
    klantid int,
    tijd time,
    vliegtuig int,
    primary key (id),
    foreign key (klantid) references Klanten(id)
    );
	CREATE TABLE Raspberry (
    id int NOT NULL,
    ip_adres varchar(15),
    mac_adres varchar(17),
    primary key (id)
    );
    CREATE TABLE Vliegtuig (
    id int NOT NULL,
    ticketnummer int,
    raspberry int,
    primary key (id),
    foreign key (ticketnummer) references Ticket(id),
    foreign key (raspberry) references Raspberry(id)
    );