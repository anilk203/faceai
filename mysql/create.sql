
create table registrations(
    registration_id char(50),
	user_id char(50),
	user_name varchar(100),
	l_file_name varchar(100),
	l_file_path varchar(255),
	l_file_size_in_kb float(10,4),
	created_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
	primary key (user_id, user_name)
);

  
create table registration_params(
	user_id char(50),
	param_name varchar(255),
	param_value varchar(255),
	primary key (user_id, param_name)
); 

create table recognize_params(
    recongize_id char(50),
	file_name char(50),
	param_name varchar(255),
	param_value varchar(255)
);


