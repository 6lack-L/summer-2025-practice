from typing import List
import random

def simple_random_sampling(data: List[float], sample_size: int) -> List[float]:
    """
    Perform simple random sampling from a dataset.
    
    :param data: The dataset to sample from.
    :param sample_size: The number of samples to draw.
    :return: A list of sampled data points.
    """
    if sample_size > len(data):
        raise ValueError("Sample size cannot be greater than the population size.")
    return random.sample(data, sample_size)

def stratified_sampling(data: List[float], strata: List[int], sample_size: int) -> List[float]:
    """
    Perform stratified sampling from a dataset.
    
    :param data: The dataset to sample from.
    :param strata: A list indicating the strata for each data point.
    :param sample_size: The total number of samples to draw.
    :return: A list of sampled data points.
    """
    stratified_samples = []
    strata_dict = {}
    
    for i, stratum in enumerate(strata):
        if stratum not in strata_dict:
            strata_dict[stratum] = []
        strata_dict[stratum].append(data[i])
    
    for stratum, values in strata_dict.items():
        stratum_sample_size = int(sample_size * (len(values) / len(data)))
        stratified_samples.extend(simple_random_sampling(values, stratum_sample_size))
    
    return stratified_samples

def systematic_sampling(data: List[float], sample_size: int) -> List[float]:
    """
    Perform systematic sampling from a dataset.
    
    :param data: The dataset to sample from.
    :param sample_size: The number of samples to draw.
    :return: A list of sampled data points.
    """
    if sample_size > len(data):
        raise ValueError("Sample size cannot be greater than the population size.")
    
    interval = len(data) // sample_size
    return [data[i] for i in range(0, len(data), interval)][:sample_size]