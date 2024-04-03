# Documentation for `FED UP CUSTOS.py`

## Overview
`FED UP CUSTOS.py` is a Python simulation program designed for the AQA AS Summer 2024 examination. It simulates a queue system in a store with multiple tills, tracking customer arrivals, service times, and queue lengths. The program also includes functionality to simulate customers leaving the queue if they have been waiting too long (getting "fed up").

## Constants
- `BLANK`: Placeholder for an empty buyer ID.
- `MAX_Q_SIZE`: Maximum size of the queue.
- `MAX_TILLS`: Maximum number of tills available.
- `MAX_TIME`: Maximum simulation time.
- `TILL_SPEED`: Number of items a till can process per time unit.
- `TIME_IDLE`, `TIME_BUSY`, `TIME_SERVING`: Indices for tracking till states.
- `ARRIVAL_TIME`, `ITEMS`: Indices for customer data.
- `MAX_Q_LENGTH`, `MAX_WAIT`, `TOTAL_WAIT`, `TOTAL_Q`, `TOTAL_Q_OCCURRENCE`, `TOTAL_NO_WAIT`: Indices for statistics tracking.

## Classes
### `Q_Node`
Represents a node in the queue with attributes for buyer ID, waiting time, and items in the basket.

## Functions
### `ResetDataStructures()`
Initializes and returns the statistics, tills, and buyer queue data structures.

### `ChangeSettings()`
Allows the user to change simulation settings such as simulation time, number of tills, and the maximum waiting time before customers get fed up.

### `ReadInSimulationData()`
Reads customer arrival times and item counts from a file named `SimulationData.txt`.

### `OutputHeading()`
Prints the heading for the simulation output.

### `BuyerJoinsQ(Data, BuyerQ, QLength, BuyerNumber)`
Adds a buyer to the queue.

### `BuyerArrives(Data, BuyerQ, QLength, BuyerNumber, NoOfTills, Stats)`
Handles the arrival of a buyer by adding them to the queue and updating relevant statistics.

### `FindFreeTill(Tills, NoOfTills)`
Finds an available till.

### `ServeBuyer(BuyerQ, QLength)`
Processes the first buyer in the queue, serving them and removing them from the queue.

### `UpdateStats(Stats, WaitingTime)`
Updates the simulation statistics based on the waiting time of the last served customer.

### `CalculateServingTime(Tills, ThisTill, NoOfItems)`
Calculates and sets the serving time for a till based on the number of items.

### `IncrementTimeWaiting(BuyerQ, QLength, fut)`
Increments the waiting time for each buyer in the queue and removes buyers who have exceeded the fed-up threshold.

### `UpdateTills(Tills, NoOfTills)`
Updates the state of each till for a time unit.

### `OutputTillAndQueueStates(Tills, NoOfTills, BuyerQ, QLength)`
Prints the current state of tills and the queue.

### `Serving(Tills, NoOfTills, BuyerQ, QLength, Stats, fut)`
Processes serving buyers at available tills and updates the queue and tills accordingly.

### `TillsBusy(Tills, NoOfTills)`
Checks if any tills are currently serving a customer.

### `OutputStats(Stats, BuyerNumber, SimulationTime)`
Prints the final statistics of the simulation.

### `QueueSimulator()`
The main function that runs the queue simulation.

## Execution
To run the simulation, execute the script. The user will be prompted to adjust settings before the simulation begins. After completion, the simulation statistics are displayed.

## File Dependencies
- Requires a file named `SimulationData.txt` for input data.

## Notes
- The simulation includes handling for customers leaving the queue if they wait too long, a feature controlled by user input at the start of the simulation.
- The program is designed for educational purposes as part of the AQA AS Summer 2024 examination preparation.