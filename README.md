# naturalselection
projects on natural selection, like primer

Doves = doves <br />
Hawks = hawks <br />
Randomers = 50/50 doves or hawks <br />
Shifters = Always picks dove/hawk that gives best outcome, but pays energy cost for big intelligence. <br />

In this simulation, we use the same model as Primer's video: "Simulating the Evolution of Aggression." <br />
There are a bunch of food piles, where either 1 creature or 2 creatures can get to a food pile at the same time. If just 1 creature gets there, they get 2 food = 2 energy (reproducing twice before dying), but if 2 creatures get there, they play a little game. We have a starting 95% chance of finding another creature, which scales proportionally with population (multiply by current_population/initial_population). <br />
Now for the game the 2 players play, there are 2 strategies; Dove and Hawk. Dove is "nice", Hawk is "selfish". If both play Dove, each player takes half the food pile (1 food each). But if one plays Hawk and one plays Dove, the Hawk will "go for the same piece of the food as the Dove and eat it, then quickly eat its half". This means Hawk gets 1.5, Dove gets 0.5 (50% chance of reproducing before dying). However if two Hawks meet, they spend ALL their energy fighting and both get 0. <br />
Under just the Dove/Hawk strategies, in the Primer video, the population forms a stable equilibrium at 50/50, and this is an attractor; as long as the population isn't 100% Dove or 100% Hawk, the underrepresented strategy will do better enough to bring it to 50/50. <br />
I wanted to try out some new strategies, so I added Randomers (randomly 50/50s Hawk or Dove), and Shifters (Chooses the option that gives most food, but pays a cost for intelligence). The cost for Shifters is a variable you can change (sval, line 30, currently at a -30% cost, or 0.7 multiplier). <br />
I also added mutation so now even 100% homogeneous populations will tend to an equilibrium. <br />
We run a 200-day sim using these standards. <br />
We then plot the results of this 200-day sim using pyplot (the number of creatures following each strategy over time), in a stackplot (all different types are stacked, but colored differently.) <br />
And that's it! <br />

You can change the initial numbers for Dove/Hawk/Shifters/Randomers on lines 84-87, and change the sim from 200 days to something else on line 138. <br />
Currently we have an initial 0.95 chance of meeting with 200 creatures: you can change the number of creatures on line 78, and the chance on line 137. <br />
We have a mutation rate of 0.001 (1/1000) on Line 169. <br />
