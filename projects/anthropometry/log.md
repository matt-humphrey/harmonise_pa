## Issue Log

### Discussions

- When there are multiple measurements (like for height), take the average, and drop the "raw" values (agreed in meeting 23/7).
- Avoid renaming variables unless required, to avoid additional work updating the PDFs.

### Questions

- Should I harmonise with Antenatal?
    - If so, can I harmonise "length" with "height"?
- Should I delete "avg" blood pressures when there are the 2 min increment versions?

### General

- Include and validate BMI for each follow-up
- For *_BP3 (blood pressure state), the field values/options have changed over time
- Protocol for regular exam blood pressure tests (different from resting/sitting?)
- The back-end of the Qs sometimes have Ave/Avg for things like weight or hip
    - Name the variable "avg" or just regular "weight", for example?
- Remove the "CIRC" from var_names
    - Just rename existing G208_HEAD!

- Add field type (TIME) for `banksia`

### Follow-up Specific

- Drop `G210_EXMR`? No label; any value?

#### Y0

- Double check the variables do align/harmonise
    - For example, length may actually be crown to rump (sitting height)

#### Y8

- For Y8, raw data (2019) contained no data for inter-scapular (A11) and no column for sitting height
- Be careful of G108_BP5_1 -> has nothing to do with *_BP_5 (poorly harmonised by John)
    - Effectively the same as G105_BPCD -> just need to tweak G105 to harmonise

#### Y14

- Strange that we have data for hip circ., even though not listed on assessment
    - Is specified for the protocol, just not in the actual data form -> check paper copy?
- Lots of variables to be renamed!
    - Change to more meaningful names for different blood pressures
- Was there a separate weight and height taken at the exam, or just avg of school and ICHR?
    -> final weight/height was just ICHR is available, otherwise school
- The noted exam blood pressures were an avg of the first two recordings -> drop
- Drop the additional derived blood pressure avgs
- Drop the avgs for hip and width, and hip-width ratio


#### Y17

- BP4 was dropped some time after "ayear16a.sav" from 26/11/2019 -> add back?
- Even though two measurements were taken from anthro data, even going back to superseded, it seems only the mean values has been recorded - how to harmonise?

#### Y20

- Calculate avg left and right wrist

#### Y22

- Cuff, time and temp of BP not harmonised with Y20 (is cuff variable options different?)

#### Y27

- Has AvSBP, AvDBP and AvHR - any different from the way these are normally calculated in the exam?
- Where did A6 (circ. arm) and A2B come from?

#### Y28

- Calculate avg height

#### G126



#### G0G1

- Discovered that labels for blood pressures were so rogue because of a change made by - you guessed it - John, in "G0G1_PA_202405271546.sav"
- Where is BP_TEMP? (noted on sheet, not in even superseded data)

### Variable Specific

#### Height

- started of measuring in cm, transitioned to m in G214
    - parent height was in cm still for G114 and G117 -> m in G126 and G0G1
- values of 999 occur in most datasets; 888 occurs in G0G1 also
- G0G1, four cases where height was between 78 and 86???
- how to handle values of 999 (and 888)? -> None, or is that valid?
