#!/usr/bin/env python

"""Tests for `reclist` package."""

from reclist.datasets import *
from reclist.metrics.standard_metrics import mrr_at_k
from reclist.datasets import CoveoDataset, SpotifyDataset
from reclist.recommenders.prod2vec import CoveoP2VRecModel, SpotifyP2VRecModel
from reclist.reclist import CoveoCartRecList, SpotifySessionRecList
import random

def test_basic_dataset_downloading():
    pass
    #CoveoDataset()
    #MovieLensDataset()


def test_coveo_example():
    # get the coveo data challenge dataset as a RecDataset object
    coveo_dataset = CoveoDataset()

    # re-use a skip-gram model from reclist to train a latent product space, to be used
    # (through knn) to build a recommender
    model = CoveoP2VRecModel()
    x_train = random.sample(coveo_dataset.x_train, 2000)
    model.train(x_train, iterations=1)

    # instantiate rec_list object, prepared with standard quantitative tests
    # and sensible behavioral tests (check the paper for details!)
    rec_list = CoveoCartRecList(
        model=model,
        dataset=coveo_dataset
    )
    # invoke rec_list to run tests
    rec_list(verbose=True)

def test_spotify_example():
    pass
    # get the Spotify million playlist dataset as a RecDataset object
    # spotify_dataset = SpotifyDataset()

    # re-use a skip-gram model from reclist to train a latent product space, to be used
    # (through knn) to build a recommender
    # model = SpotifyP2VRecModel()
    # spotify_dataset._x_train = spotify_dataset._x_train[0:1000]
    #
    # spotify_dataset._x_test = spotify_dataset._x_test[0:20]
    #
    #
    # model.train(spotify_dataset._x_train, iterations=1)
    #
    # # instantiate rec_list object, prepared with standard quantitative tests
    # # and sensible behavioral tests (check the paper for details!)
    # rec_list = SpotifySessionRecList(
    #     model=model,
    #     dataset=spotify_dataset
    # )
    # # invoke rec_list to run tests
    # rec_list(verbose=True)


def test_mrr():
    """
    Testing MRR works as intended
    """
    list_a = [[0], [1]]
    list_b = [[0, 1], [1, 0]]
    list_c = [[2, 3], [0, 1]]

    assert mrr_at_k(list_b, list_a, 1) == 1
    assert mrr_at_k(list_c, list_a, 21) == 0.25
    assert mrr_at_k(list_c, list_a, 1) == 0
