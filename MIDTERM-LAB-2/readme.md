# Algorithm Approach
For the routing logic, I used Dijkstra’s Algorithm. Since this activity deals with different "weights" like distance, time, and fuel, Dijkstra’s is the most efficient way to find the absolute shortest path from point A to point B. It works by checking all possible connections and picking the one with the lowest total cost. Because all the values in the data table are positive, the algorithm always finds the most optimal route without any issues.


# Challenges Faced
Bidirectional Routes: My first version treated some roads as one-way streets. This caused the algorithm to take a huge detour just to go back to a nearby city. I had to fix the data to make sure every route can be traveled both ways.

Cleaning Up the UI: Since I made the roads two-way, the map labels were overlapping and hard to read. I added a logic check to merge these into a single clean label whenever the values for both directions are the same.