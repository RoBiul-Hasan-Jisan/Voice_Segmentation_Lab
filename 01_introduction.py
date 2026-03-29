
"""


sound and digital audio fundamentals.

"""

# ============================================================================
# WHAT IS SOUND?
# ============================================================================

# Sound is a mechanical vibration that travels through a medium 
# (like air, water, or solids) and can be heard when it reaches our ears.

# ============================================================================
# KEY PROPERTIES OF SOUND
# ============================================================================

# ----------------------------------------------------------------------------
# a) FREQUENCY (f)
# ----------------------------------------------------------------------------
# - Frequency is how many times a sound wave repeats in one second.
# - Measured in Hertz (Hz).
# - Determines the pitch of the sound:
#    - High frequency → high pitch (like a whistle)
#    - Low frequency → low pitch (like a drum)

# Example:
# A piano key might produce a frequency of 440 Hz (the A above middle C).

# ----------------------------------------------------------------------------
# b) AMPLITUDE
# ----------------------------------------------------------------------------
# Amplitude is the height of the sound wave.
# Determines the loudness:
#   - Larger amplitude → louder sound
#   - Smaller amplitude → quieter sound
# Measured in decibels (dB).

# Visual analogy:
# Think of waves in water: the higher the wave → more energy → louder sound.

# ============================================================================
#  ANALOG VS DIGITAL SIGNALS
# ============================================================================

# ANALOG SOUND
# Sound is naturally analog: continuous waves.
# Example: your voice or music from a guitar string.
# Represented as a smooth curve (continuous in time and amplitude).

# DIGITAL SOUND
# Computers cannot store continuous signals, so we sample the analog sound 
# and convert it into numbers.
# Result → digital signal (sequence of numbers).

# ============================================================================
#  SAMPLING
# ============================================================================

# Sampling is the process of measuring the amplitude of an analog signal 
# at discrete points in time.

# KEY TERMS
# ---------
# SAMPLING RATE / FREQUENCY (Fs)
# - How many times per second we measure the analog signal.
# - Measured in samples per second (Hz).
# - Examples:
#   - CD-quality audio → 44,100 Hz (44.1 kHz)
#   - Telephone → 8,000 Hz

# QUANTIZATION
# - After sampling, we approximate each amplitude value to the nearest number 
#   (digital value).
# - The more bits you use → more accurate digital representation.

# NYQUIST THEOREM
# ---------------
# To accurately capture a signal:
#   Sampling rate must be at least 2 × maximum frequency in the signal.
# If not → aliasing occurs (distorted sound).

# Example:
# Max human hearing = 20 kHz → sampling rate must be ≥ 40 kHz 
# (CD uses 44.1 kHz).

# ============================================================================
# DIGITAL SIGNAL REPRESENTATION
# ============================================================================

# After sampling and quantization, sound can be represented as a sequence 
# of numbers:

# Time (ms) | Analog Amplitude | Digital Value
# ----------|------------------|--------------
# 0.00      | 0.0              | 0
# 0.01      | 0.7              | 179
# 0.02      | 1.0              | 255
# 0.03      | 0.5              | 128

# These numbers can now be stored, processed, and transmitted digitally.
# You can apply filters, effects, or analysis on these digital numbers.

# ============================================================================
#  QUICK SUMMARY
# ============================================================================

summary = """
┌───────────────────┬────────────────────────────────────────────────────────┐
│ Concept           │ Meaning                                                │
├───────────────────┼────────────────────────────────────────────────────────┤
│ Sound             │ Mechanical vibrations traveling through a medium       │
├───────────────────┼────────────────────────────────────────────────────────┤
│ Frequency (Hz)    │ How fast the wave oscillates → pitch                   │
├───────────────────┼────────────────────────────────────────────────────────┤
│ Amplitude (dB)    │ Height of wave → loudness                              │
├───────────────────┼────────────────────────────────────────────────────────┤
│ Analog Signal     │ Continuous in time and amplitude                       │
├───────────────────┼────────────────────────────────────────────────────────┤
│ Digital Signal    │ Discrete in time and amplitude (numbers)               │
├───────────────────┼────────────────────────────────────────────────────────┤
│ Sampling Rate     │ How often we take measurements per second              │
├───────────────────┼────────────────────────────────────────────────────────┤
│ Quantization      │ Converting amplitude to nearest digital value          │
├───────────────────┼────────────────────────────────────────────────────────┤
│ Nyquist Theorem   │ Fs ≥ 2 × max frequency to avoid distortion             │
└───────────────────┴────────────────────────────────────────────────────────┘
"""
