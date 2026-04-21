# scripts/generate_data.py
import random
import os

# Configuration
NUM_INPUTS = 8
TIME_STEPS = 500
KEYWORDS = ["JARVIS", "MARK", "START", "STOP"]

def generate_spike_pattern(keyword_id, intensity=0.6):
    """
    Generates synthetic spike trains for specific keywords.
    Format: time_step neuron_id
    """
    spikes = []
    for t in range(TIME_STEPS):
        active_bands = []
        
        # Distinct patterns for each keyword
        if keyword_id == 0: # JARVIS (Low freq bands 0-3)
            active_bands = range(0, 4)
        elif keyword_id == 1: # MARK (High freq bands 4-7)
            active_bands = range(4, 8)
        elif keyword_id == 2: # START (Alternating 0,2,4,6)
            active_bands = [0, 2, 4, 6]
        elif keyword_id == 3: # STOP (Burst all bands at end)
            active_bands = range(0, 8) if t > 300 else []
            
        for neuron_id in active_bands:
            # Poisson-like probability
            if random.random() < intensity:
                spikes.append(f"{t} {neuron_id}")
    return spikes

def generate_weights():
    """
    Generates dummy 8-bit signed weights.
    Format: One weight per line.
    """
    weights = []
    # 8 Inputs * 16 Hidden Neurons = 128 weights
    for _ in range(NUM_INPUTS * 16): 
        weights.append(str(random.randint(-127, 127)))
    return weights

if __name__ == "__main__":
    # Ensure data directory exists
    if not os.path.exists("../data"):
        os.makedirs("../data")
        
    # 1. Generate Test Spikes (JARVIS Example)
    print("Generating test_spikes.txt (JARVIS Pattern)...")
    spikes = generate_spike_pattern(keyword_id=0, intensity=0.7)
    with open("../data/test_spikes.txt", "w") as f:
        f.write("\n".join(spikes))
        
    # 2. Generate Weights
    print("Generating weights.txt...")
    weights = generate_weights()
    with open("../data/weights.txt", "w") as f:
        f.write("\n".join(weights))
        
    print("✅ Done! Files saved to /data/")
    print("   - data/test_spikes.txt")
    print("   - data/weights.txt")
