CREATE DATABASE OLA;
USE OLA;
-- Retrieve all successful bookings
select * from bookings
WHERE Booking_Status = 'Success' ;
-- Find the average ride distance for each vehicle type 
CREATE VIEW ride_distance_for_each_vehichle As
SELECT Vehicle_Type , AVG(Ride_Distance)
as avg_distance FROM bookings
GROUP BY Vehicle_Type;
-- Find the average ride distance for each vehichle
select * from ride_distance_for_each_vehichle;
-- Get the total number of cancelled rides by customers
CREATE VIEW cancelled_rides_by_customer As
SELECT COUNT(*) FROM bookings
WHERE Booking_Status = 'canceled by customer' ;
select * from  cancelled_rides_by_customer;
-- 	List the top 5 customers who booked the highest number of rides
CREATE VIEW Top_5_Customers As
SELECT Customer_ID , COUNT(Booking_ID) as total_rides
FROM bookings
GROUP BY Customer_ID
ORDER BY total_rides DESC LIMIT 5;
SELECT * FROM Top_5_Customers;
-- Get the number of rides canceled by drivers due to personal or car-related issue
Create view rides_canceled_by_drivers As
SELECT COUNT(*) FROM bookings
WHERE Canceled_Rides_by_Driver = 'Personal and car related issue ' ;
-- Find the max and min driver ratings for Prime sedan 
Select MAX(Driver_Ratings) as max_rating ,
MIN(Driver_Ratings) as min_rating 
FROM bookings WHERE Vehicle_Type = 'Prime Sedan' ;
-- Retrieve all rides where payment was made using UPI
CREATE VIEW Upi_Payment As 
SELECT * FROM bookings 
WHERE Payment_Method = 'UPI' ;
-- Find the average customer rating per vehicle type 
CREATE VIEW Avg_c_r as
SELECT Vehicle_Type , AVG(Customer_Rating) as avg_customers_rating
FROM bookings 
GROUP BY Vehicle_Type ;

-- Calculate the total booking value of rides completed successfully 
CREATE VIEW total_successfull_ride_value As 
SELECT SUM(Booking_Value) as total_succeeded_rides 
FROM bookings 
WHERE Booking_Status = 'success' ;

-- List all incomplete rides along with the reason ;
CREATE VIEW Incomplete_ride_reason As 
SELECT Booking_ID , Incomplete_Rides_Reason 
from bookings 
where Incomplete_Rides = 'Yes' ;


