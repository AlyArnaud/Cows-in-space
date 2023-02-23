###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string
    
    File format: 
        Maggie,3
        Herman,7

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    print("Loading cows from file...")
        # inFile: file
    inFile = open(filename, 'r')
    # cow_dict: dictionary of cow: weight pairs
    cow_dict = {}
    for line in inFile:
        #line will equal "Maggie,3"
        #split line into dictionary cow:weight on ,
        cow_list = line.split(",")

        cow_dict[cow_list[0]] = cow_list[1]
        for cows in cow_dict: 
            cow_dict[cows] = cow_dict[cows].replace('\n', '')
    print(cow_dict)


    print("  ", len(cow_dict), "cows loaded.")
    return cow_dict

def get_heaviest(cow_dict):
    heaviest_cow = ""
    for cow in cow_dict: 
        if heaviest_cow == "":
            heaviest_cow = cow
        if cow_dict[cow] > cow_dict[heaviest_cow]:
             heaviest_cow = cow
    return(heaviest_cow)

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
   
    #output: outer list has all trips, inner list has cows taken per trip
    total_list = []
    trip_list = []
    total_weight = 0
    
    #make a copy of the dictionary
    local_cows = cows.copy()
    #Store cows in a sorted list heaviest to lightest
    ordered_cow_list = []
    for i in range(len(local_cows)): 
        heavy_cow = get_heaviest(local_cows)
        ordered_cow_list.append(heavy_cow)
        del(local_cows[heavy_cow])
        
    while len(ordered_cow_list) > 0:
        #Add heaviest cow to trip_list, check weight limit, 
        #if next heaviest cow is below remaining limit add else move to next cow
        for i in (range(len(ordered_cow_list))):
            next_cow = ordered_cow_list[i]
            if total_weight + int(cows[next_cow]) <= limit: 
                trip_list.append(next_cow)
                total_weight += int(cows[next_cow])
        
        #remove added cow(s) from sorted list
        for element in trip_list:
            ordered_cow_list.remove(element)
            
        #when trip full add to total_list & start again
        total_weight = 0
        total_list.append(trip_list)
        trip_list = []
    return total_list
                

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    #make a local copy of cows dict
    local_cows = cows.copy()
    #First get all partitions using get_partitions
    all_partitions = []
    good_flights = []
    for partition in get_partitions(local_cows):
        all_partitions.append(partition)
    
    #find weight of trip, if trip under weight limit add to possibles[]
    for total_trip in all_partitions: 
        trip_weights = []
        for flight in total_trip: 
            flight_weight = 0
            for cow in flight: 
                flight_weight += int(local_cows[cow])            
            trip_weights.append(flight_weight)
        for elem in trip_weights: 
            if elem > limit: 
                break
        else: 
            good_flights.append(total_trip)
            
    num_flights_required = 100000 #arbitrarily large number
    best_trip = []
    #find number of flights in trip, lowest is the winner
    for overall_trip in good_flights: 
        if len(overall_trip) < num_flights_required:
            num_flights_required = len(overall_trip)
            best_trip = overall_trip
    return best_trip

        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    cow_data_file = 'ps1_cow_data.txt'
    cows = load_cows(cow_data_file)
    

    # TODO: Your code here
    start = time.time()
    ## code to be timed
    greed = greedy_cow_transport(cows,limit=10)
    end = time.time()
    print("total greedy time = ", (end - start))
    print("total num trips: ", len(greed))

    start = time.time()
    ## code to be timed
    brute = brute_force_cow_transport(cows,limit=10)
    end = time.time()
    print("total brute force time = ", (end - start))
    print("total num trips: ", len(brute))


compare_cow_transport_algorithms()