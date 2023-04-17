Implement step

* Draw a board with 9 squares
* Define state for the board
  * 9 squares
  * 2 players
  * 1 current player
  * 1 winner
  * 1 history of moves
* Define a function to calculate the winner
* Define a function to calculate the next player
* Draw a UI with moves and buttons
* Define a function to handle a click on a square
* Define a function to handle a click on a move

```md
* Behavior diagram  :
  * Click on a square
    * mark the square with the current player
    * calculate the winner
    * calculate the next player
    * add the move to the history

  * Click on a move
    * go to the move
    * calculate the winner
    * calculate the next player
    * add the move to the history
```

```md
* State diagram  :
  * Board
    * Squares [][]
      * Square
        * Player
        * Move
    
  * Players
    * Player
      * Mark
  
  * Moves []
    * Move
      * Player
      * Square
  * Current Move Index
    * Int
    
  * Game 
    * Winner
      * Player
    * Current player
      * Player


```

```md
* Component diagram : 
  * Player Info 
  * <Board>
      * <Square>
  * <Control>
      * <Button>

```