
from .register import register


register(
    id='Mnist-s1-v0',
    entry_point='gym_mnist.mnist:MnistEnv1'
)

register(
    id='Mnist-s2-v0',
    entry_point='gym_mnist.mnist:MnistEnv2'
)

register(
    id='Mnist-s3-v0',
    entry_point='gym_mnist.mnist:MnistEnv3'
)
