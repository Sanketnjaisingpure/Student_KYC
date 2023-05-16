Create database StudentInformation;
use StudentInformation;
create table Student (student_id bigint primary key ,
					  Student_Name varchar(255) , 
                      Department varchar(255) , 
                      Program varchar(255) , 
                      Year_of_Admission varchar(255));

insert into Student  (student_id , student_name , Department , Program , Year_of_Admission) values
(19010012289 , "Sanket N. Jaisingpure" , "B.E CSE" , "Regular" , "2019-20");

insert into Student  (student_id , student_name , Department , Program , Year_of_Admission) values
(19010012362 , "Nilay M. Owe" , "B.E CSE" , "Regular" , "2019-2020") , 
(19010012374 , "Yugesh S. Bansod" , "B.E CSE" , "Regular" , "2019-2020") , 
(19010012389 , "Swaraj A. Chimurkar" , "B.E CSE" , "Regular" , "2019-2020"), 
(19010052631, "Suraj P. Ingale" , "B.E IT" , "Regular" , "2019-2020") , 
(19010082296 , "Rahul S. Ghodeswar" , "B.E MECH" , "Regular" , "2019-2020") , 
(22010083252 , "Meghna S. Yelna" , "B.E MECH" , "Regular" , "2022-2023") ,
(22010083199 , "Payal B. Khandare" , "B.E MECH" , "Regular" , "2022-2023") ,
(22010083215 , "Tushar P. Alone" , "B.E MECH" , "Regular" , "2022-2023") ,
(22010053159 , "Anirudha R. Jawarkar" , "B.E CSE" , "Regular" , "2022-2023") 
;

select * from student;
create table non_registered_Student (student_id bigint primary key ,
					  Student_Name varchar(255) , 
                      Department varchar(255) , 
                      Program varchar(255) , 
                      Year_of_Admission varchar(255));

insert into Student  (student_id , student_name , Department , Program , Year_of_Admission) values
(21010053038 , "Tilak S. Bhusare" , "B.E IT" , "Regular" , "2021-2022") ,
(21010052965 , "Sarthak V. Akhare" , "B.E IT" , "Regular" , "2021-2022") ,
(21010112961 , "Abhishek V. Adhau" , "B.E EXTC" , "Regular" , "2021-2022") ,
(21010112939 , "Vivek S. Vaidya" , "B.E EXTC" , "Regular" , "2021-2022") ,
(21010053002 , "Sameer S. Panat" , "B.E IT" , "Regular" , "2021-2022") ;