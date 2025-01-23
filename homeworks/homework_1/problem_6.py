import sys
from random import uniform

if __name__ == "__main__": 
    # Extract N from shell (if specified)
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 100
    
    # Helper function to generate num_points 2d points uniform on the unit square
    def generate_sample(num_points): 
        sample = []
        for i in range(num_points):
            sample.append((uniform(-1.0,1.0), uniform(-1.0,1.0)))
        return sample
    
    # Generate sample of N points
    sample = generate_sample(N)

    # Make calculation and report
    pi = 4*(len(list(filter(lambda x: x[0]*x[0] + x[1]*x[1] <=1, sample)))/len(sample))
    print(f"\nPi is approximately {pi}\n\nUsed sample of size {N}\n")

