import numpy as np
from math import sqrt
from typing import Callable, List
import matplotlib.pyplot as plt

from function_parser import *

GOLDEN_SEARCH_RATIO = (sqrt(5)+1)/2

POWELL_KWARGUMENTS ={"function",
                     "funInDirection",
                     "eps1",
                     "eps2",
                     "X_0",
                     "L",
                     "Xvariables",
                     "ax"   
}   


def powellsMethod(func: Callable[[float, float, float, float, float], float], start: List[float],
                   eps1: float, eps2: float, gssRange: List[float], maxIter: int, ax=None):
    # print(start)
    # input()
    dim = len(start)

    stepList = []
    dirVectors = np.identity(dim)
    currentIteration = 0

    points = np.zeros((dim+1, dim))
    startPoint = np.array(start)
   
    print("tutaj")
    print(maxIter)
    while(currentIteration < maxIter):

        points[0] = searchMinimumInDirection(func, dirVectors[0], startPoint, gssRange)
        currentIteration = currentIteration + 1

        for i in range(1, dim):
            points[i] = searchMinimumInDirection(
                func, dirVectors[i], points[i-1], gssRange)
            currentIteration = currentIteration + 1

        newDir = np.subtract(points[dim-1], startPoint)
        points[dim] = searchMinimumInDirection(func, newDir, points[dim-1], gssRange)

        for i in range(dim-1):
            dirVectors[i] = np.copy(dirVectors[i+1])
            
        dirVectors[dim-1] = np.copy(newDir)
        if any([any(np.isnan(x)) for x in points]):
            return 'Error', *points
        if(dim == 2 and ax!=None):
            #print(f'Line via {startPoint} {points[0]} {points[1]} {points[2]}')
            ax.plot([startPoint[0], points[0][0]], [
                     startPoint[1], points[0][1]], 'k-')
            ax.plot(startPoint[0], startPoint[1], marker='o',
                    markersize=3.5, markeredgecolor="red", markerfacecolor="red" )
            ax.plot([points[0][0], points[1][0]], [
                     points[0][1], points[1][1]], 'k-')
            ax.plot(points[0][0], points[0][1], marker='o',
                    markersize=3, markeredgecolor="gray", markerfacecolor="gray" )
            ax.plot([points[1][0], points[2][0]], [
                     points[1][1], points[2][1]], 'k-')
            ax.plot(points[1][0], points[1][1], marker='o',
                    markersize=3, markeredgecolor="gray", markerfacecolor="gray" )
            # if(can
            #     canvas.draw()vas!=None):
        l = points
        stepList.append(np.copy(startPoint))
        stepList.append(np.copy(l[:-1]))
        
        startPoint = np.copy(points[dim])
        diff = abs(func(*points[dim]) - func(*points[0]))
        
        print("tutaj2")
        print(currentIteration)
        currentIteration = currentIteration + 1
        if diff < eps2:
            return points[dim], func(*points[dim]), 'eps2', diff, stepList
        elif all([vectorLength(points[i],points[dim-1]) < eps1 for i in range(0,dim-1)]):
            return points[dim], func(*points[dim]), 'eps1',f'Value {[vectorLength(points[i],points[dim-1]) < eps1 for i in range(0,dim-1)]}', stepList
    
    return {'points':points[dim], 'func':func(*points[dim]), 'maxiter':'Max Iteration', 'iter': f'Iteration count: {currentIteration}','stepList': stepList}





def goldenSearch(f: Callable[[float, float, float, float, float], float], a: List[float], b: List[float], tol=0.001, iter=100):

    c = np.subtract(b, np.divide(np.subtract(b, a), GOLDEN_SEARCH_RATIO))
    d = np.add(a, np.divide(np.subtract(b, a), GOLDEN_SEARCH_RATIO))
    i = 0
    while vectorLength(np.zeros(len(a)), np.subtract(a, b)) > tol and i < iter:
        i = i+1
        if f(*c) < f(*d):  # f(c) > f(d) to find the maximum
            b = np.copy(d)
        else:
            a = np.copy(c)

        c = np.subtract(b, np.divide(np.subtract(b, a), GOLDEN_SEARCH_RATIO))
        d = np.add(a, np.divide(np.subtract(b, a), GOLDEN_SEARCH_RATIO))
    return np.divide(np.add(a, b), 2)


def vectorLength(startPoint:List[float], endPoint:List[float])->float:
    """Function calculate length of vector between 2 points

    Args:
        startPoint (List[float]): List of coordinates of startpoint
        endPoint (List[float]): List of coordinates of endpoint

    Returns:
        float: Length of vector between startpoint and endpoint
    """
    assert(len(startPoint) == len(endPoint))
    sum = 0
    for x in range(len(startPoint)):
        sum = sum + pow((endPoint[x] - startPoint[x]), 2)
    l = sqrt(sum)

    return l

def getVectorNorm(x: List[float]) -> List[float]:
    length = vectorLength(np.zeros(len(x)), x)
    if(length == 0):
        return [0 for v in x]
    return [v/length for v in x]


def searchMinimumInDirection(func: Callable[[float, float, float, float, float], float], direction: List[float],
                     startPoint: List[float], gssrange: List[float]) -> List[float]:
    normalizedDir = getVectorNorm(direction)
    #print(f'{startPoint} {normalizedDir} {gssrange}')
    
    p0 = [startPoint[i] + gssrange[0]*normalizedDir[i] for i in range(len(direction))]
    p1 = [startPoint[i] + gssrange[1]*normalizedDir[i] for i in range(len(direction))]

    #print(f'Minimize from {p0} to {p1}')
    return goldenSearch(func, p0, p1)


