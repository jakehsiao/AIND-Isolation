"""This file contains all the classes you must complete for this project.

You can use the test cases in agent_test.py to help during development, and
augment the test suite with your own test cases to further test your code.

You must test your agent's strength against a set of agents with known
relative strength using tournament.py and include the results in your report.
"""
import random

TESTING = False  # change this while not testing


class Timeout(Exception):
    """Subclass base exception for code clarity."""
    pass


def custom_score(game, player):
    """Calculate the heuristic value of a game state from the point of view
    of the given player.

    Note: this function should be called from within a Player instance as
    `self.score()` -- you should not need to call this function directly.

    Parameters
    ----------
    game : `isolation.Board`
        An instance of `isolation.Board` encoding the current state of the
        game (e.g., player locations and blocked cells).

    player : object
        A player instance in the current game (i.e., an object corresponding to
        one of the player objects `game.__player_1__` or `game.__player_2__`.)

    Returns
    -------
    float
        The heuristic value of the current game state to the specified player.
    """

    # TODO: change this function!
    #  raise NotImplementedError
    if game.is_loser(player):
        return float("-inf")

    if game.is_winner(player):
        return float("inf")

    own_moves = len(game.get_legal_moves(player))
    opp_moves = len(game.get_legal_moves(game.get_opponent(player)))

    return float(own_moves**2/(1+opp_moves))  # TODO:make it parameteristic


class CustomPlayer:
    """Game-playing agent that chooses a move using your evaluation function
    and a depth-limited minimax algorithm with alpha-beta pruning. You must
    finish and test this player to make sure it properly uses minimax and
    alpha-beta to return a good move before the search time limit expires.

    Parameters
    ----------
    search_depth : int (optional)
        A strictly positive integer (i.e., 1, 2, 3,...) for the number of
        layers in the game tree to explore for fixed-depth search. (i.e., a
        depth of one (1) would only explore the immediate sucessors of the
        current state.)

    score_fn : callable (optional)
        A function to use for heuristic evaluation of game states.

    iterative : boolean (optional)
        Flag indicating whether to perform fixed-depth search (False) or
        iterative deepening search (True).

    method : {'minimax', 'alphabeta'} (optional)
        The name of the search method to use in get_move().

    timeout : float (optional)
        Time remaining (in milliseconds) when search is aborted. Should be a
        positive value large enough to allow the function to return before the
        timer expires.
    """

    def __init__(self, search_depth=3, score_fn=custom_score,
                 iterative=True, method='minimax', timeout=10.):
        self.search_depth = search_depth
        self.iterative = iterative
        self.score = score_fn
        if method == "minimax":
            self.method = self.minimax
        else:
            self.method = self.alphabeta
        self.time_left = None
        self.TIMER_THRESHOLD = timeout

        global TESTING
        self.testing = TESTING

    def get_move(self, game, legal_moves, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.

        This function must perform iterative deepening if self.iterative=True,
        and it must use the search method (minimax or alphabeta) corresponding
        to the self.method value.

        **********************************************************************
        NOTE: If time_left < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************

        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).

        legal_moves : list<(int, int)>
            A list containing legal moves. Moves are encoded as tuples of pairs
            of ints defining the next (row, col) for the agent to occupy.

        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.

        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """

        self.time_left = time_left

        if len(legal_moves) == 0:  # if no legal moves
            return -1, -1

        next_move = random.choice(legal_moves)  # init the next move with random choice

        # TODO: finish this function!

        # Perform any required initializations, including selecting an initial
        # move from the game board (i.e., an opening book), or returning
        # immediately if there are no legal moves

        try:
            # The search method call (alpha beta or minimax) should happen in
            # here in order to avoid timeout. The try/except block will
            # automatically catch the exception raised by the search method
            # when the timer gets close to expiring
            if self.iterative:
                max_depth = self.search_depth
                for d in range(1, max_depth + 1):  # TODO:verify the min depth
                    self.search_depth = d

                    if self.testing:
                        print("in ID searching:", self.search_depth)
                        print("START SEARCHING")

                    next_move = self.method(game, depth=0)
            else:
                next_move = self.method(game, depth=0)

        except Timeout:
            # Handle any actions required at timeout, if necessary
            return next_move

        # Return the best move from the last completed search iteration
        return next_move[1]

    def minimax(self, game, depth, maximizing_player=True):
        """Implement the minimax search algorithm as described in the lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # raise NotImplementedError


        # get the possible legal moves
        legal_moves = game.get_legal_moves(self)

        if self.testing: print("depth:%d, legal moves:%d" % (depth, len(legal_moves)))

        # return the score and the none move if reaches the max depth of no more legal moves
        if depth > self.search_depth or len(legal_moves) == 0:
            return self.score(game, self), (-1, -1)

        # init the best value of min/max node
        if maximizing_player:
            best_value = [float("-inf"), 0]
        else:
            best_value = [float("inf"), 0]

        # start searching
        for move in legal_moves:
            new_game = game.forecast_move(move)
            old_value = best_value[0]
            if maximizing_player:
                best_value[0] = max(best_value[0], self.minimax(new_game, depth + 1, False)[0])
            else:
                best_value[0] = min(best_value[0], self.minimax(new_game, depth + 1, True)[0])
            if best_value[0] != old_value:
                best_value[1] = move

        return best_value

    def alphabeta(self, game, depth, alpha=float("-inf"), beta=float("inf"), maximizing_player=True):
        """Implement minimax search with alpha-beta pruning as described in the
        lectures.

        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state

        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting

        alpha : float
            Alpha limits the lower bound of search on minimizing layers

        beta : float
            Beta limits the upper bound of search on maximizing layers

        maximizing_player : bool
            Flag indicating whether the current search depth corresponds to a
            maximizing layer (True) or a minimizing layer (False)

        Returns
        -------
        float
            The score for the current search branch

        tuple(int, int)
            The best move for the current branch; (-1, -1) for no legal moves

        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project unit tests; you cannot call any other
                evaluation function directly.
        """
        if self.time_left() < self.TIMER_THRESHOLD:
            raise Timeout()

        # get the legal moves
        legal_moves = game.get_legal_moves(self)

        if self.testing: print("alpha:%f, beta:%f, depth:%f, legal moves:%s" % (alpha, beta, depth, ''.join(str(legal_moves))))

        # if no more moves or reach the max depth
        if len(legal_moves) == 0 or depth > self.search_depth:
            if self.testing:print("search hits the bottom, return: ", self.score(game,self))
            return self.score(game, self), (-1, -1)

        if not maximizing_player:  # a min node
            best_value = [beta, 0]
            for move in legal_moves:
                new_game = game.forecast_move(move)
                old_value = best_value[0]
                best_value[0] = min(best_value[0],
                                 self.alphabeta(new_game, depth + 1, alpha, best_value[0], True)[0])
                if best_value[0] != old_value:
                    best_value[1] = move
                if best_value[0] < alpha:  # pruning
                    if self.testing: print("pruning")
                    return best_value

        else:  # a max node
            best_value = [alpha, 0]
            for move in legal_moves:
                new_game = game.forecast_move(move)
                old_value = best_value[0]
                best_value[0] = max(best_value[0],
                                 self.alphabeta(new_game, depth + 1, best_value[0], beta, False)[0],
                                 )
                if best_value[0] != old_value:
                    best_value[1] = move
                if best_value[0] > beta:  # pruning
                    if self.testing: print("pruning")
                    return best_value

        return best_value
