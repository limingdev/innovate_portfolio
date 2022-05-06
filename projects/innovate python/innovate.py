# Python recap for innovate course
# I've shockingly not used github enough in the past so here's a recent project

import pandas as pd
import numpy
from typing import List

class UniqueTokenTask:
    DISTANCE_THRESHOLD = 5
    # start the task, add all tokens you want to check here
    all_tokens: set = set()

    # all of the unique tokens we want to return
    unique_tokens: set = set()

    def __init__(self, *, tokens: List[str]):
        '''
        Takes an array of keywords to check and stores them as a set
        '''
        self.all_tokens = set(tokens)
    
    @staticmethod
    def __calculate_levenschtein_distance(
            token1: str,
            token2: str
            ) -> int:
        distances = numpy.zeros((len(token1) + 1, len(token2) + 1))

        for t1 in range(len(token1) + 1):
            distances[t1][0] = t1

        for t2 in range(len(token2) + 1):
            distances[0][t2] = t2
            
        a = 0
        b = 0
        c = 0
        
        for t1 in range(1, len(token1) + 1):
            for t2 in range(1, len(token2) + 1):
                if (token1[t1-1] == token2[t2-1]):
                    distances[t1][t2] = distances[t1 - 1][t2 - 1]
                else:
                    a = distances[t1][t2 - 1]
                    b = distances[t1 - 1][t2]
                    c = distances[t1 - 1][t2 - 1]
                    
                    if (a <= b and a <= c):
                        distances[t1][t2] = a + 1
                    elif (b <= a and b <= c):
                        distances[t1][t2] = b + 1
                    else:
                        distances[t1][t2] = c + 1
        return int(distances[len(token1)][len(token2)])
            
            # return # distance int

    def __can_save_token(self, token: str) -> bool:
        for unique_token in self.unique_tokens:
            levenschtein_distance = self.__calculate_levenschtein_distance(unique_token, token)
            if levenschtein_distance < self.DISTANCE_THRESHOLD:
                return False
        return True

    def run(self) -> List[str]:
        for token in self.all_tokens:
            if self.__can_save_token(token):
                self.unique_tokens.add(token)

        return list(self.unique_tokens)


def main():
    lorem = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'.split()
    # Seperate text into list and remove punctuation
    list_of_keywords = [word.translate({ord(i): None for i in ',.'}) for word in lorem ]
    print(list_of_keywords)

    task = UniqueTokenTask(tokens=list_of_keywords)
    unique_keywords = task.run()
    print(unique_keywords)

if __name__ == '__main__':
    main()