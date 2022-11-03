DROP TABLE IF EXISTS Fish_And_Weather_Data;
CREATE TABLE Fish_And_Weather_Data AS
SELECT * FROM public."Cleaned_Fish_Data" as cfd 
INNER JOIN public."Weather_Data" USING ("Tournament_Day");