
"""


Sinusoids, DFT (Discrete Fourier Transform), 
and frequency domain analysis.
"""

import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# 1 SINUSOIDS 
# ============================================================================

sinusoid_info = """
┌─────────────────────────────────────────────────────────────────────────┐
│                         SINUSOID EQUATION                               │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│              x(t) = A × sin(2πft + φ)                                   │
│                                                                         │
│  Where:                                                                 │
│    A = Amplitude → Loudness                                             │
│    f = Frequency → Pitch                                                │
│    φ = Phase (phi) → Time shift                                         │
│                                                                         │
├─────────────────────────────────────────────────────────────────────────┤
│  IMPORTANT: Any sound = combination of many sinusoids                   │
│  This is the foundation of Fourier Analysis!                            │
└─────────────────────────────────────────────────────────────────────────┘
"""

# ============================================================================
#  WHAT IS DFT? (Discrete Fourier Transform)
# ============================================================================

dft_info = """
┌─────────────────────────────────────────────────────────────────────────┐
│                    TIME DOMAIN → FREQUENCY DOMAIN                       │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Time Domain:     How signal changes over time                          │
│  Frequency Domain: What frequencies exist inside the signal             │
│                                                                         │
│  DFT FORMULA:                                                           │
│                                                                         │
│         N-1                                                             │
│  X[k] = Σ  x[n] × e^(-j2πkn/N)                                          │
│         n=0                                                             │
│                                                                         │
│  Conceptually: DFT checks "How much of frequency k exists in signal?"   │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
"""

# ============================================================================
# INTUITION OF DFT
# ============================================================================

intuition_info = """
┌─────────────────────────────────────────────────────────────────────────┐
│                         DFT INTUITION                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  Think of DFT as a FREQUENCY DETECTOR:                                  │
│                                                                         │
│  Mixed Sound  ──────► DFT ──────► "100 Hz present"                      │
│                    │              "500 Hz present"                      │
│                    │              "1 kHz present"                       │
│                    │              "2 kHz present"                       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
"""

# ============================================================================
#  DFT1 vs DFT2 (Analysis vs Synthesis)
# ============================================================================

analysis_synthesis_info = """
┌─────────────────────────────────────────────────────────────────────────┐
│                    DFT1 (Analysis) vs DFT2 (Synthesis)                  │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  DFT1 → ANALYSIS                                                        │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │  Input:  x[n] (signal)                                          │    │
│  │  Output: X[k] (frequency components)                            │    │
│  │  Question: "What frequencies are present?"                      │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                         │
│  DFT2 → SYNTHESIS (IDFT - Inverse DFT)                                  │
│  ┌─────────────────────────────────────────────────────────────────┐    │
│  │  Input:  X[k] (frequency components)                            │    │
│  │  Output: x[n] (rebuilt signal)                                  │    │
│  │  Question: "Rebuild signal from frequencies?"                   │    │
│  └─────────────────────────────────────────────────────────────────┘    │
│                                                                         │
│  IDFT FORMULA:                                                          │
│                N-1                                                      │
│  x[n] = (1/N) Σ  X[k] × e^(j2πkn/N)                                     │
│                k=0                                                      │
│                                                                         │
│  DFT → BREAK signal  |  IDFT → REBUILD signal                           │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
"""

# ============================================================================
#  SINUSOIDS + DFT (VERY IMPORTANT)
# ============================================================================

sinusoid_dft_info = """
┌─────────────────────────────────────────────────────────────────────────┐
│                  SINUSOIDS + DFT - KEY CONCEPT                          │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│        DFT BASIS FUNCTIONS ARE SINUSOIDS                                │
│                                                                         │
│  Each frequency bin in DFT = one sinusoid                               │
│                                                                         │
│  Example:                                                               │
│    If signal = sin(2π × 100 × n)                                        │
│                                                                         │
│    DFT will show:                                                       │
│      • Peak at 100 Hz                                                   │
│      • Almost zero elsewhere                                            │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
"""

# ============================================================================
# FREQUENCY BINS
# ============================================================================

frequency_bins_info = """
┌─────────────────────────────────────────────────────────────────────────┐
│                        FREQUENCY BINS                                   │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  DFT gives DISCRETE frequencies:                                        │
│                                                                         │
│                    f_k = (k / N) × Fs                                   │
│                                                                         │
│  Where:                                                                 │
│    k = bin index (0, 1, 2, ..., N-1)                                    │
│    N = total number of samples                                          │
│    Fs = sampling rate                                                   │
│                                                                         │
│  EXAMPLE:                                                               │
│    Sampling rate = 1000 Hz                                              │
│    N = 10 samples                                                       │
│                                                                         │
│    Frequencies: 0, 100, 200, 300, 400, 500, 600, 700, 800, 900 Hz       │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
"""

# ============================================================================
# WHY DFT IS IMPORTANT
# ============================================================================

importance_info = """
┌─────────────────────────────────────────────────────────────────────────┐
│                    WHY DFT IS IMPORTANT                                 │
├─────────────────────────────────────────────────────────────────────────┤
│                                                                         │
│  DFT is used in:                                                        │
│                                                                         │
│      Audio Processing     → Equalizers, effects, pitch detection        │
│      Speech Recognition   → Feature extraction for AI                   │
│      Noise Removal        → Identify and remove unwanted frequencies    │
│      Image Processing     → JPEG compression, edge detection            │
│      Video Compression    → MPEG formats                                │
│      Data Analysis        → Finding patterns in signals                 │
│      AI & Machine Learning → Feature engineering for models             │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
"""

