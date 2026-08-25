# Shortest_path_finder
Fundamentos de programación  project

If we where in a world without google map or satelite gps, finding the shortest path between two point would be a real problem to go through a city in a hurry, finding a route in a maze etc.

For this project, a map is represented as a matrix. Each position of the matrix represents a location that can either be accessible or blocked by an obstacle. The user provides a starting point and a destination point, and the program determines a possible path between them using loops, maybye files to have trajects historic.

The main problem is to find the shortest possible path from the starting point to the destination while avoiding obstacles and staying within the limits of the map.

This project is interesting because I don't have good orientation sense so I often take a route 2 times longer than the fastest when I don't use google maps of if I don't have connexion . 

Algorithm  

Create a map  
Ask for a starting position  
Ask for a destination    
Check if the positions are valid  
Find the right path through the matrix  
Stop when destination is found   
Show the path and its length  
Tell the user if no path exists  
