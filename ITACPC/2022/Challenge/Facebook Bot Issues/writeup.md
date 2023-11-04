# Calculating Dart Scores

Description [here](https://itacpc22.kattis.com/contests/itacpc22/problems/itacpc22.facebookbotissues).

In order to print `YES` two accounts, `a` and `b`, must share `K` friendships. One way to solve this problem is to get 2 lists, one containing `a` friends and the other `b` friends and get the intersection of said list, if the cardinality of this list is equal to `K` then we must print `YES`. We will use a for cycle to check every account and if no such relationship group is found then we will print `NO`.

Code is [here](./code.py).