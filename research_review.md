# Research Review on AlphaGo
The game of Go has long been viewed as the most challenging of classic games for artificial intelligence owing to its enormous search space and the difficulty of evaluating board position. Here AlphaGo is a new approach to computer Go which beats the best player Sedol Lee in 4:1.

The main technique used to overcome this challenge is deep learning. First, a prior network was trained using supervised learning on 30 million positions from the KGS Go Server. It reached an accuracy of 57.0%. Then, the pre-trained policy network was improved by policy gradient reinforcement learning. The reward function of this stage is that +1 for a win, -1 for a lose, and 0 for all the moves in the game exclude the last one. Then it won more than 80% of games against the SL policy network. The final stage of training pipeline focuses on position evaluation, a value network was trained using reinforcement learning technique. 

To evaluate AlphaGo, an internal tournament was run among AlphaGo and several other Go programs. It reached 99.8% win rate in this tournament. In March 2016, AlphaGo beat the best human player of Go, Sedol Lee, in 4:1.

The key of success of AlphaGo is the power of deep learning. The convolutional neural network is able to extract high level features which are essensial to game evaluation and decision making. There are also plenty of amazing applications built on deep learning in recent years, and the game play in included. Deepmind, which developed the AlphaGo, has also develped the game-playing agents for Atari and StarCraft. They all built on deep reinforcement learning and achived a very good performance.


