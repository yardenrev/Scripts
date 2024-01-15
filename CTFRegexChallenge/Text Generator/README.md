# Random Paragraph Generator

This Python script generates a random paragraph consisting of various word types, each word type matching a specific regex. The generated paragraph includes sequences of different structures, and some of these sequences represent a flag.

## Word Types:

1. **Type 1 Word:**
   - Format: `\@[r-u]{0,1}[LOMN][TO]+\%`
   
2. **Type 2 Word:**
   - Format: `\#\d*JH[OWRKS]+\^`

3. **Type 3 Word:**
   - Format: `\+ ?[12]r[ENDPOT]{5}[YPE]+\$`

4. **Type 4 Word:**
   - Format: `\-[1-5]VD[ENDPOendpo]{4}[skypeSKYPE!]+\*`

## Flag Sequences:

- The script randomly embeds three flag sequences within the generated paragraph.
- Flag Formats: `TWljcm97ckVn`, `M1hfQ0FOX2`, `IzX0Z1Tn0KCg==`

## Usage:

1. Run the script to generate a random paragraph.
   ```bash
   Text_generator.py
