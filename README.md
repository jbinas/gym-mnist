
# Mnist counter environment

An OpenAI gym environment implementing an n counters based on Mnist digits, as described in the "Variational Intrinsic Control" paper (https://arxiv.org/abs/1611.07507).

The environment state is described by n integers in {0, ..., 9}, one of which can be incremented/decremented through an action in each timestep. States wrap around. A random mnist digit corresponding to the respective class is sampled in every step, leading to an observation of size (28, n*28).

```
action 0: do nothing
action 1: increment digit 1
action 2: decrement digit 1
action 3: increment digit 2
....
```

There are currently three environments:

```
Mnist-s1-v0: 1 digits
Mnist-s2-v0: 2 digits
Mnist-s3-v0: 3 digits
```

Run as follows.

```
import gym
import gym_mnist

env = gym.make('Mnist-s2-v0')
obs = env.reset()
action = np.random.randint(5)
obs, rew, done, _ = env.step(action)
```

