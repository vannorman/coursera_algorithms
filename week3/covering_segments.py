# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    segments_a = sorted(segments, key = lambda x: x[0])
    segments_b = sorted(segments, key = lambda x: x[0])
    segments = sorted(segments, key = lambda x: x[0])
    
    # intuition: If any segment totally encompasses another, simply remove the larger segment
    # intiution: If i-th segment does not totally encompass another, you can pick the rightmost point of the i-th segment

    print("sorted:"+str(segments))
    ignored = []
    for i in range(len(segments)):
        print("\n\ni:"+str(i))
        s = segments[i]
        if len(points) > 0:
            last_pt = points[len(points)-1]
            if last_pt >= s[0] and last_pt <= s[1]:
                print("skipping segment "+str(s)+" as it was already touched by point "+str(last_pt))
                continue
        if i < len(segments) - 1: # not last segment
            print("\nchecking i:"+str(i)+', range:'+str(i)+" - "+str(len(segments)-1))
            skip = False
            for j in range(i+1,len(segments)): #iter over remaining only
                print("j:"+str(j))
                if segments[j][1] > segments[i][1]: # we are now outside i and don't need to check anymore
                    print("j ("+str(segments[j])+") got past i ("+str(segments[i])+")")
                    break
                if segments[j][0] > segments[i][0] and segments[j][1] < segments[i][1]: # j is encompassed by i, and i can be skipped
                    print("j ("+str(segments[j])+") is inside i ("+str(segments[i])+")")
                    skip = True
                else:
                    print("j ("+str(segments[j])+") is NOT inside i ("+str(segments[i])+")")
                    
            if skip: 
                print("skip at i;"+str(segments[i]))
                continue
        print("Append end at i;"+str(s))
        points.append(s.end)

    return points

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
