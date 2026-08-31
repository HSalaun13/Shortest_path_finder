# Shortest_path_finder

If we where in a world without google map or satelite gps, finding the shortest path between two point would be a real problem to go through a city in a hurry, finding a route in a maze etc.

For this project, a map is represented as a matrix. Each position of the matrix represents a location that can either be accessible or blocked by an obstacle. The obstacle can be buildings, water flow, construction, etc. The user provides a starting point and a destination point, and the program determines a possible path between them using loops, files to have trajects historic, a map randomiser, .

The main problem is to find the shortest possible path from the starting point to the destination while avoiding obstacles and staying within the limits of the map.

This project is interesting because I don't have good orientation sense so I often take a route 2 times longer than the fastest when I don't use google maps of if I don't have connexion, and also i want to do like a what if google maps and all geolocalisation were just at their begining 

Algorithm  
1.Create a map  
2.Ask for a starting position  
3.Ask for a destination    
4.Check if the positions are valid  
5.Find the right path through the matrix  
6.Stop when destination is found   
7.Show the path and its length  
8.Tell the user if no path exists  
