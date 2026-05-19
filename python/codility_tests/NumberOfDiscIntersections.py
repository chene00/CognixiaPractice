# Optimal Solution

def solution(A):
    N = len(A)
    
    # 1. Create separate arrays for start and end points
    starts = [0] * N
    ends = [0] * N
    
    for i in range(N):
        starts[i] = i - A[i]
        ends[i] = i + A[i]
        
    # 2. Sort both arrays (O(N log N) time)
    starts.sort()
    ends.sort()
    
    overlaps = 0
    active_discs = 0
    end_index = 0
    
    # 3. Scan through all the start points
    for start in starts:
        # If any discs have ended before this new disc starts,
        # decrement the active count and move to the next end point.
        while end_index < N and ends[end_index] < start:
            active_discs -= 1
            end_index += 1
            
        # The new disc intersects with all currently active discs
        overlaps += active_discs
        
        # Check the Codility limit constraint
        if overlaps > 10000000:
            return -1
            
        # The new disc is now active
        active_discs += 1
        
    return overlaps9